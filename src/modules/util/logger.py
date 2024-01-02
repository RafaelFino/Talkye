from datetime import datetime
import logging

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
        logging.basicConfig(filename='talkye.log', level=logging.DEBUG) 

    def Info(message):
        formatted = f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.OKCYAN}{message}"
        logging.info(formatted) 

    def Error(message):
        formatted = f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.FAIL}{message}"
        logging.error(formatted)

    def Success(message):
        formatted = f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.OKGREEN}{message}"
        logging.info(formatted)

    def Warning(message):
        formatted = f"{bcolors.BOLD}{bcolors.OKBLUE}[{datetime.now()}] {bcolors.WARNING}{message}"
        logging.warning(formatted)