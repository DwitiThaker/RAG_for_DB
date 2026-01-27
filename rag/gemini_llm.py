
from langchain_openai import ChatOpenAI

_llm = None  


from langchain_openai import ChatOpenAI
from utils.timing import log_time

_llm = None 


@log_time("OpenAI LLM")
def get_openai_llm():
    global _llm
    if _llm is None:
        print("🔌 Initializing OpenAI LLM (once)...")
        _llm = ChatOpenAI(
            model="gpt-4o-mini",   
            temperature=0,         
            max_tokens=250,        
        )
    return _llm




