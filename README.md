# NovelAI Simple Console

This is a simple console application that utilizes NovelAI's API to generate text based on user input.
It utilizes a very rudimentary context manager that simply saves the input and output, which is used to get a more consistent response from the API.

## Setup

### Requirements

- Python 3.x
- Install required packages using `pip install -r requirements.txt`

### Environment Variables

Create a `.env` file and define the following variables:

```dotenv
# API SETTINGS
API_ENDPOINT = "https://api.novelai.net/"
API_KEY = "your-key-here"

model = "kayra-v1"
temperature = 0.9 
min_length = 10   
max_length = 100  

# APP SETTINGS
max_context_size = 8192               
context_file_name = "context.txt"     
use_persistent_context = True
```

### Usage

Run the app.py script. The console will prompt for input. Enter your prompt and press Enter. The application will generate text based on the prompt using NovelAI's API and display the output.

### Files
- app.py: Main application script
- .env: Environment variables configuration file
- api_handling.py: Module handling API requests
- context_handling.py: Module handling context management

### Description

The application works as follows:
- It loads environment variables from the .env file.
- The user provides input prompts which are used to generate text.
- The context (user prompts) is stored and can be optionally persisted between requests.
- The generated text is displayed to the user.

### Additional Notes
- The use_persistent_context variable determines whether the context is saved between "sessions".
- max_context_size limits the size of the context stored (and sent to the API)
- The api_handling.py module handles API requests to NovelAI's service.
- The context_handling.py module manages the context data.
