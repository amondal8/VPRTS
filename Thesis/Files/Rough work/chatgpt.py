import openai
openai.api_key = "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"

prompt = "What is the meaning of life?"
response = openai.Completion.create(
    engine="davinci",
    prompt=prompt,
    max_tokens=50
)
print(response.choices[0].text)
