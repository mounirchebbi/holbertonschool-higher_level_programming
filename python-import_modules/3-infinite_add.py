#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    """infinite sum"""

    import sys
    sum = 0
    if len(sys.argv) < 2:
        print("0")
    else:
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print(sum)
