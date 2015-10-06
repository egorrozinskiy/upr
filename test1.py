import unittest
import lib
import math
class Libtest(unittest.TestCase):
    def test_even_non_negative_arg(self):
        self.assertEqual(lib.even(2), True)
        self.assertEqual(lib.even(-1), False)
        self.assertEqual(lib.even(4), True)
        self.assertEqual(lib.even(-3), False)   
        self.assertEqual(lib.even(0), True)
        self.assertEqual(lib.even(-5), False) 
    def test_factorial_negative(self):
        self.assertEqual(lib.factorial(-1),1)
    def test_factorial1_negative(self):   
        self.assertEqual(lib.factorial(-2),1)
    def test_factorial2_negative(self):
        self.assertEqual(lib.factorial(2),2)      
        self.assertEqual(lib.factorial(3),6) 
        self.assertEqual(lib.factorial(4),24) 
        self.assertEqual(lib.factorial(5),120)   
    def test_palindrome_negative(self):
        self.assertEqual(lib.palindrome('aba'), True)
        self.assertEqual(lib.palindrome('aabb'), False)
        self.assertEqual(lib.palindrome('abb'), False)
    def test_palindrome1_negative(self):
        self.assertEqual(lib.palindrome('aaaaa'), True)
    def test_palindrome2_negative(self):
        self.assertEqual(lib.palindrome('aa'), True)
    def test_prime_negative(self):
        self.assertEqual(lib.prime(2), True)
        self.assertEqual(lib.prime(3), True)
        self.assertEqual(lib.prime(6), True)
        self.assertEqual(lib.prime(-1), True)
        self.assertEqual(lib.prime(10), False)
        self.assertEqual(lib.prime(11), False)
    def test_sin_negative(self):
        self.assertEqual(lib.sin(math.pi), 0)
    def test_sin1_negative(self):
        self.assertEqual(lib.sin(math.pi/2), 1)
        self.assertEqual(lib.sin(math.pi/6), 0.5)
    def test_sqrt_non_negative_arg(self): 
        self.assertEqual(lib.sqrt(9), 3)
        self.assertEqual(lib.sqrt(1), 1)
        self.assertEqual(lib.sqrt(0), 0)
    def test_sqrt_negative(self):
        self.assertEqual(lib.sqrt(-1), 0)
      
unittest.main(verbosity=2)
