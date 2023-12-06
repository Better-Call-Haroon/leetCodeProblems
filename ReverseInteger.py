class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        str_n = str(x)
        str_r = str_n[::-1].lstrip('0')
        if not str_r:
            return 0

        result = int(str_r) * sign
        int_limit = 2**31
        if result < -int_limit or result > int_limit - 1:
            return 0
        return result

        