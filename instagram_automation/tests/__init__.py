
# This is the __init__.py file for the tests package

# Importing necessary modules for testing
import unittest

# Importing test modules
from .test_account_management import TestAccountManagement
from .test_web_scraping import TestWebScraping
from .test_image_processing import TestImageProcessing
from .test_social_media_automation import TestSocialMediaAutomation
from .test_direct_messaging_automation import TestDirectMessagingAutomation
from .test_error_handling import TestErrorHandling
from .test_logging import TestLogging
from .test_state_management import TestStateManagement
from .test_commission_tracking import TestCommissionTracking

# Defining the test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestAccountManagement))
    suite.addTest(unittest.makeSuite(TestWebScraping))
    suite.addTest(unittest.makeSuite(TestImageProcessing))
    suite.addTest(unittest.makeSuite(TestSocialMediaAutomation))
    suite.addTest(unittest.makeSuite(TestDirectMessagingAutomation))
    suite.addTest(unittest.makeSuite(TestErrorHandling))
    suite.addTest(unittest.makeSuite(TestLogging))
    suite.addTest(unittest.makeSuite(TestStateManagement))
    suite.addTest(unittest.makeSuite(TestCommissionTracking))
    return suite

# Running the test suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
