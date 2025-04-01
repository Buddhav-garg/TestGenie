import openai

openai.api_key = "your_openai_api_key"  # Replace with your OpenAI API Key

def generate_test_cases(requirement):
    prompt = f"Generate detailed test cases for the requirement: {requirement}"
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]

# Example usage
user_story = "User should be able to log in with email and password."
print(generate_test_cases(user_story))
