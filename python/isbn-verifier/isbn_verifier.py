import string

def is_valid(isbn):
    if "-" in isbn:
        isbn = [i for i in isbn.replace("-", "")]
    else :
        isbn = [i for i in isbn]
            
    if len(isbn) != 10:
        return False

    _sum = 0
    for i in range(9):
        try:
            _sum += int(isbn[i]) * (10 - i)
        except ValueError:
            return False

    if isbn[-1] not in string.digits and isbn[-1] != "X":
        return False
    isbn[-1] = 10 if isbn[-1] == "X" else int(isbn[-1])
    _sum += isbn[-1]

    return True if _sum % 11 == 0 else False
