def fibonacci(n):
    n1 = 0
    n2 = 1
    series = 0
    for i in range(n):
        print(series, end=' ');
        n1 = n2;
        n2 = series;
        series = n1 + n2;

n = int(input('Enter the number:'))
fibonacci(n)
