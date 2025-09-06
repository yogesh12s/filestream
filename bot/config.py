class Telegram:
    # Directly hardcode values here
    API_ID = 26421691
    API_HASH = "a2ddc72ad8e40cd501790d36e7605d66"
    OWNER_ID = 1837916554
    ALLOWED_USER_IDS = [1837916554]   # list form
    BOT_USERNAME = "Stream_134vbot"
    BOT_TOKEN = "7829016089:AAG4jcffLZYLyKs7VCeP6Fe_SvCQspieAuc"

    # ✅ If public channel, you can use username
    CHANNEL_ID = "@chadstreamz"  

    # Or if private channel, use numeric ID like this:
    #CHANNEL_ID = -1837916554

    SECRET_CODE_LENGTH = 24


class Server:
    BASE_URL = "https://yogesh12d.pythonanywhere.com"
    BIND_ADDRESS = "127.0.0.1"
    PORT = 8000


# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'hydrogram': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
