def slices(series, length):
    if int(length) > len(series) or length <= 0:
        raise ValueError("The length must be 0 < length <= series number of digits")
    slices_lst = []
    i = 0
    while i < (len(series)-length+1):
        slices_lst.append(series[i:i+length])
        i += 1
    return slices_lst
