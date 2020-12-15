import logging

class Logger(object):
        
    def info(self, payloadLooger):
        logging.basicConfig(filename='var/log/system.log', level=logging.INFO)
        logging.info(payloadLooger)

    def error(self, payloadLooger):
        logging.basicConfig(filename='var/log/error.log', level=logging.ERROR)
        logging.error(payloadLooger)

    def warning(self, payloadLooger):
        logging.basicConfig(filename='var/log/system.log', level=logging.INFO)
        logging.warning(payloadLooger)