import functools

# def record_calls(func):
#
#     def wrapped(*args, **kwargs):
#         wrapped.call_count += 1
#         return func(*args, **kwargs)
#
#     wrapped.call_count = 0
#     return wrapped

# def record_calls(func):
#
#     @functools.wraps(func)
#     def wrapped(*args, **kwargs):
#         wrapped.call_count += 1
#         return func(*args, **kwargs)
#
#     wrapped.call_count = 0
#     return wrapped

# class Call:
#     def __init__(self, args, kwargs):
#         self.args, self.kwargs = args, kwargs
#
#
# def record_calls(func):
#
#     @functools.wraps(func)
#     def wrapped(*args, **kwargs):
#         wrapped.call_count += 1
#         wrapped.calls.append(Call(args, kwargs))
#         return func(*args, **kwargs)
#
#     wrapped.call_count = 0
#     wrapped.calls = []
#     return wrapped

NO_RETURN = 'NULL'


class Call:
    def __init__(self, args, kwargs, return_value, exception):
        self.args, self.kwargs, self.return_value, self.exception = args, kwargs, return_value, exception


def record_calls(func):

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        wrapped.call_count += 1
        try:
            return_value = func(*args, **kwargs)
            wrapped.calls.append(Call(args, kwargs, return_value, None))
        except Exception as e:
            return_value = NO_RETURN
            wrapped.calls.append(Call(args, kwargs, return_value, e))
            raise
        return return_value

    wrapped.call_count = 0
    wrapped.calls = []
    return wrapped
