print("Nama: Nasywa Adila Rahma")
print("Nim: 2310433022")
print("SHIFT-2")

def get_fibonacci_sequence(n):
    """
    Returns a list of the first n Fibonacci numbers.
    """
    sequence = [1, 1]
    for i in range(2, n):
        sequence.append(sequence[i-1] + sequence[i-2])
    return sequence

def main():
    """
    Gets the nth Fibonacci number and the sum of the first n Fibonacci numbers.
    """
    while True:
        try:
            n = int(input("Enter a positive integer between 3 and 199, exclusive of the range (100, 109): "))
            if n >= 3 and n <= 199 and n not in range(100, 109):
                sequence = get_fibonacci_sequence(n)
                nth_number = sequence[-1]
                sum_of_numbers = sum(sequence)
                print(f"The nth Fibonacci number (for n = {n}) is: {nth_number}")
                print(f"The sum of the first {n} Fibonacci numbers is: {sum_of_numbers}")
                break
            else:
                print("Invalid input, please try again.")
        except ValueError:
            print("Invalid input, please enter a positive integer between 3 and 199, exclusive of the range (100, 109).")

if __name__ == "__main__":
    main()