import unittest
import main

class TestGame(unittest.TestCase):
    def setUp(self):
        print('\n=============start==============')
    
    def test_game_answer_correct(self):
        test_answer = 5
        gusser = 5
        result = main.guess_number(test_answer,gusser)
        self.assertTrue(result)
        
    def test_game_answer_wrong(self):
        test_answer = 9
        gusser = 5
        result = main.guess_number(test_answer,gusser)
        self.assertFalse(result)
        
    def test_game_answer_type(self):
        test_answer = 'test'
        gusser = 5
        result = main.guess_number(test_answer,gusser)
        self.assertFalse(result)
        
    def tearDown(self):
        print('=============end==============')
    
if __name__ == '__main__':    
    unittest.main()