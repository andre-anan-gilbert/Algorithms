"""An implementation of the extended euclidean algorithms - ~O(log(a + b))."""


class ExtendedEuclideanAlgorithm:
    """Class that performs the extended euclidean algorithm."""

    def egcd(self, a: int, b: int) -> tuple[int]:
        """Returns the gcd(a, b) and the numbers x, y such that ax + by = gcd(a, b)."""
        if not b: return a, 1, 0

        gcd, prev_x, prev_y = self.egcd(b, a % b)
        x = prev_y
        y = prev_x - prev_y * (a // b)
        return gcd, x, y


def main() -> None:
    egcd = ExtendedEuclideanAlgorithm()
    print(egcd.egcd(260, 52))  # (52, 0, 1) since 260 * 0 + 52 * 1 = gcd(260, 52)
    print(egcd.egcd(1914, 899))  # (29, 8, -17)
    print(egcd.egcd(42823, 6409))  # (17, -22, 147)


if __name__ == '__main__':
    main()
