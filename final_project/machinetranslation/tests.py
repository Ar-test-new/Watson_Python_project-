import unittest
from translator import englishTofrench, frenchToenglish

class TestTranslator(unittest.TestCase):
  def test_englishToFrench(self):
    self.assertEqual(englishTofrench(None), '')
    self.assertEqual(englishTofrench('Hello'), 'Bonjour')
    self.assertEqual(englishTofrench('Goodbye'), 'Au revoir')

  def test_frenchToEnglish(self):
    self.assertEqual(frenchToenglish(None), '')
    self.assertEqual(frenchToenglish('Bonjour'), 'Hello')
    self.assertEqual(frenchToenglish('Au revoir'), 'Goodbye')

if __name__ =='__main__':
  unittest.main()