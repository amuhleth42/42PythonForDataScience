def print_mean(args):
    if (len(args) == 0):
        print("ERROR")
        return
    res = sum(args) / len(args)

    print(f"mean : {res}")

def get_median(args):
    sorted_args = sorted(args)
    n = len(args)
    if n % 2 == 0:
        mid1 = sorted_args[n // 2 - 1]
        mid2 = sorted_args[n // 2]
        res = (mid1 + mid2) / 2
    else:
        res = sorted_args[n // 2]
    return res
    

def print_median(args):
    if (len(args) == 0):
        print("ERROR")
        return
    res = get_median(args)

    print(f"median : {res}")


def print_quartile(args):
    if (len(args) == 0):
        print("ERROR")
        return
    sorted_args = sorted(args)
    half = len(args) // 2
    n = len(args)
    if n % 2 == 0:
        list1 = sorted_args[:half]
        list3 = sorted_args[-half:]
    else:
        list1 = sorted_args[:half + 1]
        list3 = sorted_args[-half - 1:]
    q1 = get_median(list1)
    q3 = get_median(list3)

    print(f"quartile : [{float(q1)}, {float(q3)}]")


def print_std(args):
    if (len(args) == 0):
        print("ERROR")
        return
    m = sum(args) / len(args)
    squared_diff = [(x - m) ** 2 for x in args]
    variance = sum(squared_diff) / len(args)
    res = variance ** 0.5

    print(f"std : {res}")


def print_var(args):
    if (len(args) == 0):
        print("ERROR")
        return
    m = sum(args) / len(args)
    squared_diff = [(x - m) ** 2 for x in args]
    variance = sum(squared_diff) / len(args)

    print(f"var : {variance}")


def ft_statistics(*args: any, **kwargs: any) -> None:
    for key, value in kwargs.items():
        if value == 'mean':
            print_mean(args)
        if value == 'median':
            print_median(args)
        if value == 'quartile':
            print_quartile(args)
        if value == 'std':
            print_std(args)
        if value == 'var':
            print_var(args)
