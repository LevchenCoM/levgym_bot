import os

from dotenv import load_dotenv
from training_programs import program_1

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')

ALLOWED_IDS = os.getenv('ALLOWED_IDS').split(',')

AVAILIBLE_PROGRAMS = (
   program_1.TRAINING
)

DB_CONNECTOR = os.getenv('DB_CONNECTOR')
