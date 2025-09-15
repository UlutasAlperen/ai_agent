import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    verbose_flag = False

    if api_key is None:
        raise ValueError("GEMINI_API_KEY environment variable not set")
    client = genai.Client(api_key=api_key)
    
    if len(sys.argv) < 2:
        print("Prompt not provided")
        sys.exit(1)

    if "--verbose" in sys.argv:
        verbose_flag = True



    argument = ""
    for i in range(1,len(sys.argv)):
        if sys.argv[i]=="--verbose":
            continue
        argument += sys.argv[i] + " "

    messages = [
        types.Content(
            role="user",
            parts=[
                types.Part(
                    text=argument
                )
            ]
        ),
    ]
    generate_content(client,messages,verbose_flag)

def generate_content(client, messages,verbose_flag=False):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
    )
    if verbose_flag:
        print(f"User prompt: {messages}")
        print(f"Prompt tokens:{response.usage_metadata.prompt_token_count}")
        print(f"Response tokens:{response.usage_metadata.candidates_token_count}")

    print("Response:")
    print(response.text)



if __name__ == "__main__":
    main()
