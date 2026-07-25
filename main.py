import os
import litellm
from dotenv import load_dotenv

_ = load_dotenv()
litellm.api_base = "http://localhost:4000"
litellm.api_key = os.getenv("VIRTUAL_KEY")

messages=[{"role": "user", "content": "Hi!"}]
response = litellm.completion(
    messages=messages,
    model="groq/openai/gpt-oss-120b",
    custom_llm_provider="openai"
)
print(response.choices[0].message.content)