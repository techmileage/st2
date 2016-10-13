from lib.actions import BaseAction
from zenpy.lib.api_objects import Ticket, User, Comment 
from zenpy.lib.exception import RecordNotFoundException, APIException

class SearchNewTicketsAndUpdate(BaseAction):
    """ Search for new tickets and assign it """
    def run(self, subject):
        try:
            #search for the tickets that match the subject line and with the status 'new'
            tics = self.client.search(subject= subject, type='ticket', status= 'new')
            #process the list of ticket(s)
            for tic in tics:
                #find the user with email address in the config and assign him 
                tic.assignee = self.client.users(email=self.creds['email'])
                #Update the status to pending
                tic.status = 'pending'
                #comment on the ticket
                tic.comment = Comment(body='I am Working on it')
                self.client.tickets.update(tic)
        except RecordNotFoundException as e:
            print('Ticket/User not found with subject {1}. Exception is {2}'.format(subject, e))
        except APIException as e:
            print('Api Exception occured while updating Ticket with subject {1}'.format(subject))
        except Exception as e:
            print('General Exception {1} occured while updating Ticket with subject {2}'.format(e, subject))
        pass
