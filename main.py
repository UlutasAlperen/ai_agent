import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
from call_function import call_function, available_functions
from prompts import system_prompt

MAX_STEPS = 20

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)
    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    run_agent_loop(client, messages, verbose)


def run_agent_loop(client, messages, verbose=False):
    config = types.GenerateContentConfig(
        tools=[available_functions],
        system_instruction=system_prompt
    )

    for step in range(MAX_STEPS):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=config
            )

            if verbose and response.usage_metadata:
                print(f"\n--- Step {step+1} ---")
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print("Response tokens:", response.usage_metadata.candidates_token_count)

            if not response.candidates:
                print("No candidates in response.")
                break

            for cand in response.candidates:
                if cand.content:
                    messages.append(cand.content)

            parts = response.candidates[0].content.parts
            function_calls = [p.function_call for p in parts if p.function_call]

            if not function_calls:
                text_parts = [p.text for p in parts if p.text]
                if text_parts:
                    print("\nFinal response:\n" + text_parts[0])
                else:
                    print("No text content returned.")
                break

            for fc in function_calls:
                if verbose:
                    print(f" - Calling function: {fc.name}")

                result_str = call_function(fc, verbose=verbose)

                if verbose:
                    print(f"   -> Result: {result_str}")

                function_response_content = types.Content(
                    role="user",
                    parts=[types.Part(function_response=types.FunctionResponse(
                        name=fc.name,
                        response={"result": result_str}
                    ))]
                )
                messages.append(function_response_content)

        except Exception as e:
            print(f"Error on step {step+1}: {e}")
            break
    else:
        print("Max steps reached without a final response.")


if __name__ == "__main__":
    main()

