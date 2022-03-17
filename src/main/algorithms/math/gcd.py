"""An implementation of finding the greatest common divisor of two numbers.

Time Complexity: ~O(log(a + b)).
"""


class GCD:
    """Class for finding the greatest common divisor."""

    def gcd(self, a: int, b: int) -> int:
        """Computes the greatest common divisor of a & b."""
        return abs(a) if not b else self.gcd(b, a % b)

    def main(self) -> None:
        print(self.gcd(5, 0))
        print(self.gcd(0, 5))
        print(self.gcd(-5, 0))
        print(self.gcd(0, -5))

        print(self.gcd(12, 18))
        print(self.gcd(-12, 18))
        print(self.gcd(12, -18))
        print(self.gcd(-12, -18))


if __name__ == '__main__':
    GCD().main()
