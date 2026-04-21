# Loading the required libraries
from langchain_cerebras import ChatCerebras
from dotenv import load_dotenv
from app.config import config

def get_answer(docs,query):

    env_path = config['env']['env_path']
    load_dotenv(dotenv_path=env_path)
    llm = ChatCerebras(model=config['model']['model_name'])

    context = "\n\n".join(d.page_content for d in docs)


    prompt = f"""You are a helpful zerodha assistant.
    Answer only from the context below.

    If the answer is not present, say 'I dont know'

    context:
    {context}

    query:
    {query}
    """
    response = llm.invoke(prompt)

    return response
    



