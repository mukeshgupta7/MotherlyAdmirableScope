from transformers import pipeline

class ContentAgent:
    def __init__(self):
        # Load GPT-2 model from Hugging Face
        self.generator = pipeline('text-generation', model='gpt2')

    def generate_content(self, prompt, customer_segment):
        # Create a personalized prompt based on the customer segment
        personalized_prompt = f"For customer segment {customer_segment}: {prompt}"

        # Use Hugging Face's GPT-2 model to generate personalized content
        try:
            response = self.generator(personalized_prompt, max_length=150, num_return_sequences=1)
            generated_content = response[0]['generated_text'].strip()
            return generated_content
        except Exception as e:
            print(f"Error generating content: {e}")
            return "Error generating personalized content."
