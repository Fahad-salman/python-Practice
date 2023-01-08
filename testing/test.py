import unittest
import main

class TestMain(unittest.TestCase):
    def setUp(self):
        print('About this function')
    
    def test_do_stuff(self): # test is equal the same value ?
        ''' test the function'''
        test_param = 10 
        result = main.do_stuff(test_param)
        self.assertEqual(result, 15)
        
    def test_do_stuff2(self): # test is it int or else then raise exception
        test_param = 'Test parameter' 
        result = main.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff3(self): # test is it a None value ? then will return the same result at line 18 ?
        test_param = None
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')
        
    def test_do_stuff4(self): # test is it a empty string ? then will return the same result at line 23 ?
        test_param = ''
        result = main.do_stuff(test_param)
        self.assertEqual(result, 'Please enter a number')
        
    def tearDown(self):
        print('clean up')
        
if __name__ == '__main__':
    unittest.main()