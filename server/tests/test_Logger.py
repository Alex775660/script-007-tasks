import Logger
import pytest

@pytest.fixture(scope='function')
def case_get_logger_message_explicit():
    yield 'example message'

# Test suite
class TestMyLogger:

    logger = Logger.LoggerInstance()    # logger with default settings

    def test_print_error(self, case_get_logger_message_explicit):
        assert case_get_logger_message_explicit == 'example message'
        self.logger.print_error(case_get_logger_message_explicit)


    def test_print_warning(self, case_get_logger_message_explicit):
        assert case_get_logger_message_explicit == 'example message'
        self.logger.print_warning(case_get_logger_message_explicit)


    def test_print_info(self, case_get_logger_message_explicit):
        assert case_get_logger_message_explicit == 'example message'
        self.logger.print_info(case_get_logger_message_explicit)


    def test_print_debug(self, case_get_logger_message_explicit):
        assert case_get_logger_message_explicit == 'example message'
        self.logger.print_debug(case_get_logger_message_explicit)
