import os
import cohere
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))
PROMPT = """
You are an AI agent that provides informative text summaries. Write a summary from this given text input in no more than 3 sentences
"""

def summarize_text(text: str):
  print("Attempting to summarize text")
  response = co.summarize(
    text=text,
    length='short',
    format='paragraph',
    model='command',
    additional_command=PROMPT,
    temperature=0.3
  )
  return response