import time


def track_execution(func):

    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(
            *args,
            **kwargs
        )

        end = time.time()

        print(
            f"{func.__name__} took "
            f"{round(end-start,2)} sec"
        )

        return result

    return wrapper