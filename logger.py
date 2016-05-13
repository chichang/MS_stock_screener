import os
import json
import logging.config


def setup_logging(
    default_path='configs/logging_configs.json',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    """Setup logging configuration

    """
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

setup_logging()


# logging.info("info.")
# logging.debug("debug.")
# logging.warning("warning.")
# logging.error("error.")
# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# except Exception, e:
#     logger.error('Failed to open file', exc_info=True)
