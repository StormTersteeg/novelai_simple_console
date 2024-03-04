import requests

def generate_output(API_KEY, API_ENDPOINT, model, temperature, min_length, max_length, context):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }

    data = {
        "input": context,
        "model": model,
        "parameters": {
            "use_string": True,
            "temperature": temperature,
            "min_length": min_length,
            "max_length": max_length
        }
    }

    response = requests.post(API_ENDPOINT + "ai/generate", headers=headers, json=data)

    if response.status_code == 201:
        output = response.json()['output']
        return output
    else:
        return f'Error: {response.status_code} - {response.text}'