import unittest
from ai_module.code_generation import generate_code

class TestCodeGeneration(unittest.TestCase):
    def test_sort_function_generation(self):
        prompt = "Write a Python function to sort a list of integers."
        generated = generate_code(prompt)
        # Check that the generated code contains a function definition and 'sort'
        self.assertIn("def", generated)
        self.assertIn("sort", generated)
    
    def test_add_function_generation(self):
        prompt = "Write a Python function to add two numbers."
        generated = generate_code(prompt)
        self.assertIn("def", generated)
        self.assertIn("add", generated)
    
if __name__ == "__main__":
    unittest.main()
