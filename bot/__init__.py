import logging
import logging.handlers
import time


logging.Formatter.converter = time.gmtime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.handlers.RotatingFileHandler(
    filename='nene_logs.log',
    encoding='utf-8',
    maxBytes=640 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', style="%")
handler.setFormatter(formatter)
logger.addHandler(handler)


dc_logger = logging.getLogger('discord')
dc_logger.setLevel(logging.DEBUG)
logging.getLogger('discord.http').setLevel(logging.INFO)
handler = logging.handlers.RotatingFileHandler(
    filename='nene_discord.log',
    encoding='utf-8',
    maxBytes=640 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = '%Y-%m-%d %H:%M:%S'
formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
handler.setFormatter(formatter)
dc_logger.addHandler(handler)


from .main import bot
from . import main
from . import responses
from . import events

