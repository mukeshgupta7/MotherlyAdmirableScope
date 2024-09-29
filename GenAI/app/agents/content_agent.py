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

# from transformers import pipeline

# class ContentAgent:
#     def __init__(self):
#         self.summarizer = pipeline('summarization')

#     def generate_content(self, prompt, customer_segment):
#         personalized_prompt = f"For customer segment {customer_segment}: {prompt}"

#         # Use a pre-trained language model for text processing
#         summary = self.summarizer(personalized_prompt, max_length=50, min_length=30, do_sample=False)
#         return f"Generated text: {summary}"

# import spacy

# class ContentAgent:
#     def __init__(self):
#         self.nlp = spacy.load("en_core_web_sm")

#     def generate_content(self, prompt, customer_segment):
#         personalized_prompt = f"For customer segment {customer_segment}: {prompt}"

#         # Use spaCy for text processing
#         doc = self.nlp(personalized_prompt)
#         summary = [chunk.text for chunk in doc.noun_chunks]
#         return f"Generated text: {summary}"

import spacy
from transformers import T5ForConditionalGeneration, T5Tokenizer

class ContentAgent:
    def __init__(self):
        self.nlp = spacy.load("en_core_web_sm")
        self.t5_model = T5ForConditionalGeneration.from_pretrained('t5-small')
        self.t5_tokenizer = T5Tokenizer.from_pretrained('t5-small')

    def generate_content(self, prompt, customer_segment):
        personalized_prompt = f"Create a marketing message for customer segment {customer_segment} based on the following prompt: {prompt}"

        # Use spaCy for text processing
        doc = self.nlp(personalized_prompt)
        keywords = [token.text for token in doc if token.pos_ == "NOUN" or token.pos_ == "VERB"]

        # Use T5 model to generate marketing content
        input_ids = self.t5_tokenizer.encode("generate marketing content", return_tensors="pt")
        attention_mask = self.t5_tokenizer.encode("generate marketing content", return_tensors="pt", max_length=512, padding="max_length", truncation=True)
        output = self.t5_model.generate(input_ids, attention_mask=attention_mask, num_beams=4, no_repeat_ngram_size=2, min_length=50, max_length=200)

        # Post-processing to make the content more engaging
        generated_content = self.t5_tokenizer.decode(output[0], skip_special_tokens=True)
        generated_content = generated_content.replace("generate marketing content", "")
        generated_content = generated_content.capitalize()
        generated_content = generated_content + " " + ", ".join(keywords)

        return generated_content
