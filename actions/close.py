from lib.actions import BaseAction
from zenpy.lib.api_objects import Comment
from zenpy.lib.exception import APIException, RecordNotFoundException


class CloseTicket(BaseAction):
    """Close ticket in zendesk
       input: subject for matching tickets
    """
    def run(self, subject, ticket_id):
        assert subject or ticket_id, 'subject or ticket id is required'
        try:
            # search for the tickets with subject match
            tics = self.client.search(ticket_id, subject=subject, type='ticket')
            for tic in tics:
                # update the ticket with status closed
                tic.status = 'closed'
                # comment on the ticket
                tic.comment = Comment(body='Closing the ticket')
                job_status = self.client.tickets.update(tic)
                print('Closed Ticket Status: ', job_status['status'])
        except RecordNotFoundException as e:
            print('Ticket not found with subject {}'.format(subject))
        except APIException as e:
            print('Api Exception occured while updating Ticket with subject {}'
                  .format(subject))
        except Exception as e:
            print('General Exception {} occured while updating Ticket with subject {}'
                  .format(e, subject))
        pass
