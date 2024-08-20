# YouTube Content Generator (pt-br)

This project provides a tool for transcribing audio from YouTube videos and generating YouTube chapters and relevant hashtags using Cohere's language models in Portuguese. The tool supports transcription using either Whisper or AssemblyAI and adds timestamps every minute for easy segmentation.


## Features

- Download audio from YouTube videos
- Transcribe audio using Whisper or AssemblyAI
- Generate YouTube chapters using Cohere's language models
- Generate relevant social media hashtags using Cohere's language models
- Save transcriptions and chapters to text files

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Whisper](https://github.com/openai/whisper) (optional, for Whisper transcription)
- [AssemblyAI](https://www.assemblyai.com) (optional, for AssemblyAI transcription)
- [Cohere](https://cohere.ai)
- [FFmpeg](https://ffmpeg.org) (required for Whisper)

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/gmbabreu/YouTube-Chapter-Generator.git
    cd YouTube-Chapter-Generator
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install FFmpeg (for Whisper transcription):
    - **Windows**: Download and install FFmpeg from [FFmpeg Windows](https://ffmpeg.org/download.html#build-windows).
    - **Mac**: Use Homebrew to install FFmpeg:
      ```sh
      brew install ffmpeg
      ```
    - **Linux**: Use your package manager to install FFmpeg. For example, on Ubuntu:
      ```sh
      sudo apt update
      sudo apt install ffmpeg
      ```

4. Set up environment variables:
    Create a `.env` file in the root directory and add your API keys:
    ```
    COHERE_API_KEY=your_cohere_api_key
    ASSEMBLYAI_API_KEY=your_assemblyai_api_key
    ```

### Usage
The script supports two primary modes:
1. **Transcribe a new audio file and generate chapters/hashtags**
   ```sh
    python generate_whisper.py transcribe --audio_path="path_to_audio_file.mp3"
    ```
   - Choose your transcribing method and run the corresponding python file. To use AssemblyAI you must gain access to their API keys
   - The transcript will be saved as ```transcript.txt```, and chapters and hashtags will be generated based on it.
2. **Read an existing transcript and generate chapters/hashtags**
   ```sh
    python generate_whisper.py read_transcript
    ```
   - This mode reads the existing transcript.txt in the directory. No transcription is performed, so the AssemblyAI API key is not needed.



### Output

The script will generate the following files in the root directory:
- transcript.txt: The transcript of the video.
- chapters.txt: YouTube chapters generated from the transcript.
- hashtags.txt: Relevant social media hashtags based on the video content.

