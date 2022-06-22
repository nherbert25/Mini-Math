import random


def addition_problem() -> int:

    a = random.randint(0, 10)
    b = random.randint(0, 10)

    answer = a + b

    print(f"{a}+{b} = ?")

    return answer


def subtraction_problem() -> int:
    a = random.randint(1, 100)
    b = random.randint(0, a)

    answer = a - b

    print(f"{a}-{b} = ?")

    return answer


def multiplication_problem() -> int:
    a = random.randint(0, 10)
    b = random.randint(0, 10)

    answer = a * b

    print(f"{a}*{b} = ?")

    return answer


def division_problem() -> int:
    a = random.randint(1, 10)
    answer = random.randint(0, 10)

    b = a*answer

    print(f"{b}/{a} = ?")

    return answer
