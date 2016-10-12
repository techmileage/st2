from lib.actions import BaseAction
from zenpy.lib.api_objects import Ticket
from zenpy.lib.exception import APIException

class AddTicket(BaseAction):
     def run(self, subject, description):
        try:
            newTicket = Ticket(subject=subject, description=description)
            response = self.client.tickets.create(newTicket)
            id = response['ticket']['id']
        except APIException as e:
            print('Adding ticket with subject {1} failed with API exception {2}'.format(subject, e))
        except Exception as e:
            print('Adding ticket with subject {1} failed with General exception {2}'.format(subject, e))
        return id

