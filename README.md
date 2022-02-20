# interactions.py and Slash Commands
## Description
This is a dirty example on how one can use the `interactions.py` library to handle Slash commands in a Discord server.

## Package Requirements
- `interactions.py` - see References
- `dotenv` 
- `json`

## Discord Bot Requirements
- Make sure that your bot has the `application.commands` scope

## Usage
- After making sure you have the above requirements in place, create a `.env` file with the format of the `.env.example` and fill in with your values
- Run `python mock.py`, which will register the commands in `commands.json` in your specified server and then it will spawn your bot.
- If you just wont to spawn the bot, run `python bot.py`


## References
- [interactions.py](https://discord-interactions.readthedocs.io/en/latest/index.html) library