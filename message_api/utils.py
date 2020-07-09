import logging

from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        data = response.data
        response.data = {}
        errors = []
        if isinstance(data, list):
            errors += data

        else:
            for field, value in data.items():
                if isinstance(value, list):
                    value = " ".join(value)
                errors.append(value)

        detail = " ".join(errors)
        response.data['detail'] = detail


def log(module, message, level='info'):
    """Set the logger to log the message."""
    logger = logging.getLogger(module)
    getattr(logger, level)(message)