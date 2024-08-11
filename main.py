def count_zeros():
        N = int(input("введи число n "))
        numbers = list(map(int, input("введите n целых чисел ").split()))
        count = sum(1 for num in numbers if num == 0)
        print("кол-во нулей ", count)
count_zeros()

def count_divisors():
        X = int(input("введи натруальное число х "))
        divisors_count = 0
        for i in range(1, int(X**0.5) + 1):
            if X % i == 0:
                divisors_count += 1 
                if i != X // i:
                    divisors_count += 1
        print("кол-во натуральных делителей", divisors_count)
count_divisors()

def print_even_numbers():
        A, B = map(int, input("введи два целых числа A и B (A ≤ B) ").split())
        evens = [str(num) for num in range(A, B + 1) if num % 2 == 0]
        print("четные числа на отрезке:", " ".join(evens))
print_even_numbers()
