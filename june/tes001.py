import openai

openai.api_key = "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"

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)