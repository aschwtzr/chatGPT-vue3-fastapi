import openai
import os
openai.api_key = os.getenv("OPENAI_API_KEY", "")
# ref https://github.com/yoheinakajima/babyagi/commit/c08e820ca8c0724696c29fecb57e79719748872e

# OPENAI_API_KEY = os.getenv("OPENAI_API_MODEL", "gpt-3.5-turbo")


def send_openai_chat_message(prompt: str, model: str = 'gpt-3.5-turbo', temperature: float = 0.5, max_tokens: int = 100):
    if not model.startswith('gpt-'):
        # Use completion API
        response = openai.Completion.create(
            engine=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )
        return response.choices[0].text.strip()
    else:
        messages = [{"role": "system", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,
            max_tokens=max_tokens,
            n=1,
            stop=None,
        )
        return response.choices[0].message.content.strip()
