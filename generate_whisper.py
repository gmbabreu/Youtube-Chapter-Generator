import whisper
import cohere
import os
from dotenv import load_dotenv
import argparse

load_dotenv()
API_KEY = os.getenv('COHERE_API_KEY')

def transcribe(audio_path):
    # Load Whisper model
    model = whisper.load_model("base")
    # Transcribe the audio file specifying the language as Portuguese
    result = model.transcribe(audio_path, language='pt') 
    
    segments = result['segments']
    transcript = ""
    current_minute = 0
    # Iterate through each segment of the transcription
    for segment in segments:
        start_time = segment['start']
        minutes = int(start_time // 60)
        # Add timestamp at the beginning of every new minute
        if minutes > current_minute:
            current_minute = minutes
            transcript += f"[{minutes}:00] "
        transcript += segment['text'] + " "
    return transcript

def segment(transcript):
    co = cohere.Client(API_KEY)
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
    parser = argparse.ArgumentParser(description="Generate YouTube chapters and hashtags using Whisper and Cohere.")
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

