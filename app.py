from flask import Flask, render_template, request, jsonify
import cohere

app = Flask(__name__)  # Correct the variable name to __name__

# Initialize Cohere API
co = cohere.Client(' Replace with your actual API key')  # Replace with your actual API key

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']

    # Construct a simple mental health-related prompt
    prompt = (
        f"The following is a conversation with a mental health support chatbot. "
        f"The chatbot provides empathetic and supportive responses to mental health concerns.\n\n"
        f"User: {user_input}\n"
        f"Chatbot:"
    )

    # Use Cohere's API to generate a response
    response = co.generate(
        model='command-xlarge-nightly',  # Use an appropriate model
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
    )

    # Extract the response text
    chatbot_response = response.generations[0].text.strip()

    # Return the response as JSON
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':  # Correct the variable name to __name__
    app.run(port=5001)
