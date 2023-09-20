
from instagram_private_api import Client, ClientCompatPatch

class DirectMessagingAutomation:
    def __init__(self, username, password):
        self.api = Client(username, password)

    def send_message(self, user_id, message):
        try:
            self.api.direct_message(user_id, message)
            return True
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return False

    def send_bulk_messages(self, user_ids, message):
        for user_id in user_ids:
            self.send_message(user_id, message)

