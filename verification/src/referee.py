from checkio_referee import RefereeRank, ENV_NAME



import settings_env
from tests import TESTS


class Referee(RefereeRank):
    TESTS = TESTS
    ENVIRONMENTS = settings_env.ENVIRONMENTS

    DEFAULT_FUNCTION_NAME = "end_of_other"
    FUNCTION_NAMES = {
        "python_3": "end_of_other",
        "js_node": "endOfOther"
    }
    ENV_COVERCODE = {
        ENV_NAME.PYTHON: '''def cover(f, data):
    return f(set(data))'''
    }