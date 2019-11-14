# fibonacci.py

def fib():
    fibs = []
    b=1
    c = 1
    a = 0


    for i in range(1,9):
        c = a + b
        a = b
        b = c
        fibs = fibs + c

    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()