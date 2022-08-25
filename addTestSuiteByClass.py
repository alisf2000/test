# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 21:15:38 2022

@author: pc2
"""

import unittest
import Namava 
# from test_by_id import TestCaseDetailsById
# from test_details_by_name import TestCaseDetailsByNmae
from HTMLTestRunner import HTMLTestRunner

def test_suite():
    
    # test2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDetailsById)
    # test3 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDetailsByNmae)
    test1 = unittest.TestLoader().loadTestsFromTestCase(Namava)
    suite = unittest.TestSuite(test1)
    
    filename = 'C:\\Users\pc2\\Documents\\py3\\py3result.html'
    fp = open(filename, 'wb')
    #define test report
    runner = HTMLTestRunner(
        log=True,
        stream=fp,
        verbosity=2, title='Test report'
                         , description="HTMLTestReport"
    )
    
    runner.run(suite)
if __name__ == '__main__':
    test_suite()