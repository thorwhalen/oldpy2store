import doctest
import oldpy2store.test.util
import oldpy2store.test.simple_test


t = doctest.testmod(oldpy2store.test.simple_test)
print(f"failed={t.failed} attempted={t.attempted}")

# def load_tests(loader, tests, ignore):
#     tests.addTests(doctest.DocTestSuite(oldpy2store.test.util))
#     return tests
#
#
# import unittest
# import os
# from pprint import pprint
#
#
# pprint(unittest.TestLoader().discover(os.path.dirname(__file__)))
