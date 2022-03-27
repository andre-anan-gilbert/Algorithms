"""An implementation of finding the modular inverse - ~O(log(a + b))."""


class ModularInverse:
    """Class that computes the modular inverse."""

    def _egcd(self, a: int, b: int) -> None:
        """Returns the gcd(a, b) and the numbers x, y such that ax + by = gcd(a, b)."""
        if not b: return a, 1, 0

        gcd, prev_x, prev_y = self._egcd(b, a % b)
        x = prev_y
        y = prev_x - prev_y * (a // b)
        return gcd, x, y

    def mod_inv(self, a: int, m: int) -> None:
        """Computes the modular inverse of a & m if it exists."""
        if m <= 0: raise ArithmeticError('Mod must be > 0.')

        a = ((a % m) + m) % m
        v = self._egcd(a, m)
        gcd = v[0]
        x = v[1]

        if gcd != 1: return
        return ((x + m) % m) % m


def main() -> None:
    modular_inverse = ModularInverse()
    print(modular_inverse.mod_inv(2, 5))  # 3 since 2 * 3 mod 5 = 1
    print(modular_inverse.mod_inv(4, 18))  # None


if __name__ == '__main__':
    main()
