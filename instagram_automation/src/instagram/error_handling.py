
import logging
from instagram_private_api.errors import ClientError

logger = logging.getLogger(__name__)

def handle_error(e):
    if isinstance(e, ClientError):
        logger.error(f"Instagram API Error: {e}")
    else:
        logger.error(f"Unexpected Error: {e}")

def handle_response(response):
    if response.get('status') != 'ok':
        logger.error(f"Bad Response: {response}")
