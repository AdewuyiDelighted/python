def factors_0f_numbers(first_num, second_num):
    factors = []
    real_length = max(first_num,second_num)
    for numb in range(1, real_length, 1):
        if first_num % numb == 0 or second_num % numb == 0:
            factors.append(numb)
    return factors


def finding_gcd(first_num, second_num):
    gcd = []
    list_factors = factors_0f_numbers(first_num,second_num)
    for factor in list_factors:
        if (first_num % factor == 0) and second_num % factor == 0:
            gcd.append(factor)
    return max(gcd)


print(finding_gcd(12,36))
