import unittest
import name_generator

class TestNameGeneration(unittest.TestCase):
	def test_name(self):
		self.assertEqual(name_generator.generate_full_name("John", "Smith"), "John Smith")
		self.assertEqual(name_generator.generate_full_name("Firstname", "Lastname"), "Firstname Lastname")

	def test_empty_string(self):
		self.assertEqual(name_generator.generate_full_name("Firstname", ""), "At least one of your inputs was an empty string.")
		self.assertEqual(name_generator.generate_full_name("", "Lastname"), "At least one of your inputs was an empty string.")
		self.assertEqual(name_generator.generate_full_name("", ""), "At least one of your inputs was an empty string.")
	
	def test_string_validity(self):
		self.assertEqual(name_generator.generate_full_name("1234", "5678"), "One of your inputs contained an invalid character.")
		self.assertEqual(name_generator.generate_full_name("F1rstnam3", "7astn4me"), "One of your inputs contained an invalid character.")
		self.assertEqual(name_generator.generate_full_name("Firstname", "7434"), "One of your inputs contained an invalid character.")

if __name__ == '__main__':
	unittest.main()
