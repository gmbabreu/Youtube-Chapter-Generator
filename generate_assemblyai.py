import os
import time
import assemblyai as aai
import cohere
from dotenv import load_dotenv
import argparse

load_dotenv()

ASSEMBLYAI_API_KEY = os.getenv('ASSEMBLYAI_API_KEY')
COHERE_API_KEY = os.getenv('COHERE_API_KEY')


def transcribe(audio_path):
    aai.settings.api_key = ASSEMBLYAI_API_KEY
    transcriber = aai.Transcriber()

    # Configure the transcription request
    config = aai.TranscriptionConfig(language_code="pt", punctuate=True,)
    transcript = transcriber.transcribe(audio_path, config=config)

    # Poll for transcription completion
    while transcript.status not in [aai.TranscriptStatus.completed, aai.TranscriptStatus.error]:
        time.sleep(5)
        transcript = transcriber.transcript(transcript.id)

    if transcript.status == aai.TranscriptStatus.error:
        raise Exception(transcript.error)

    # Generate transcript text with timestamps
    transcript_text = ""
    current_minute = 0
    for word in transcript.words:
        start_time = word.start / 1000
        minutes = int(start_time // 60)
        if minutes > current_minute:
            current_minute = minutes
            transcript_text += f"[{minutes}:00] "
        transcript_text += word.text + " "

    return transcript_text

def segment(transcript):
    co = cohere.Client(COHERE_API_KEY)
    # Use Cohere's generate endpoint
    response = co.chat(
        message=(
            "Fornecerei um texto transcrito de um vídeo, e você deverá me fornecer  capítulos do youtube relevantes para ele. No total, deve haver cerca de 10 timestamps, cada um por volta de 5 e 15 minutos.\n"
            'Use o formato do youtube:\n'
            '"0:00 Capitulo 1\n'
            '1:30 Capitulo 2\n'
            '9:23 Capitulo 3\n'
            '21:00 Capitulo 4\n\n"'
            f"Aqui esta o texto: {transcript}\n\n"
        ),
    )
    return response.text

def generate_hashtags(transcript):
    co = cohere.Client(COHERE_API_KEY)
    # Use Cohere's generate endpoint
    response = co.chat(
        message=(
            "Fornecerei um texto transcrito de um vídeo, e você deverá me fornecer hashtags relevantes para compartilhar nas redes sociais. Gere entre 5 e 10 hashtags relacionadas ao conteúdo do vídeo.\n"
            f"Aqui está o texto: {transcript}\n\n"
        ),
    )
    return response.text

# Saves content to text file
def save_to_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate YouTube chapters and hashtags using AssemblyAI and Cohere.")
    parser.add_argument("mode", choices=["transcribe", "read_transcript"], help="Choose whether to transcribe a new audio file or read an existing transcript.")
    parser.add_argument("--audio_path", type=str, help="Path to the audio file to transcribe (required if using 'transcribe').")
    
    args = parser.parse_args()

    if args.mode == "transcribe":
        if not args.audio_path:
            print("Error: You must provide --audio_path when using 'transcribe'.")
            exit(1)

        transcript = transcribe(args.audio_path)
        save_to_file("transcript.txt", transcript)
        print("Transcript saved to transcript.txt")
    else:  # read_transcript
        if os.path.exists("transcript.txt"):
            with open("transcript.txt", "r", encoding="utf-8") as file:
                transcript = file.read()
            print("Transcript read from transcript.txt")
        else:
            print("No transcript.txt file found. Run the script with 'transcribe' mode to generate a transcript.")
            exit(1)
        
    # Generate chapters and hashtags based on the transcript
    chapters = segment(transcript)
    save_to_file("chapters.txt", chapters)
    print("Chapters saved to chapters.txt")

    hashtags = generate_hashtags(transcript)
    save_to_file("hashtags.txt", hashtags)
    print("Hashtags saved to hashtags.txt")
