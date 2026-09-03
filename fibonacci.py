def fibonacci(count):
    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


if __name__ == "__main__":
    print(f"The first 10 Fibonacci numbers are: {fibonacci(10)}")
