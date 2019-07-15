class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        
        s = ''
        a_count, b_count, tot_count = 0, 0, 0
        a_tmp_count, b_tmp_count = 0, 0
        while a_count + b_count < A + B:
            if a_tmp_count == 2:
                s += 'b'
                b_count += 1
                b_tmp_count += 1
                a_tmp_count = 0
            if b_tmp_count == 2:
                s += 'a'
                a_count += 1
                a_tmp_count +=1 
                b_tmp_count = 0
            if A - a_count >= B - b_count:
                s += 'a'
                a_count += 1
                a_tmp_count += 1
                b_tmp_count = 0
            if B - b_count > A - a_count:
                s += 'b'
                b_count += 1
                b_tmp_count +=1 
                a_tmp_count = 0
        return s