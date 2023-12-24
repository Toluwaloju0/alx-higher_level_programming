#!/usr/bin/python3
if __name__ == "__main__":
    import inspect
    import hidden_4
    names = dir(hidden_4)
    function_names = []
    for name in names:
        obj = getattr(hidden_4, name)
        if inspect.isfunction(obj):
            function_names.append(name)
        function_names.sort()
    for name in function_names:
        print(name)
