import json
import os
import requests

from prominence import auth
from prominence import exceptions

class ProminenceClient(object):
    """
    PROMINENCE client class
    """
    def __init__(self, timeout=30):
        self._url = os.environ['PROMINENCE_URL']
        self._timeout = timeout

        token = auth.get_token()
        if not token:
            raise exceptions.TokenError('Unable to obtain a token')

        self._headers = {"Authorization":"Bearer %s" % token}

    def list_jobs(self, completed, all, num, constraint):
        """
        List running/idle jobs or completed jobs
        """
        params = {}

        if completed:
            params['completed'] = 'true'

        if num:
            params['num'] = num

        if all:
            params['all'] = 'true'

        if constraint:
            params['constraint'] = constraint

        try:
            response = requests.get(self._url + '/jobs', params=params, timeout=self._timeout, headers=self._headers)
        except requests.exceptions.RequestException as e:
            raise exceptions.ConnectionError(e)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        elif response.status_code < 500:
            if 'error' in response.json():
                raise exceptions.JobGetError(response.json()['error'])
        raise exceptions.JobGetError('Unknown error')

    def list_workflows(self, completed, all, num, constraint):
        """
        List running/idle workflows or completed workflows
        """
        params = {}

        if completed:
            params['completed'] = 'true'

        if num:
            params['num'] = num

        if all:
            params['all'] = 'true'

        if constraint:
            params['constraint'] = constraint

        try:
            response = requests.get(self._url + '/workflows', params=params, timeout=self._timeout, headers=self._headers)
        except requests.exceptions.RequestException as e:
            raise exceptions.ConnectionError(e)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        elif response.status_code < 500:
            if 'error' in response.json():
                raise exceptions.WorkflowGetError(response.json()['error'])
        raise exceptions.WorkflowGetError('Unknown error')

    def create_job(self, job):
        """
        Create a job
        """
        return self.create_job_from_json(job.to_json())

    def create_job_from_json(self, job):
        """
        Create a job from a JSON description
        """
        data = job
        try:
            response = requests.post(self._url + '/jobs', json=data, timeout=self._timeout, headers=self._headers)
        except requests.exceptions.RequestException as e:
            raise exceptions.ConnectionError(e)

        if response.status_code == 201:
            if 'id' in response.json():
                return response.json()['id']
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        elif response.status_code < 500:
            if 'error' in response.json():
                raise exceptions.JobCreationError(response.json()['error'])
        raise exceptions.JobCreationError('Unknown error')

    def create_workflow(self, workflow):
        """
        Create a workflow
        """
        return self.create_workflow_from_json(workflow.to_json())

    def create_workflow_from_json(self, workflow):
        """
        Create a workflow from a JSON description
        """
        data = workflow
        try:
            response = requests.post(self._url + '/workflows', json=data, timeout=self._timeout, headers=self._headers)
        except requests.exceptions.RequestException:
            raise exceptions.ConnectionError(e)

        if response.status_code == 201:
            if 'id' in response.json():
                return response.json()['id']
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        elif response.status_code < 500:
            if 'error' in response.json():
                raise exceptions.WorkflowCreationError(response.json()['error'])
        raise exceptions.WorkflowCreationError('Unknown error')

    def delete_job(self, job_id):
        """
        Delete the specified job
        """
        return self.delete_generic(job_id, 'jobs')

    def delete_workflow(self, workflow_id):
        """
        Delete the specified workflow
        """
        return self.delete_generic(workflow_id, 'workflows')

    def delete_generic(self, id, resource):
        """
        Delete the specified job or workflow
        """
        try:
            response = requests.delete(self._url + '/%s/%d' % (resource, id), timeout=self._timeout, headers=self._headers)
        except requests.exceptions.RequestException:
            raise exceptions.ConnectionError(e)

        if response.status_code == 200:
            return True
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        elif response.status_code == 500:
            raise exceptions.DeletionError('Got a 500 internal server error from PROMINENCE')
        else:
            if 'error' in response.json():
                raise exceptions.DeletionError(response.json()['error'])
        raise exceptions.DeletionError('Unknown error')

    def describe_job(self, job_id):
        """
        Describe a specific job
        """
        try:
            response = requests.get(self._url + '/jobs/%d' % job_id, timeout=self._timeout, headers=self._headers)
        except requests.exceptions.RequestException:
            raise exceptions.ConnectionError(e)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        elif response.status_code < 500:
            if 'error' in response.json():
                return self.Response(return_code=1, data={'error': '%s' % response.json()['error']})
        raise exceptions.JobGetError('Unknown error')

    def describe_workflow(self, workflow_id):
        """
        Describe a specific workflow
        """

        try:
            response = requests.get(self._url + '/workflows/%d' % workflow_id, timeout=self._timeout, headers=self._headers)
        except requests.exceptions.RequestException:
            raise exceptions.ConnectionError(e)

        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        elif response.status_code < 500:
            if 'error' in response.json():
                return self.Response(return_code=1, data={'error': '%s' % response.json()['error']})

        raise exceptions.WorkflowGetError('Unknown error')

    def stdout_job(self, job_id):
        """
        Get standard output from a job
        """
        return self.stdout_generic('jobs', job_id)

    def stdout_workflow(self, job_id, job):
        """
        Get standard output from a workflow
        """
        return self.stdout_generic('workflows', job_id, job)

    def stdout_generic(self, type, id, job=None):
        """
        Get standard output from a job or workflow
        """
        if job is not None:
            path = '/%s/%d/%s/stdout' % (type, id, job)
        else:
            path = '/%s/%d/stdout' % (type, id)

        try:
            response = requests.get(self._url + path, timeout=self._timeout, headers=self._headers)
        except requests.exceptions.RequestException:
            raise exceptions.ConnectionError(e)

        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        else:
            if 'error' in response.json():
                raise exceptions.StdStreamsError(response.json()['error'])
        raise exceptions.StdStreamsError('Unknown error')

    def stderr_job(self, job_id):
        """
        Get standard error from a job
        """
        return self.stderr_generic('jobs', job_id)

    def stderr_workflow(self, job_id, job):
        """
        Get standard error from a workflow
        """
        return self.stderr_generic('workflows', job_id, job)

    def stderr_generic(self, type, id, job=None):
        """
        Get standard error from a job
        """
        if job is not None:
            path = '/%s/%d/%s/stderr' % (type, id, job)
        else:
            path = '/%s/%d/stderr' % (type, id)

        try:
            response = requests.get(self._url + path, timeout=self._timeout, headers=self._headers)
        except requests.exceptions.RequestException:
            raise exceptions.ConnectionError(e)

        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        else:
            if 'error' in response.json():
                raise exceptions.StdStreamsError(response.json()['error'])
        raise exceptions.StdStreamsError('Unknown error')

    def upload(self, file, filename):
        """
        Upload a file to transient cloud storage
        """   
        # Get Swift URL
        data = {'filename':file}
        
        try:
            response = requests.post(self._url + '/data/upload', json=data, headers=self._headers)
        except requests.exceptions.RequestException:
            raise exceptions.ConnectionError(e)

        if response.status_code == 201:
            if 'url' in response.json():
                url = response.json()['url']
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid PROMINENCE URL, got a 404 not found error')
        else:
            if 'error' in response.json():
                raise exceptions.FileUploadError(response.json()['error'])
            raise exceptions.FileUploadError('Unknown error when querying the PROMINENCE server')

        # Upload
        try:
            with open(filename, 'rb') as file_obj:
                response = requests.put(url, data=file_obj)
        except requests.exceptions.RequestException as e:
            raise exceptions.ConnectionError(e)     
        except IOError as e:
            raise exceptions.FileUploadError(e)

        if response.status_code == 201:
            return True
        elif response.status_code == 404:
            raise exceptions.ConnectionError('Invalid cloud storage URL, got a 404 not found error from cloud storage')

        raise exceptions.FileUploadError('Got status code', response.status_code, 'from cloud storage')

