import unittest
from ai_module.debugger import detect_errors, fix_errors

class TestDebugger(unittest.TestCase):
    def test_detect_error(self):
        # Code with a syntax error: assignment used instead of equality
        code_with_error = "if x = 5:\n    print('Error')"
        errors = detect_errors(code_with_error)
        self.assertTrue(len(errors) > 0)
    
    def test_fix_error(self):
        code_with_error = "if x = 5:\n    print('Error')"
        fixed = fix_errors(code_with_error)
        # After fix, the code should not have syntax errors and must include '=='
        errors_after_fix = detect_errors(fixed)
        self.assertEqual(len(errors_after_fix), 0)
        self.assertIn("==", fixed)

if __name__ == "__main__":
    unittest.main()
