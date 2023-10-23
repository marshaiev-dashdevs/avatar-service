from functools import wraps

from botocore.exceptions import NoCredentialsError

from logger import logger


def handle_s3_exceptions(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NoCredentialsError as e:
            logger.error(f"Amazon S3 credentials not available {e}")
        except Exception as e:
            logger.exception(f"Unexpected error occurred: {e}")

    return wrapper
