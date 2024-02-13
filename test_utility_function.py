
from utility_function import is_prime, factorial


def test_is_prime_true():
    assert is_prime(5),"Expected 5 to be prime"

def test_factorial():
    assert factorial(5) == 125, "Expected factorial of 5 to be 120"

