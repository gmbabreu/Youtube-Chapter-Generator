# YouTube Chapter Generator

This project provides a tool for transcribing audio from YouTube videos and generating YouTube chapters using Cohere's language models. The tool uses Whisper for transcription and adds timestamps every minute for easy segmentation.

## Features

- Download audio from YouTube videos
- Transcribe audio using Whisper
- Generate YouTube chapters using Cohere's language models
- Save transcriptions and chapters to text files

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Whisper](https://github.com/openai/whisper)
- [Cohere](https://cohere.ai)

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

3. Set up environment variables:
    Create a `.env` file in the root directory and add your Cohere API key:
    ```
    COHERE_API_KEY=your_cohere_api_key
    ```

### Usage

1. Configure the audio_path variable.
2. Run the script:
    ```sh
    python transcribe_and_segment.py
    ```

