def ft_filter(f, iterable):
    """
    custom version of the filter function, using list comprehension
    """
    if f:
        return (x for x in iterable if f(x))
    return (x for x in iterable if x)
