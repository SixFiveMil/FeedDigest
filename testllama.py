import requests

def generate_response(prompt):
    url = 'http://localhost:11434/api/generate'
    data = {'model': 'llama3.2', 'prompt': prompt, 'stream': False}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        return response.json().get('response')
    else:
        raise Exception(f'Error {response.status_code}: {response.text}')

# Example usage:
prompt = "What is water made of?"
response = generate_response(prompt)
print(response)