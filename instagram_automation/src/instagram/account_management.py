
from instagram_private_api import Client, ClientCompatPatch

class InstagramAccountManager:
    def __init__(self, username, password):
        self.api = Client(username, password)

    def get_user_info(self, user_id):
        user_info = self.api.user_info(user_id)
        return user_info

    def follow_user(self, user_id):
        self.api.friendships_create(user_id)

    def unfollow_user(self, user_id):
        self.api.friendships_destroy(user_id)

    def post_image(self, image_path, caption):
        media = self.api.media_upload(image_path)
        self.api.media_configure(media['upload_id'], caption)

    def send_direct_message(self, user_id, message):
        thread = self.api.direct_message(user_id, message)
        return thread

    def get_followers(self, user_id):
        followers = self.api.user_followers(user_id)
        return followers

    def get_following(self, user_id):
        following = self.api.user_following(user_id)
        return following
