from st2actions.runners.pythonrunner import Action
from zenpy import Zenpy


class BaseAction(Action):
    def __init__(self, config):
        super(BaseAction, self).__init__(config)
        assert self.config['password'] or self.config['token'] or self.config['oauth'], \
            'Need to specify either of password or token or oauth'
        # build credentials from the config object
        self.creds = {
            'subdomain': self.config['subdomain'],
            'email': self.config['username'],
            'password': self.config['password'],
            'token': self.config['token'],
            'oauth_token': self.config['oauth']
        }
        self.client = self._get_client()

    def _get_client(self):
        return Zenpy(**self.creds)
