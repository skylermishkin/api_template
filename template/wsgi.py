from template.app import create_app, logger


def start():
    logger.info("WSGI is starting up.")
    app = create_app()
    logger.info(f"Application created: {app}")
    return app
