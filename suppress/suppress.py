from contextlib import contextmanager

# @contextmanager
# def suppress(error):
#     try:
#         yield
#     except error:
#         pass

# @contextmanager
# def suppress(*errors):
#     try:
#         yield
#     except errors:
#         pass


class ErrorInfo:
    exception = None
    traceback = None


@contextmanager
def suppress(*errors):
    info = ErrorInfo()
    try:
        yield info
    except errors as e:
        info.exception = e
        info.traceback = e.__traceback__

#  we get Bonus 3 for free with contextmanager
