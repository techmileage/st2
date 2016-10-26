from lib.actions import BaseAction
from zenpy.lib.exception import APIException
# from zenpy.lib.exception import ZenpyException


class DeleteTicket(BaseAction):
    """ Delete tickets with matching id """
    def run(self, ticket_id):
        try:
            # find the matching ticket (retuns generator)
            tic = self.client.search(type='ticket', ticket_id)
            # delete the ticket now
            job_status = self.client.tickets.delete(tic.next())
            print('Delete Ticket Status: ', job_status)
            # return job status
            return job_status
        except APIException as e:
            print('Deleting ticket with id {} failed with API exception {}'
                  .format(ticket_id, e))
        except Exception as e:
            print('Deleting ticket with id {} failed with General exception {}'
                  .format(ticket_id, e))
