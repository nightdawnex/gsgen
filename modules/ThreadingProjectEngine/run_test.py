import json
import os
import shutil
import sys

from . import config
from .thread_test import ThreadTest 
from .project_config import ThreadTestCase
from core.managers import TestManager
from core.managers.test_manager import TestCase

def run_test_case(test_case: ThreadTestCase):
    test_obj = ThreadTest(test_case.thread_num)
    pass_all = True
    msg = ''
    for method_name in test_case.methods:

        rtn = getattr(test_obj, method_name)()
        pass_all &= rtn[0]
        if rtn[1]:
            msg += rtn[1] + '\n'
    
    test_result = TestCase(name=test_case.name, max_score=test_case.max_score, visibility=test_case.visibility)
    if pass_all:
        test_result.score = test_case.max_score    
    else:
        test_result.score = 0

    test_result.msg = msg
    TestManager.add_test(test_result)


def run_all_test():
    from . import config
    tests = config.test
    for test in tests:
        run_test_case(test)

