from lib.actions import BaseAction
from zenpy.lib.exception import APIException, ZenpyException 

class DeleteTicket(BaseAction):
    """ Delete tickets with matching id """
    def run(self, id):
        try:
            #find the matching ticket
            tic = self.client.search(type='ticket', id=id) 
            #delete the ticket now 
            job_status = self.client.tickets.delete(tic)
            print('Delete Ticket Status: ', job_status['status'])
        except APIException as e:
            print('Deleting ticket with id {} failed with API exception {}'.format(id, e))
        except Exception as e:
            print('Deleting ticket with id {} failed with General exception {}'.format(id, e))
        pass

