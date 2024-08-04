# Simple Gemini Python Chat Bot #
## Description ##
A brief description of what your project does and its main features.

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
/process_message
This endpoint handles HTTP POST requests to process a message. It expects a JSON payload with a message field.

/prompts
This endpoint returns a JSON response containing a list of available prompts.

## License ##
This project is licensed under the MIT License.
