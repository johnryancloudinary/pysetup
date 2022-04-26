from src.log import log

logger = log.logging.getLogger(log.filepath_as_log_id(__file__))


def main():
    logger.debug("Howdy")


if __name__ == "__main__":
    main()
