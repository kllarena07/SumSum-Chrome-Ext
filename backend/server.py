from fastapi import FastAPI
from transcribe import transcribe_video
from summarize import summarize_text

app = FastAPI()

@app.get("/summarize/{video_id}")
def main(video_id: str):
    video_transcript = transcribe_video(video_id)
    
    cohere_data = summarize_text(video_transcript)
    
    return cohere_data.summary