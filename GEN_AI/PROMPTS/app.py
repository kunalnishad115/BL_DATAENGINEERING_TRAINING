from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv
load_dotenv()

llm=HuggingFaceEndpoint(
  repo_id='Qwen/Qwen2.5-7B-Instruct',
  task="text-generation"
)

model=ChatHuggingFace(llm=llm)
chat_history=[]

while True:
  user_input=input('Human: ')
  chat_history.append(user_input)
  if user_input == 'exit':
    break
  res=model.invoke(chat_history)
  chat_history.append(res.content) 
  print("AI: ",res.content)
  
