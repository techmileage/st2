from lib.actions import BaseAction
from zenpy.lib.api_objects import Comment
from zenpy.lib.exception import RecordNotFoundException, APIException


class SearchNewTicketsAndUpdate(BaseAction):
    """ Search for new tickets and assign it """
    def run(self, subject, ticket_id):
        assert subject or ticket_id, 'subject or ticket id is required'
        try:
            # search for the tickets that match the subject line and with the status 'new'
            tics = self.client.search(ticket_id, subject=subject, type='ticket', status='new')
            # process the list of ticket(s)
            for tic in tics:
                # Update the status to pending
                tic.status = 'pending'
                # comment on the ticket
                tic.comment = Comment(body='I am Working on it')
                self.client.tickets.update(tic)
        except RecordNotFoundException as e:
            print('Ticket not found. Exception is {}'.format(e))
        except APIException as e:
            print('Api Exception occured while updating Ticket with subject {}'
                  .format(subject))
        except Exception as e:
            print('General Exception {} occured while updating Ticket with subject {}'
                  .format(e, subject))
