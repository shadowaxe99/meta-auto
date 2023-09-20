
import sys
from instagram import account_management, web_scraping, image_processing, social_media_automation, direct_messaging_automation, error_handling, logging, state_management, commission_tracking

def main():
    try:
        # Initialize account management
        account = account_management.AccountManagement()

        # Initialize web scraping
        scraper = web_scraping.WebScraping()

        # Initialize image processing
        image_processor = image_processing.ImageProcessing()

        # Initialize social media automation
        social_media = social_media_automation.SocialMediaAutomation()

        # Initialize direct messaging automation
        direct_messaging = direct_messaging_automation.DirectMessagingAutomation()

        # Initialize error handling
        error_handler = error_handling.ErrorHandling()

        # Initialize logging
        logger = logging.Logging()

        # Initialize state management
        state_manager = state_management.StateManagement()

        # Initialize commission tracking
        commission_tracker = commission_tracking.CommissionTracking()

        # Run the automation
        account.run()
        scraper.run()
        image_processor.run()
        social_media.run()
        direct_messaging.run()
        error_handler.run()
        logger.run()
        state_manager.run()
        commission_tracker.run()

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
