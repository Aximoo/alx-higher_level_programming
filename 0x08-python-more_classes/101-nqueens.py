#!/usr/bin/python3
"""
its nqueens backtracking program to print coordinates of n queens
"""


from sys import argv

if __name__ == "__main__":
    a = []
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if argv[1].isdigit() is False:
        print("N must be a number")
        exit(1)
    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # its initial the answer list
    for i in range(n):
        a.append([i, None])

    def already_exists(y):
        """it checks that a queen doesnt already exist in that y value"""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """it determines wheter it or not to reject the solution"""
        if (already_exists(y)):
            return False
        i = 0
        while(i < x):
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """it clears d answers from point of failure on"""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """its recursive backtracking a func to find the solution"""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if (x == n - 1):  # it accepts the solution
                    print(j)
                else:
                    nqueens(x + 1)  # it moves on to next x value to continue

    # it start the recursive process at x = 0
    nqueens(0)
