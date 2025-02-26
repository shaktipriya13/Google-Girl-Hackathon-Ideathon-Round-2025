import re

def generate_unit_tests(code: str) -> str:
    """
    Generate unit tests based on the provided code snippet.
    
    Parameters:
        code (str): The source code for which tests should be generated.
    
    Returns:
        str: A string containing generated unit test code.
    """
    tests = ""
    if re.search(r"def\s+add\s*\(", code):
        tests = (
            "import unittest\n\n"
            "class TestAddFunction(unittest.TestCase):\n"
            "    def test_add_positive(self):\n"
            "        self.assertEqual(add(2, 3), 5)\n\n"
            "    def test_add_negative(self):\n"
            "        self.assertEqual(add(-1, -1), -2)\n\n"
            "if __name__ == '__main__':\n"
            "    unittest.main()\n"
        )
    elif re.search(r"def\s+sort_array\s*\(", code):
        tests = (
            "import unittest\n\n"
            "class TestSortArray(unittest.TestCase):\n"
            "    def test_sort_array(self):\n"
            "        self.assertEqual(sort_array([3, 1, 2]), [1, 2, 3])\n\n"
            "if __name__ == '__main__':\n"
            "    unittest.main()\n"
        )
    else:
        tests = "# No specific unit tests generated for the provided code snippet."
    return tests

if __name__ == "__main__":
    sample_code = "def add(a, b):\n    return a + b"
    print("Generated Unit Tests:\n", generate_unit_tests(sample_code))
