"""An implementation of finding the least common multiple of two number - ~O(log(a + b))."""


class LCM:
    """Class for finding the least common multiple."""

    def _gcd(self, a: int, b: int) -> int:
        """Computes the greatest common divisor of a & b."""
        return abs(a) if not b else self._gcd(b, a % b)

    def lcm(self, a: int, b: int) -> int:
        """Computes the least common multiple of a & b."""
        lcm = (a // self._gcd(a, b)) * b
        return abs(lcm)


def main() -> None:
    lcm = LCM()
    print(lcm.lcm(12, 18))
    print(lcm.lcm(-12, 18))
    print(lcm.lcm(12, -18))
    print(lcm.lcm(-12, -18))


if __name__ == '__main__':
    main()
