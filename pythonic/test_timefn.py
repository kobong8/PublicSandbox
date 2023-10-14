import time
from functools import wraps


def timefn(fn):
    @wraps(fn)
    def measure_time(*args, **kwargs):
        t1 = time.time()
        result = fn(*args, **kwargs)
        t2 = time.time()
        print(f"@timefn: {fn.__name__} took {t2 - t1} seconds")
        return result
    return measure_time


# recursive function
@timefn
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@timefn
def calculate_pi(n_terms: int) -> float:
    numerator: float = 4.0
    denominator: float = 1.0
    operation: float = 1.0
    v_pi: float = 0.0
    for _ in range(n_terms):
        v_pi += operation * (numerator / denominator)
        denominator += 2.0
        operation *= -1.0
    return v_pi

if __name__ == "__main__":
    fibonacci(10)
    calculate_pi(10000)
        