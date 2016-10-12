from lib.actions import BaseAction
from zenpy.lib.exception import APIException, RecordNotFoundException 

class CloseTicket(BaseAction):
    def run(self, subject):
        try:
            tics = self.client.search(subject= subject, type='ticket')
            for tic in tics:
                tic.status='closed'
                job_status = self.client.tickets.update(tic)
                print('Closed Ticket Status: ', job_status['status'])
        except RecordNotFoundException as e:
            print('Ticket not found with subject {1}'.format(subject))
        except APIException as e:
            print('Api Exception occured while updating Ticket with subject {1}'.format(subject))
        except Exception as e:
            print('General Exception {1} occured while updating Ticket with subject {2}'.format(e, subject))
        pass
        

