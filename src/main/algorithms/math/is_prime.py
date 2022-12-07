"""Tests whether a number is a prime number - O(sqrt(n))"""
import math


class IsPrime:
    """Class for finding prime numbers."""

    def is_prime(self, n: int) -> bool:
        """Determines whether a number is a prime number."""
        if n < 2: return False
        if n in (2, 3): return True
        if n % 2 == 0 or n % 3 == 0: return False

        limit = int(math.sqrt(n))
        for i in range(5, limit, 6):
            if n % i == 0 or n % (i + 2) == 0:
                return False

        return True


def main() -> None:
    is_prime = IsPrime()
    print(is_prime.is_prime(5))
    print(is_prime.is_prime(31))
    print(is_prime.is_prime(1433))
    print(is_prime.is_prime(31393))


if __name__ == '__main__':
    main()
