from flask import Flask, request, jsonify
import requests
import json

app = Flask(__name__)

@app.route('/api/get_chat_response', methods=['POST'])
def chat():
    character = request.json.get('character')
    questions = request.json.get('questions')

    # Call the existing code or functions to process the inputs and generate the response
    response = process_questions(character, questions)

    return jsonify({'response': response})

def process_questions(character, questions):
    # Add your existing code here to handle the conversation logic and generate the response
    # You can use the character and questions inputs to interact with the companion

    # API endpoint URL
    url = 'http://localhost:5000/api/get_chat_responset'

    # Request payload
    payload = {
        'character': character,
        'questions': questions
    }

    # Send POST request
    response = requests.post(url, json=payload)

    # Check response status code
    if response.status_code == 200:
        # Parse response JSON
        data = response.json()
        # Extract the response from the JSON
        api_response = data['response']
        # Return the response
        return api_response
    else:
        return 'Error: ' + str(response.status_code)
    

if __name__ == '__main__':
    app.run()


