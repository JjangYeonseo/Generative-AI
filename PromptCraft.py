pip install openai

import openai

# Set up your OpenAI API key
openai.api_key = 'your-api-key-here'

def generate_detailed_prompt(keyword):
    """
    Generate a detailed prompt based on a given keyword.
    """
    # Define keyword-to-prompt mappings
    prompts = {
        'tech': "You are an expert in technology. Explain the latest advancements in artificial intelligence and how they impact everyday life.",
        'health': "You are a healthcare specialist. Describe the most effective strategies for maintaining a healthy lifestyle and managing chronic diseases.",
        'education': "You are an educator. Discuss the benefits and challenges of online learning compared to traditional classroom education.",
        'finance': "You are a financial advisor. Provide insights into effective personal finance management and investment strategies for beginners."
    }
    
    # Default prompt if keyword not found
    default_prompt = "Please provide more details or choose a specific topic."

    # Get the detailed prompt based on the keyword
    prompt = prompts.get(keyword.lower(), default_prompt)
    
    return prompt

def get_chatgpt_response(prompt):
    """
    Get a response from ChatGPT based on the generated prompt.
    """
    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )
    
    return response.choices[0].text.strip()

# Example usage
keyword = 'tech'  # This would be dynamically set in a real application
detailed_prompt = generate_detailed_prompt(keyword)
response = get_chatgpt_response(detailed_prompt)

print("Generated Prompt:")
print(detailed_prompt)
print("\nChatGPT Response:")
print(response)
