
import google.generativeai as genai
import textwrap
import os
from flask import Flask, request, jsonify
from IPython.display import Markdown
from flask import render_template
from dotenv import load_dotenv
from static.data import get_safety_settings
from config import INITIAL_PROMPT
load_dotenv()
app = Flask(__name__)


# Load the GEMINI API key from the environment variables
# The .env file is loaded using the load_dotenv() function from the dotenv module
# The GEMINI API key is stored in the environment variable GEMINI_API_KEY
# This key is then assigned to the GENAI_API_KEY variable
GENAI_API_KEY = os.environ['GEMINI_API_KEY']


# Configure GEMINI API
# This API is used to connect our application to the GEMINI model
# GEMINI is a state-of-the-art large language model that is trained on a diverse range of internet text
# It is capable of generating human-like text given a prompt
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')
genai.configure(api_key=GENAI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')


@app.route('/', methods=['GET'])
def render():
  """
  Renders the 'chat.html' template with the initial prompts.

  Returns:
    The rendered 'chat.html' template with the initial prompts.
  """
  return render_template('chat.html', initial_prompts=INITIAL_PROMPT)


@app.route('/process_message', methods=['POST'])
def process_message_route():
  """
  Route for processing a message.

  This route handles HTTP POST requests to '/process_message'. It expects a JSON payload with a 'message' field.

  Parameters:
    None

  Returns:
    A JSON response containing a 'response' field with the processed message.
  """
  message = request.json.get('message')
  response = process_message(message)
  return jsonify({'response': response})


def to_markdown(text):
  """
  Converts a given text to markdown format.

  Args:
      text (str): The text to be converted to markdown.

  Returns:
      Markdown: The converted markdown text.
  """
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


def process_message(message):
  """
  Processes a message and returns the response.

  This function takes a message as input and processes it using the selected prompt. It first retrieves the selected prompt and name from the request JSON payload. It then prints the selected prompt and name for debugging purposes. If the selected prompt is not in the INITIAL_PROMPT dictionary, it returns an "Invalid prompt key" error. 

  The function then retrieves the prompt text from the INITIAL_PROMPT dictionary based on the selected prompt. If the 'chat_session' is not present in the globals(), it starts a new chat session with an empty history and sends the prompt text to the chat session. Otherwise, it uses the existing chat session. 

  The function sends the message with the name appended to it to the chat session and retrieves the response. It then updates the 'chat_session' in the globals() with the updated chat session. 

  Finally, it returns the response text.

  Parameters:
  - message (str): The message to be processed.

  Returns:
  - str: The response text.
  """
  selected_prompt = request.json.get('prompt')
  name = request.json.get('name')
  print(f"Selected Prompt: {selected_prompt}")  
  print(f"Name: {name}")  
  if selected_prompt not in INITIAL_PROMPT:
    return "Invalid prompt key"  # Handle invalid prompt key
  prompt_text = INITIAL_PROMPT[selected_prompt]
  if 'chat_session' not in globals():
    chat = model.start_chat(history=[])
    chat.send_message(
      prompt_text,
      safety_settings = get_safety_settings(selected_prompt)
    )
  else:
    chat = globals()['chat_session']
  response = chat.send_message(
    f'{name} said:\n' + message,
    safety_settings = get_safety_settings(selected_prompt)
  )
  globals()['chat_session'] = chat
  return response.text


def process_message_with_gemini(message):
    """
    Processes a message using the Gemini AI model and returns the response.

    Args:
        message (str): The message to be processed.

    Returns:
        str: The response text from the Gemini AI model.

    This function creates a new chat session using the `model.start_chat()` method with an empty history. It then sends the message to the chat session using the `chat.send_message()` method and converts the response to markdown format using the `to_markdown()` function. The response text is printed to the console and returned as the final result.
    """
    chat = model.start_chat(history=[])
    response = to_markdown(chat.send_message(message))
    print(response.text)
    return response.text


if __name__ == '__main__':
    app.run(debug=True)