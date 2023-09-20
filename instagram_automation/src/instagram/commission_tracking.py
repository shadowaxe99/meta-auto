
import json
from instagram_private_api import Client

class CommissionTracking:
    def __init__(self, username, password):
        self.api = Client(username, password)

    def get_user_posts(self, user_id):
        results = self.api.user_feed(user_id)
        return results.get('items', [])

    def get_post_likes(self, post_id):
        results = self.api.media_info(post_id)
        return results.get('like_count', 0)

    def get_post_comments(self, post_id):
        results = self.api.media_info(post_id)
        return results.get('comment_count', 0)

    def calculate_commission(self, user_id):
        posts = self.get_user_posts(user_id)
        total_likes = sum(self.get_post_likes(post['id']) for post in posts)
        total_comments = sum(self.get_post_comments(post['id']) for post in posts)
        commission = 0.01 * total_likes + 0.02 * total_comments
        return commission

    def track_commission(self, user_id):
        commission = self.calculate_commission(user_id)
        with open(f'{user_id}_commission.json', 'w') as f:
            json.dump({'commission': commission}, f)

