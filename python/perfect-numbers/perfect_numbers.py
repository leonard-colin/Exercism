def classify(number):
    factors = []
    if number <= 0:
        raise ValueError("Number must be > 0")
    for factor in range(1, number):
        if number > 0 and number % factor == 0:
            factors.append(factor)
    aliquot_sum = sum(factors)
    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    elif aliquot_sum < number:
        return "deficient"

classify(9008)
