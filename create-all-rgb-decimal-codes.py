import itertools

with open("all-rgb-decimal-codes.txt", "w") as f:
    for color in itertools.product(range(256), repeat=3):
        f.write("({:03d},{:03d},{:03d})\n".format(*color))
