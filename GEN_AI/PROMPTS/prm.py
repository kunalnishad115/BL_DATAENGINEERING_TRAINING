from langchain_openai import ChatOpenAI  ## chat model 
from langchain_google_genai import ChatGoogleGenerativeAI ## chat model
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

docs=[
  "Delhi is the capital of India.",
  "Paris is the capital of France."
]
query='What is The Capital of India'


prompt = ChatPromptTemplate.from_template(
"""
You are a helpful AI assistant.

Use only the provided context.

If the answer cannot be found in the context, say:
"I don't have enough information."

Context:
{docs}

Question:
{query}

Answer:
"""
)

messages = prompt.invoke({
    "docs": "\n".join(docs),
    "query": query
})


llm = ChatOpenAI(
    model="llama-3.1-8b-instant",
    base_url="https://api.groq.com/openai/v1"
)

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
)


res_google=gemini_llm.invoke(messages)
print("GEMINI RES",res_google.content)

response = llm.invoke(messages)
print("GROQ RES",response.content)


