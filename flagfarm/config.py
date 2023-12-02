# Must be inserted info
BOARD_URL = ""
ROUND_TIMER = -1
TEAM_TOKEN = ""

# Can be untouched
LOG_FILENAME = ""
LOG_LEVEL = 2

# Generated
FLAG_POST_URL = f"http://{BOARD_URL}/flags"

# Constant
FLAG_LENGTH = 32
FLAG_REGEX = r'[A-Z0-9]{31}='

# Check variables to be valid
assert BOARD_URL != "", "Please specify BOARD_URL in config.py"
assert ROUND_TIMER > 0, "Please specify ROUND_TIMER in config.py"
assert TEAM_TOKEN != "", "Please specify TEAM_TOKEN in config.py"