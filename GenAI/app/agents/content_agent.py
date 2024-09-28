"""
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
            return "Error generating personalized content."""

# from transformers import pipeline

# class ContentAgent:
#     def __init__(self):
#         # Load GPT-2 model from Hugging Face
#         self.generator = pipeline('text-generation', model='gpt2')

#     def generate_content(self, prompt, customer_segment):
#         # Create a personalized prompt based on the customer segment
#         personalized_prompt = f"For customer segment {customer_segment}: {prompt}"
        
#         # Use Hugging Face's GPT-2 model to generate personalized content
#         try:
#             response = self.generator(personalized_prompt, max_length=150, num_return_sequences=1)
#             generated_content = response[0]['generated_text'].strip()
#             return generated_content
#         except Exception as e:
#             print(f"Error generating content: {e}")
#             return "Error generating personalized content."


from textblob import TextBlob

class ContentAgent:
    def generate_content(self, prompt, customer_segment):
        personalized_prompt = f"For customer segment {customer_segment}: {prompt}"

        # Use simple rule-based text processing (TextBlob)
        blob = TextBlob(personalized_prompt)
        summary = blob.noun_phrases  # Extracts key phrases
        return f"Generated text: {summary}"
