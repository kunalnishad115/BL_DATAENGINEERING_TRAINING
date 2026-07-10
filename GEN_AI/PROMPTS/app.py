from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
  repo_id='Qwen/Qwen2.5-7B-Instruct',
  task="text-generation"
)

model=ChatHuggingFace(llm=llm)

while True:
  user_input=input('Human: ')
  if user_input == 'exit':
    break
  res=model.invoke(user_input)
  print("AI: ",res.content)
  
  