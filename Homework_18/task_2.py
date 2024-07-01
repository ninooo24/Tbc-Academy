def midpoint(x1, y1, x2, y2):
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return (mid_x, mid_y)


def main():
    print("Midpoint of (0, 0) and (4, 4):", midpoint(0, 0, 4, 4))
    print("Midpoint of (-1, 0) and (7, 3):", midpoint(-1, 0, 7, 3))
    print("Midpoint of (5, 1) and (10, 15):", midpoint(5,1 , 10, 15))


if __name__ == "__main__":
    main()
