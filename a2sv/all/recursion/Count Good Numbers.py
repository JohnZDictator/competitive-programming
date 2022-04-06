class Solution:
    def countGoodNumbers(self, n: int) -> int:
        product = pow(20, n // 2, 1000000007) * pow(5, n % 2)
        return product % 1000000007