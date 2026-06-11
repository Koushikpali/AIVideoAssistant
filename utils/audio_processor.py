from numpy import False_
import yt_dlp
import os
from pydub import AudioSegment

DOWNLOAD_DIR='downloades'
os.makedirs(DOWNLOAD_DIR,exist_ok=True)


def download_ytaudio(url:str)->str:
                    output_path = os.path.join(DOWNLOAD_DIR, "%(title)s.%(ext)s")
                    ydl_opts = {
                        "format": "bestaudio/best",
                        "outtmpl":  output_path,
                        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "quiet": False,
                    }

                    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                        info = ydl.extract_info(url, download=True)
                        filename = ydl.prepare_filename(info).replace(".webm", ".wav").replace(".m4a", ".wav")
                    return filename
    
# url = "https://www.youtube.com/watch?v=q89NdfH-P8Q"
# download_ytaudio(url)

def convert_to_wav(input_path: str) -> str:
    """Convert any audio/video file to WAV format using pydub."""
    output_path = os.path.splitext(input_path)[0] + "_converted.wav"
    audio = AudioSegment.from_file(input_path)
    audio = audio.set_channels(1).set_frame_rate(16000) #16khz
    audio.export(output_path, format="wav")
    return output_path

def chunk_audio(wav_path:str,chunk_minutes:int=10)->list:
                    audio=AudioSegment.from_wav(wav_path)
                    chunk_size=chunk_minutes*1000*60
                    chunks=[]
                    for i, start in enumerate(range(0, len(audio), chunk_size)):
                                                                                chunk = audio[start:start + chunk_size]

                                                                                chunk_path = f"{wav_path}_chunk_{i}.wav"
                                                                                chunk.export(chunk_path, format="wav")

                                                                                chunks.append(chunk_path)

                    return chunks


def process_input(source: str) -> list:
            if source.startswith("http://") or source.startswith("https://"):
                print("Detected YouTube URL. Downloading audio...")
                wav_path = download_ytaudio(source)
            else:
                print("Detected local file. Converting to WAV...")
                wav_path = convert_to_wav(source)

            print("Chunking audio...")
            chunks = chunk_audio(wav_path)
            print(f"Audio ready — {len(chunks)} chunk(s) created.")
            return chunks