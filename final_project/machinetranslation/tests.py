import unittest
from translator import french_to_english, english_to_french


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertTrue(french_to_english('null'),True)#test when null input is given as input the ouptut is null.
        self.assertEqual(french_to_english("Bonjour"),"Hello") #test when Bonjour is given as input the output is Hello.



class TestEnglishToFrench(unittest.TestCase): 
    def test2(self): 
        self.assertTrue(english_to_french('null'),True)#test when null input is given as input the ouptut is null.
        self.assertEqual(english_to_french("Hello"),"Bonjour") #test when hello is given as input the output is Bonjour.

unittest.main()