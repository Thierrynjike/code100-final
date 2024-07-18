def test_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"la méthode {func.__name__} a utilisé mon wrapper")
        result = func(*args, **kwargs)

        return result

    return wrapper


@test_decorator
def calcul(n):
    fact = 1

    for i in range(1, n + 1):
        fact *= i

    return fact


print(calcul(5))
