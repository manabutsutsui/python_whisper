from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

# 音声ファイルを取得
audio_file = open("sample.mp3", "rb")
transcript = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file, 
  response_format="text"
)

# ChatGPRに要約してもらう
summary = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": f"以下の文章を３行の箇条書きにして要約してください。:\n{transcript}",
        }
    ],
    model="gpt-3.5-turbo",
  )

print(summary.choices[0].message.content)