import ast

def detect_errors(code: str) -> list:
    """
    Detect syntax errors in the code using the ast module.
    
    Parameters:
        code (str): The source code to analyze.
    
    Returns:
        list: A list of error messages (if any).
    """
    errors = []
    try:
        ast.parse(code)
    except SyntaxError as se:
        errors.append(f"SyntaxError on line {se.lineno}: {se.msg}")
    return errors

def fix_errors(code: str) -> str:
    """
    Attempt to fix common syntax errors in the code.
    
    This simple implementation replaces an incorrect assignment in conditionals
    (e.g., 'if x = 5:') with the correct equality operator ('if x == 5:').
    
    Parameters:
        code (str): The code to fix.
    
    Returns:
        str: The potentially corrected code.
    """
    errors = detect_errors(code)
    fixed_code = code
    if errors:
        # Naively replace '=' with '==' in simple conditionals; in production, use more robust logic.
        fixed_code = fixed_code.replace("if x = ", "if x == ")
    return fixed_code

if __name__ == "__main__":
    sample_code = "if x = 5:\n    print('Hello, world!')"
    print("Detected Errors:", detect_errors(sample_code))
    print("Fixed Code:\n", fix_errors(sample_code))
