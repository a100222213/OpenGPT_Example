import openai
# Set the API key
openai.api_key = "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"
# Use the ChatGPT model to generate text
model_engine = "text-davinci-003"
while True:
    _input = input("please enter your question : ")
    if _input == 'exit':
        break
    completion = openai.Completion.create(
        engine=model_engine, prompt=_input, max_tokens=1024, n=1, stop=None, temperature=0.7)
    message = completion.choices[0].text
    print(message)
