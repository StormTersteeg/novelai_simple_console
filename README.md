# NovelAI Simple Console

This is a simple console application that utilizes NovelAI's API to generate text, based on user input.
It utilizes a very rudimentary context manager that simply saves the input and output, which is used to get a more consistent response from the API.

![image](https://github.com/StormTersteeg/novelai_simple_console/assets/42808385/c4c0901a-ca38-47ef-942e-0824ee8a162b)

## Description

The application works as follows:
- It loads the context and base_context.
- The user provides an input prompt which is used to generate text.
- The input is stored in the context.
- The app generates output based on the context and base_context.
- The output is stored in the context.

## Setup

### Requirements

- Python 3.x
- Install required packages using `pip install -r requirements.txt`

### Environment Variables

Create a `.env` file and define the following variables:

```dotenv
API_ENDPOINT = "https://api.novelai.net/"
API_KEY = "your-key-here"

# API SETTINGS
model = "kayra-v1"                              # kayra-v1 default model, used to generate text
temperature = 0.5                               # 0.9 default temperature, 0.0-1.0, 0.0 is deterministic, 1.0 is random
min_length = 10                                 # 10 default minimum length, used to prevent the model from returning very short outputs
max_length = 100                                # 100 default maximum length, used to prevent the model from returning very long outputs

# APP SETTINGS
max_context_size = 8192                         # 8192 maximum context size allowed by the API
context_file_name = "context.txt"               # context.txt default context file name, used to store the context between requests
use_persistent_context = True                   # True to keep the context persistent between requests, False to reset the context after each request
context_base_file_name = "context_base.txt"     # context_base.txt default context base file name, used to store the base context
```

## Usage

Run the app.py script. The console will prompt for input. Enter your prompt and press Enter. The application will generate text based on the prompt using NovelAI's API and display the output.
Change the context_base.txt to your liking, this file is used to give the beginning of your next story a starting point. Using the context_base.txt will massively improve the quality of the generated output.
If you want to completely reset the direction of your last generated story, simply erase the contents of context.txt and restart the app.

## Files
- app.py: Main application script
- .env: Environment variables configuration file
- api_handling.py: Module handling API requests
- context_handling.py: Module handling context management
- context.txt: File that is used by the app to save input/output to be used in the next session
- context_base.txt: File that contains a start narrative to help the NovelAI API generate more relevant output

## Additional Notes

- The use_persistent_context variable determines whether the context is saved between "sessions".
- max_context_size limits the size of the context stored (and sent to the API)
- The api_handling.py module handles API requests to NovelAI's service.
- The context_handling.py module manages the context data.
