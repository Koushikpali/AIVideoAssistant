from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough, RunnableLambda

import os 
def get_llm():
    return ChatMistralAI(model = "mistral-small-latest", mistral_api_key = os.getenv("MISTRAL_API_KEY"),temperature=0.3)

def split_text(transcription:str)->list:
    splitter=RecursiveCharacterTextSplitter(
         chunk_size=300,
    chunk_overlap=200,
    )
    return splitter.split_text(transcription)

def summarize(transcription:str)->str:
    llm=get_llm()
    map_prompt = ChatPromptTemplate.from_messages(
        [
        ("system", "Summarize this portion of a meeting transcript concisely."),
        ("human", "{text}"),
    ]
    )

    map_chain=map_prompt |llm |StrOutputParser()
    chunk_summarise=""
    chunks=split_text(transcription)
    for chunk in chunks:
        print(chunk)
        chunk_summarise+=map_chain.invoke({"text":chunk})
    
    combined_prompt = ChatPromptTemplate.from_messages(
    [
    (
        "system",
        "You are an expert meeting summarizer. Combine these partial summaries "
        "into one final professional meeting summary in bullet points.",
    ),
    ("human", "{text}"),
    ]
    )
     #didnt understand passthrough and lambda
    combined_chain = (
        # RunnablePassthrough() | RunnableLambda(lambda x:{"text":x})
       combined_prompt | llm | StrOutputParser()
    )

    return combined_chain.invoke({"text":chunk_summarise})

def generate_title(transcipt : str) -> str:
    llm = get_llm()

    

    title_chain = (
        # RunnablePassthrough() | RunnableLambda(lambda x:{"text":x}) | 
        ChatPromptTemplate.from_messages([
             (
                "system",
                "Based on the meeting transcript, generate a short professional meeting title "
                "(max 8 words). Only return the title, nothing else.",
            ),
            ("human", "{text}"),
        ])
        | llm
        |StrOutputParser()
    )

    return title_chain.invoke({"text":transcipt[:2000]})
