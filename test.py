from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "user", "content": "Hi, how are you doing?"}
  ]
)

print(completion.choices[0].message.content)
