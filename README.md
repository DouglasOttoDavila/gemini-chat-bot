# Simple Gemini Python Chat Bot #
## Description ##
The Gemini Python Chat Bot is a web-based chatbot application that utilizes the GEMINI language model to generate human-like responses to user queries.

## Features ##
- **Chat Interface**: The chatbot is accessible through a web-based interface, allowing users to interact with it by typing their questions.
- **GEMINI Language Mode**l: The chatbot leverages the GEMINI language model, which is a state-of-the-art large language model trained on a diverse range of internet text. It generates responses based on the user's input.
- **Initial Prompts**: The chatbot is seeded with initial prompts that provide a starting point for the conversation. These prompts are stored in the INITIAL_PROMPT dictionary.
- **Safety Settings**: The chatbot has safety settings that determine the level of filtering applied to its responses. The safety settings are defined in the prompt_safety dictionary.
- **API Endpoints**: The chatbot exposes two API endpoints: /process_message for processing user messages and /prompts for retrieving a list of available prompts.
- **Configuration**: The application can be configured by adding or modifying prompts in the config.py file.
Dependencies: The project relies on the Flask framework, the iPython library, the protobuf library, and the python-dotenv library.

## Installation ##
- Clone the repository: `git clone https://github.com/DouglasOttoDavila/gemini-chat-bot.git`
- (Optional) [Configure your virtual python environment (venv)](https://code.visualstudio.com/docs/python/environments) and activate it.
- Install the dependencies: `pip install -r requirements.txt`
- Set up the environment variables: create a `.env` file in the root directory and set the `GEMINI_API_KEY` variable to your GEMINI API key.

### Additional Steps ###
You can configure this application for your own needs by simply following these steps:
- Go to `config.py` file, located in the project's root
- Replace or include a new entry under `INITIAL_PROMPT` with your customized context prompt.
- Include the recently created entry under `prompt_safety` object along with it's respective safety rating (_safe or unsafe_).

## Usage ##
- Run the application: `python app.py`
- Open a web browser and navigate to `http://localhost:5000`
- Start chatting with the bot!

## API Endpoints ##
- `/process_message`: This endpoint handles HTTP POST requests to process a message. It expects a JSON payload with a message field.
- `/prompts`: This endpoint returns a JSON response containing a list of available prompts.

## License ##
This project is licensed under the MIT License.
