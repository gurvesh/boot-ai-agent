import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv
import prompts
from schema import available_functions
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python import run_python_file

WORKING_DIR = "./calculator"
func_dict = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "write_file": write_file,
    "run_python_file": run_python_file
}

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = [arg for arg in sys.argv[1:] if not arg.startswith("--")]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    for _ in range(20):
        final_response = generate_content(client, messages, verbose)
        if final_response:
            print(final_response)
            break

def generate_content(client, messages, verbose):
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=prompts.system_prompt)
    )
    
    if response.candidates:
        for candidate in response.candidates:
            messages.append(candidate.content)
    
    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    # print("Response:")

    function_responses = []
    
    if not response.function_calls:
        return response.text
    
    for func_call in response.function_calls:
        func_call_result = call_function(func_call, verbose)
        try:
            if verbose:
                print(f"-> {func_call_result.parts[0].function_response.response}")
            function_responses.append(func_call_result.parts[0])
        except Exception as e:
            raise Exception("An unrecoverable error occurred.")
    if not function_responses:
        raise Exception("no function responses generated, exiting.")
    
    # We don't have a final response yet, but we add the messages
    messages.append(types.Content(role="tool", parts=function_responses))
    

def call_function(func_call, verbose=False):
    if verbose:
        print(f"Calling function: {func_call.name}({func_call.args})")
    else:
        print(f"Calling function: {func_call.name}")
    
    if func_call.name not in func_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=func_call.name,
                    response={"error": f"Unknown function: {func_call.name}"},
                )
            ],
        )
    
    func_call.args["working_directory"] = WORKING_DIR
    function_result = func_dict[func_call.name](**func_call.args)
    
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=func_call.name,
                response={"result": function_result},
            )
        ],
    )


if __name__ == "__main__":
    main()



