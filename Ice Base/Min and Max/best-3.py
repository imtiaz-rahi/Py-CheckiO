arguments = lambda args: args if len(args) > 1 else args[0]


def min(*args, **kwargs):
    key = kwargs.get("key")
    return sorted(arguments(args), key=key)[0]


def max(*args, **kwargs):
    key = kwargs.get("key")
    return sorted(arguments(args), key=key, reverse=True)[0]
