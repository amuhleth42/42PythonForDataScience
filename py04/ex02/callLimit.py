def callLimit(n: int):
    count = 0
    def decorator(func):
        def wrapper():
            nonlocal count
            count += 1
            if count > n:
                print(f"Error: {func} called too many times")
            else:
                return func()
        return wrapper
    return decorator
