def fibonacci(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    fib_list = [1, 1]
    counter = 0

    while len(fib_list) < n:
        fib_list.append(fib_list[counter] + fib_list[counter + 1])
        counter += 1
    return fib_list

print(fibonacci(10))
