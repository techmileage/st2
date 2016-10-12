from lib.actions import BaseAction
from zenpy.lib.exception import APIException, ZenpyException 

class DeleteTicket(BaseAction):
    def run(self, id):
        try:
            job_status = self.client.tickets.delete(Ticket(id=id))
            print('Delete Ticket Status: ', job_status['status'])
        except APIException as e:
            print('Deleting ticket with id {} failed with API exception {}'.format(id, e))
        except Exception as e:
            print('Deleting ticket with id {} failed with General exception {}'.format(id, e))
        pass
        

