import openai
import os
from dotenv import load_dotenv

class ContentAgent:
    def __init__(self):
        # Initialize OpenAI API with your key
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')

    def generate_content(self, prompt, customer_segment):
        personalized_prompt = f"For customer segment {customer_segment}: {prompt}"

        try:
            response = openai.Completion.create(
                engine="text-davinci-003",  # Use GPT-3 or GPT-4 model
                prompt=personalized_prompt,
                max_tokens=150
            )
            generated_content = response.choices[0].text.strip()
            return generated_content
        except Exception as e:
            print(f"Error generating content: {e}")
            return "Error generating personalized content."
