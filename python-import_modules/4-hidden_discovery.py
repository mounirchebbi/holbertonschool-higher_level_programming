#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    # Get all names defined in the module
    names = dir(hidden_4)

    # Filter and sort names
    filtered_names = sorted(name for name in names if not name.startswith('__'))

    # Print each name
    for name in filtered_names:
        print(name)
