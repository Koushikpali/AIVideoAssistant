
import whisper
import os
import requests
from pydub import AudioSegment
from rich import print 
from dotenv import load_dotenv
load_dotenv()
model=None

def load_model():
    global model
    if model is None:
        model=whisper.load_model(os.getenv("WHISPER_MODEL","small"))
    
    return model

def transcribe_chunk(chunk_path:str ,translate:bool=False):
      model=load_model()
      if(translate):
           task="translate"
      else:
           task="transcribe"

      result=model.transcribe(chunk_path,task=task)
      print(result)
      return result

def transcribe_all(chunks:list ,translate :bool=False)->str:
      print(f"=="*50)
      print(f'start whisper ai')
      full_transcript:str=""
      for i, chunk in enumerate(chunks):  
           print(f"transcribing chunk{i}")
           text = transcribe_chunk(chunk,translate=translate)

           print(type(text))
           text_space=text["text"]+" "
           full_transcript+=text_space
      return full_transcript


