import os
import argparse
from dotenv import load_dotenv
from google.genai import types
from google.genai import Client
from config import system_prompt
from functions.call_functions import available_functions
from functions.call_functions import call_function

def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("Gemini API key is not present in configuration")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()
    messages = [types.Content(role="user", parts=[types.Part(text=args.user_prompt)])]

    model = 'gemini-2.5-flash'
    client = Client(api_key=api_key)
    response = client.models.generate_content(
        model=model, 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
        )
    if response.usage_metadata is None:
        raise RuntimeError("Something went wrong, please check your request")

    function_results = []

    if len(response.function_calls) > 0:
        for call in response.function_calls:
            #print(f"Calling function: {call.name}({call.args})")
            function_call_result = call_function(call)
            if not function_call_result.parts:
                raise Exception(f"No parts in function result -  {call.name} ")
            if function_call_result.parts[0].function_response == None:
                raise Exception(f"No response from function call - {call.name}")
            if function_call_result.parts[0].function_response.response == None:
                raise Exception(f"No response from function call - {call.name}")
            function_results.append(function_call_result.parts[0])

    if args.verbose:
        print("User prompt: ", args.user_prompt)
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(f"-> {function_call_result.parts[0].function_response.response}")
    print("Response:")
    print(response.text)
            


if __name__ == "__main__":
    main()
