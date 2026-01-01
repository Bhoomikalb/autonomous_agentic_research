from groq import Client

# Initialize the Groq client
client = Client(api_key="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")  # replace with your key

models = client.models.list()

# Print raw output to understand structure
print(models)