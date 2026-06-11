from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document


def get_embeddings():
           return  HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def declare_vector_DB():
                    embeddings=get_embeddings()
                    vector_store = Chroma(
                    collection_name="ai-video-assistant",
                    embedding_function=embeddings,
                      persist_directory="./chroma_langchain_db"
                )
                    return vector_store

def build_vector_store(transcript : str)->Chroma:
                print("Building vector Store")

                splitter=RecursiveCharacterTextSplitter(
                        chunk_size=32,
                        chunk_overlap=0,
                    
                    )
                spillted_sentences=splitter.split_text(transcript)
                documents=[]
                for index, docs in enumerate(spillted_sentences):
                        document=Document(page_content=docs,
                                          id=index)
                        documents.append(document)
                
                embeddings = get_embeddings()

                print(documents)

                vector_store = Chroma.from_documents(
                                            documents= documents,
                                            embedding=embeddings,
                                            collection_name="ai-video-assistant",
                                            persist_directory="./chroma_langchain_db"
                                        )

                return vector_store

def get_retriever(vector_store : Chroma, k :int = 4):
    return vector_store.as_retriever(
        search_type = 'similarity',
        search_kwargs = {"k":k}
    )
