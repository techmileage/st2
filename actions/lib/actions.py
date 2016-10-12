from st2actions.runners.pythonrunner import Action
from zenpy import Zenpy

class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        self.creds = {
            'subdomain' : self.config['subdomain'],
            'email': self.config['username'],
            'token' : self.config['token']
        }
        self.client = self._get_client()

    def _get_client(self):
        return Zenpy(instance_name, **self.creds)
