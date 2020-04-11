##question no 3
def check(ip):
    splitted_str = ip[2:]
    splitted_str = "0x" + splitted_str
    print(splitted_str)
    prefix = ip[:2].upper()
    try:
        decimal_splitted = str(int(splitted_str, 16))
        sum = 0
        for val in decimal_splitted:
            sum += int(val)
        hex_sum = hex(sum).split('x')[-1]

        if prefix == hex_sum.upper():
            return "VALID"
        else:
            return "INVALID"
    except Exception as e:
        return "INVALID"