import os
from dotenv import load_dotenv

# local imports
from context_handling import *
from api_handling import *

# Check the operating system for cross-platform title setting
if os.name == 'nt':  # Check if it's Windows
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW("NovelAI Simple Console")
elif os.name == 'posix':  # Check if it's Linux or Mac
    print("\033]0;NovelAI Simple Console\007", end="")

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
API_ENDPOINT = os.getenv('API_ENDPOINT')
model = os.getenv('model')
temperature = float(os.getenv('temperature', 0.7))
min_length = int(os.getenv('min_length', 10))
max_length = int(os.getenv('max_length', 150))
max_context_size = int(os.getenv('max_context_size', 8192))
use_persistent_context = os.getenv('use_persistent_context', "false").lower() == "true"
context_file = os.getenv('context_file', "context.txt")
context_base_file = os.getenv('context_base_file', "context_base.txt")

# Load context from file
if use_persistent_context:
    context = get_context(context_file)
context_base = get_context(context_base_file)

# Subtract context_base.length from max_context_size to ensure that the context is not longer than max_context_size
max_context_size -= len(context_base)

print()

while True:
    # Get user input
    input_prompt = input(" > ")
    add_to_context(input_prompt, max_context_size)
    if use_persistent_context:
        save_context(context_file)

    # Generate output
    output = ""
    while output == "":
        full_context = context_base + "\n" + context
        output = generate_output(API_KEY, API_ENDPOINT, model, temperature, min_length, max_length, full_context)
    add_to_context(output, max_context_size)
    if use_persistent_context:
        save_context(context_file)

    # Print output
    print(" >> " + output + "\n")