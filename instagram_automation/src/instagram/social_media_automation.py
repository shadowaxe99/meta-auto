
import time
from instagram_private_api import Client

class SocialMediaAutomation:
    def __init__(self, username, password):
        self.api = Client(username, password)

    def follow_user(self, user_id):
        self.api.friendships_create(user_id)
        time.sleep(2)

    def unfollow_user(self, user_id):
        self.api.friendships_destroy(user_id)
        time.sleep(2)

    def like_post(self, media_id):
        self.api.post_like(media_id)
        time.sleep(2)

    def unlike_post(self, media_id):
        self.api.delete_like(media_id)
        time.sleep(2)

    def comment_on_post(self, media_id, comment_text):
        self.api.post_comment(media_id, comment_text)
        time.sleep(2)

    def delete_comment(self, media_id, comment_id):
        self.api.delete_comment(media_id, comment_id)
        time.sleep(2)
