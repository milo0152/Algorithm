a = input()
b = input()
c = input()

arr = [a, b, c]

for i in range(3):
    x = arr[i]
    if x not in ("Fizz", "Buzz", "FizzBuzz"):
        num = int(x) + (3 - i)
        if num % 15 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)
        break