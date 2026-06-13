# 🎬 MeetMind AI
### Your Intelligent Meeting Intelligence Platform

Transform any video or audio content into actionable insights with advanced AI-powered analysis, transcription, and interactive Q&A capabilities.

---

## ✨ Features

### 🎤 **Smart Transcription**
- Convert YouTube videos and local audio files to text using OpenAI's Whisper
- Support for multiple languages including English and Hinglish
- High-accuracy speech-to-text with local processing for privacy

### 📝 **Intelligent Summarization**
- Auto-generate concise summaries of meetings and videos
- AI-powered title generation
- Extract key insights at a glance

### ✅ **Action Item Extraction**
- Automatically identify action items and tasks
- Prioritize deliverables from discussions
- Never miss an assignment again

### 🔑 **Key Insights**
- Extract critical decisions made during meetings
- Identify open questions and discussion points
- Track important takeaways

### 💬 **Interactive RAG-Powered Q&A**
- Ask natural language questions about your meeting content
- Retrieval-Augmented Generation (RAG) powered answers
- Semantic search through meeting transcripts
- Maintain conversation context for follow-ups

### 🌐 **Multi-Source Support**
- YouTube video downloads
- Local audio/video file processing
- Support for various audio formats

---

## 🚀 Quick Start

### Prerequisites
- **Python 3.10+**
- **FFmpeg** (must be installed separately)
- API key for Mistral AI

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/Koushikpali/AIVideoAssistant.git
cd AIVideoAssistant
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirement.txt
```

4. **Set up environment variables**
Create a `.env` file in the project root:
```env
MISTRAL_API_KEY=your_mistral_api_key_here
```

### Usage

**Run the pipeline:**
```bash
python main.py
```

**Enter your source:**
```
Enter YouTube URL or local file path: https://www.youtube.com/watch?v=...
Language (english/hinglish): english
```

**Output includes:**
- 📌 Auto-generated title
- 📋 Comprehensive summary
- ✅ Action items
- 🔑 Key decisions
- ❓ Open questions
- 💬 Interactive chat for Q&A

**Test the pipeline:**
```bash
python test.py
```

---

## 📦 Tech Stack

### **Core Components**
| Technology | Purpose |
|---|---|
| **Python** | Main programming language |
| **OpenAI Whisper** | Speech-to-text transcription |
| **LangChain** | LLM orchestration & RAG pipeline |
| **Mistral AI** | Large language model backend |
| **ChromaDB** | Vector database for embeddings |
| **Sentence Transformers** | Text embedding generation |

### **Media Processing**
- `yt-dlp` - YouTube video downloading
- `pydub` - Audio manipulation
- `ffmpeg-python` - Media format conversion
- `PyTorch` - Deep learning backend

### **Utilities**
- `python-dotenv` - Environment configuration
- `deep-translator` - Hindi to English translation
- `reportlab` & `fpdf2` - PDF export
- `tqdm` - Progress tracking

---

## 📁 Project Structure

```
AIVideoAssistant/
├── main.py                 # Main pipeline entry point
├── test.py                 # Testing script
├── requirement.txt         # Python dependencies
│
├── core/                   # Core processing modules
│   ├── transcribe.py      # Speech-to-text processing
│   ├── summarize.py       # Text summarization
│   ├── extractor.py       # Information extraction
│   └── rag_engine.py      # RAG Q&A pipeline
│
├── utils/                  # Utility functions
│   └── audio_processor.py  # Audio/video processing
│
└── project/               # Project-specific configs
```

---

## 🎯 How It Works

1. **Input**: YouTube URL or local audio/video file
2. **Processing**: 
   - Extract and process audio from source
   - Transcribe using Whisper with language support
   - Translate if needed (Hinglish → English)
3. **Analysis**:
   - Generate meeting title
   - Create comprehensive summary
   - Extract action items, decisions, and questions
4. **Knowledge Base**:
   - Build vector embeddings from transcript
   - Store in ChromaDB for fast retrieval
5. **Interaction**:
   - Ask natural questions about the meeting
   - Get AI-powered contextual answers
   - Interactive chat until ready to exit

---

## 🛠️ Development

### Dependencies Overview
```
Audio/Video: yt-dlp, pydub, ffmpeg-python
Speech-to-Text: openai-whisper, torch, torchaudio
Translation: deep-translator
LLM: langchain, langchain-mistralai, mistralai
RAG: chromadb, sentence-transformers, langchain-huggingface
Utilities: python-dotenv, numpy, requests, tqdm
```

### Run Tests
```bash
python test.py
```

---

## 🔐 Privacy & Security

- **Local Processing**: Whisper runs locally for privacy
- **API Keys**: Managed via `.env` file (not committed)
- **No Data Storage**: Transcripts processed in-memory unless explicitly saved
- **Optional Export**: Generate PDF reports on demand

---

## 📊 Language Support

- ✅ English
- ✅ Hinglish (Hindi/English mixed)
- 🌍 Extensible to other languages via deep-translator

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

This project is open source and available under the MIT License.

---

## 🚀 What's Next?

- [ ] Web UI with Streamlit
- [ ] Batch processing for multiple files
- [ ] Advanced sentiment analysis
- [ ] Speaker diarization support
- [ ] Custom prompt templates
- [ ] Export to multiple formats (PDF, DOCX, JSON)
- [ ] Meeting schedule integration

---

## 💡 Examples

### Example 1: YouTube Meeting Analysis
```python
from main import run_pipeline

result = run_pipeline("https://www.youtube.com/watch?v=...", language="english")
print(result['title'])
print(result['summary'])
print(result['action_items'])
```

### Example 2: Interactive Q&A
```
You: What were the main action items?
🤖 Assistant: Based on the meeting, the main action items are...

You: Who is responsible for task 1?
🤖 Assistant: According to the discussion, the person assigned to...
```

---

## 📞 Support

For issues and questions, please open an issue on [GitHub Issues](https://github.com/Koushikpali/AIVideoAssistant/issues).

---

## ⭐ Show Your Support

If you find this project helpful, please consider giving it a star! Your support helps us improve and maintain the project.

---

**Made with ❤️ by Koushik Pali**
