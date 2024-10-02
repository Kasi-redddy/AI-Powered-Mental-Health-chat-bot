# AI-Powered-Mental-Health-chat-bot
AI-Powered Mental Health Chatbot using Cohere API

This project is an AI-powered mental health chatbot that uses the Cohere API to provide empathetic and supportive responses to mental health-related concerns. It is built using Flask (a Python web framework) and utilizes Cohere's natural language processing capabilities.
Features
- Chatbot provides empathetic and human-like responses to mental health queries.
- Integrates Cohere’s NLP model to generate dynamic responses.
- Supports text input and responds via both text and voice.
- Users can stop the chatbot's voice reply with a "Stop" button.
- Easy-to-use web interface with voice command support.

 Demo
You can test the chatbot locally by following the instructions below.

Getting Started

Prerequisites
Before you begin, ensure you have the following installed on your system:
- Python 3.x
- Pip (Python package manager)

Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/mental-health-chatbot.git
   cd mental-health-chatbot
   ```

2. **Install dependencies:**
   In the project directory, install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```
 Setting Up Your Own Cohere API Key

To use this project, you'll need to set up your own Cohere API key. Follow the steps below:

1. **Create a Cohere account:**
   - Visit [Cohere's website](https://cohere.com/) and sign up for an account.

2. **Get your API key:**
   - Once logged in, go to your [Cohere Dashboard](https://dashboard.cohere.ai/).
   - In the dashboard, click on **API Keys** and copy the API key.

3. **Set your API key in the project:**
   - Open the `app.py` file in your text editor.
   - Find the line with the `cohere.Client()` call:
     ```python
     co = cohere.Client('your-api-key-here')
     ```
   - Replace `'your-api-key-here'` with your actual API key from Cohere.

Running the Application

1. **Start the Flask server:**
   After setting up your API key, start the Flask application:
   ```bash
   python app.py
   ```

2. **Access the chatbot:**
   Open your browser and navigate to:
   ```
   http://127.0.0.1:5001/
   ```

3. **Interact with the chatbot:**
   - Type your message in the input box and click "Send."
   - Alternatively, you can use the "Voice" button to input messages using your voice.
   - The chatbot will respond with text and voice, and you can stop the voice response by clicking the "Stop" button.

How It Works

- The chatbot receives input from the user via text or voice.
- The input is sent to the Cohere API, which generates a mental health-related response using NLP.
- The generated response is displayed as text, and a voice response is also generated using the SpeechSynthesis API in the browser.
  
Key Files

- `app.py`: The Flask server and main logic to interact with the Cohere API.
- `index.html`: The front-end interface for interacting with the chatbot.
- `static/`: Contains the icons and background image used in the chatbot interface.

 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

 Acknowledgments

 [Cohere AI](https://cohere.ai/) for providing powerful NLP models.
