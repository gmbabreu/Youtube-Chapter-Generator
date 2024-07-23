# YouTube Chapter Generator

This project provides a tool for transcribing audio from YouTube videos and generating YouTube chapters using Cohere's language models. The tool uses Whisper for transcription and adds timestamps every minute for easy segmentation.

## Features

- Download audio from YouTube videos
- Transcribe audio using Whisper
- Generate YouTube chapters using Cohere's language models
- Save transcriptions and chapters to text files

## Getting Started

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/YouTube-Chapter-Generator.git
    cd YouTube-Chapter-Generator
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Install FFmpeg:
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
    Create a `.env` file in the root directory and add your Cohere API key:
    ```
    COHERE_API_KEY=your_cohere_api_key
    ```


### Usage

1. Configure the audio_path variable to the path for your audio file.
2. Run the script:
    ```sh
    python transcribe_and_segment.py
    ```

