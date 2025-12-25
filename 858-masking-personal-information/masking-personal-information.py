class Solution:
    def maskPII(self, s: str) -> str:
        if '@' in s :
            first,rest = s.lower().split('@')
            return f"{first[0]}*****{first[-1]}@{rest}"
        else :
            digits = "".join(c for c in s if c.isdigit())
            num_len = len(digits)
            last_f = digits[-4:]

            temp = "***-***-"+ last_f
            
            if num_len == 10 :
                return temp
            else :
                country_code = "*"*(num_len-10)
                return f"+{country_code}-{temp}"