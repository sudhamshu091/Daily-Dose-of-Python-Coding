class Solution:
    def superpalindrome(self, L, R):
        l, u = int(L) ** 0.5, int(R) ** 0.5
        sq, answer = ['1', '2'], int(l <= 3 <= u)
        is_palindrome = lambda i: i == i[::-1]
        for s in sq:
            if int(s) > u:
                break
            if int(s) >= l:
                answer += is_palindrome(str(int(s)**2))
            L, odd = divmod(len(s), 2)
            if odd:
                sq += [s[:L+1] + s[-(L+1):]]
            else:
                sq += [s[:L] + d + s[-L:] for d in '012']
        return answer

print(Solution().superpalindrome('4','1000'))
