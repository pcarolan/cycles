''' Analytics Engine '''

import os
import json
import logging
import logging.config
import time

logging.Formatter.converter = time.gmtime


def setup_logging(
        default_path='logging.json',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    """Setup logging configuration"""
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = json.load(f)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        path = "None"
    logger = logging.getLogger(__name__)
    logger.info('Logging initialized using config: ' + path)

setup_logging()
