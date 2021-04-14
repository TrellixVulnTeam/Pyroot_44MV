import operator as op
from functools import reduce

def diverseTeam(m , w):

    import operator as op
    from functools import reduce

    def ncr_m_1(m):
        numer1 = reduce(op.mul, range(m, m-1, -1),1)  # r = 1
        denom1 = reduce(op.mul, range(1, 2),1)
        return numer1 / denom1

    def ncr_m_2(m):
        numer2 = reduce(op.mul, range(m, m-2, -1),1) # r= 2
        denom2 = reduce(op.mul, range(1, 3), 1)
        return numer2 / denom2

    def ncr_w_1(w):
        numer3 = reduce(op.mul, range(w, w - 2, -1), 1) # r =2
        denom3 = reduce(op.mul, range(1, 3), 1)
        return numer3 / denom3

    def ncr_w_2(w):
        numer4 = reduce(op.mul, range(w, w - 1, -1), 1)  # r =1
        denom4 = reduce(op.mul, range(1, 2), 1)
        return numer4 / denom4

    final_combination = ncr_m_1(m) + ncr_m_2(m) + ncr_w_1(w) + ncr_w_2(w);
    return final_combination;



print(diverseTeam(2,1))


