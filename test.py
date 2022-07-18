from multiprocessing import connection
import unittest

import db 
import flask
import json
#import server

class DBTestSuite(unittest.TestCase):

    def setUp(self):
        self.DB=db.DB("localhost","root","root","sys")

    def test_connect(self):
        self.assertIsNotNone(self.DB.connection)
    
    def test_get_tables(self):
        # result is list and elements are strings
        result=self.DB.get_tables()
        self.assertIsInstance(result,list)
        for table in result:
            self.assertIsInstance(table,str)

    

if __name__ == '__main__':
	unittest.main()
