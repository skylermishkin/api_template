from app_template.app import create_app, logger


def start(env, start_response):
    logger.info("WSGI is starting up.")
    app = create_app()
    logger.info("Application created.")
    return app
