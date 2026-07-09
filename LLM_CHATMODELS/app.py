from langchain_openai import ChatOpenAI  ## chat model 
from langchain_google_genai import ChatGoogleGenerativeAI ## chat model

from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOpenAI(
    model="llama-3.1-8b-instant",
    base_url="https://api.groq.com/openai/v1"
)

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
)


res_google=gemini_llm.invoke("when i add the 90+90 what i got ?")
print("GEMINI RES",res_google.content)

response = llm.invoke("when i add the 90+90 what i got ?")
print("GROQ RES",response.content)


