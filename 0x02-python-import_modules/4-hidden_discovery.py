#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    all_attributes = dir(hidden_4)
    n = [attr for attr in all_attributes if callable(getattr(hidden_4, attr))]
    sorted_function_names = sorted(n)
    for n in sorted_function_names:
        if n[0] == '_':
            continue
        print(n)
