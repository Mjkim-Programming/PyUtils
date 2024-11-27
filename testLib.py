import unittest
from lib import *

class Tests(unittest.TestCase):
    def test_typeFromStringToInt(self):
        for i in range(0,10):
            typeChanged = changeFrom(str(i)).To("Int")
            self.assertEqual(typeOf(typeChanged), typeOf(i), f'[TEST CASE {i}] It must be INT TYPE.')
            self.assertEqual(typeChanged, int(str(i)), f'[TEST CASE {i}] It must work exactly same as int() function.')
            self.assertEqual(typeChanged, i, f'[TEST CASE {i} It must be same as FLOAT NUMBER,')
    
    def test_typeFromStringToFloat(self):
        for i in range(0,10):
            typeChanged = changeFrom(str(0.1*i)).To("Float")
            self.assertEqual(typeOf(typeChanged), typeOf(0.1*i), f'[TEST CASE {i}] It must be FLOAT TYPE.')
            self.assertEqual(typeChanged, float(str(0.1*i)), f'[TEST CASE {i}] It muse work exactly same as float() function.')
            self.assertEqual(typeChanged, 0.1*i, f'[TEST CASE {i}] It must be same as FLOAT NUMBER.')            

    def test_typeFromIntToBool(self):
        typeChanged = changeFrom(0).To("Bool")
        self.assertTrue(not typeChanged, f'[TEST CASE 1] It must be TRUE.')
        self.assertFalse(typeChanged, f'[TEST CASE 2] It must be FALSE.')

    def test_throwError(self):
        with self.assertRaises(Exception): throwError("a")
        
if __name__ == "__main__":
    unittest.main();