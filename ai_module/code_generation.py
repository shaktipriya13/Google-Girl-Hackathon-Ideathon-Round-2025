import os
import openai

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_code(prompt: str) -> str:
    """
    Generate a code snippet using OpenAI's ChatCompletion API (GPT-4).
    
    Parameters:
        prompt (str): Natural language instruction for code generation.
    
    Returns:
        str: The generated code snippet.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful coding assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.2,
            max_tokens=256,
        )
        generated_code = response.choices[0].message["content"].strip()
        return generated_code
    except Exception as e:
        return f"Error generating code: {str(e)}"

if __name__ == "__main__":
    sample_prompt = "Write a Python function to sort a list of integers."
    print("Generated Code:")
    print(generate_code(sample_prompt))
