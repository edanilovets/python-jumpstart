def main():
    n = 10
    factorial = fact(n)
    print('Factorial: {}! = {}'.format(n, factorial))


def fact(n):
    # 5! = 5*4*3*2*1
    if n == 1:
        return 1

    return n * fact(n-1)


if __name__ == '__main__':
    main()
