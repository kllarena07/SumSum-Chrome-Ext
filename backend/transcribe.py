from youtube_transcript_api import YouTubeTranscriptApi

def transcribe_video(video_id: str):
  print(f'Attempting to transcribe: https://www.youtube.com/watch?v={video_id}')

  data = YouTubeTranscriptApi.get_transcript(video_id)
  
  transcript = ""
  for blob in data:
    transcript += f'\n{blob["text"]}'

  return transcript