from datetime import datetime
import logging
from modules.config import Config

# Background Colors to log messages
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger:
    def init():        
        logging.basicConfig(filename=Config.LOG_NAME, level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    def Info(message):
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.OKCYAN}{message}")
        logging.info(message)

    def Error(message):
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.FAIL}{message}")
        logging.error(message, exc_info=True)

    def Success(message):
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.OKGREEN}{message}")
        logging.info(message)

    def Warning(message):
        print(f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.WARNING}{message}")
        logging.warning(message)