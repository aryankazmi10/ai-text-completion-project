
import os
from openai import OpenAI

# Create a client instance
client = OpenAI(api_key="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")

def generate_text(prompt, temperature=0.7, max_tokens=150):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            temperature=temperature,
            max_tokens=max_tokens
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Error: {str(e)}"

def main():
    print("Welcome to the AI Text Completion App! Type 'exit' to quit.")
    while True:
        prompt = input("\nEnter your prompt: ").strip()
        if prompt.lower() == "exit":
            break
        if not prompt:
            print("Please enter a non-empty prompt.")
            continue

        temp_input = input("Enter temperature (default 0.7): ").strip()
        if temp_input == "":
            temp = 0.7
        else:
            temp = float(temp_input)

        tokens_input = input("Enter max tokens (default 150): ").strip()
        if tokens_input == "":
            tokens = 150
        else:
            tokens = int(tokens_input)

        result = generate_text(prompt, temperature=temp, max_tokens=tokens)
        print("\nAI Response:\n", result)

if __name__ == "__main__":
    main()
