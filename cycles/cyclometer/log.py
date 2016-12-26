import logging

logger = logging.getLogger(__name__)

def beat():
    logger.info("[BEAT] .")

def info(message):
    logger.info(message)

def error(message):
    logger.error(message)
