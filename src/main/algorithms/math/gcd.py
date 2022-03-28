"""An implementation of finding the greatest common divisor of two numbers - ~O(log(a + b))."""


class GCD:
    """Class for finding the greatest common divisor."""

    def gcd(self, a: int, b: int) -> int:
        """Computes the greatest common divisor of a & b."""
        return abs(a) if not b else self.gcd(b, a % b)


def main() -> None:
    gcd = GCD()
    print(gcd.gcd(5, 0))  # 5
    print(gcd.gcd(0, 5))  # 5
    print(gcd.gcd(-5, 0))  # 5
    print(gcd.gcd(0, -5))  # 5

    print(gcd.gcd(12, 18))  # 6
    print(gcd.gcd(-12, 18))  # 6
    print(gcd.gcd(12, -18))  # 6
    print(gcd.gcd(-12, -18))  # 6


if __name__ == '__main__':
    main()
