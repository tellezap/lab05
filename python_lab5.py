from math import remainder


def is_valid_part(part):
    # check input can be converted to an integer
    try:
        num = int(part)
    except ValueError:
        return False

    # input is int between 0 and 255
    if 0 < num > 255:
        return False

    # no leading zero's unless input is 0
    if len(part) > 1 and part[0] == "0":
        return False

    return True

def is_valid_ip(ip):
    # split the input string by period
    parts = ip.split(".")

    # 4 parts to ip address must be true
    if len(parts) != 4:
        return False

    for part in parts:
        if not is_valid_part(part):
            return False

    return True

print(is_valid_ip("192.168.1.1"))
print(is_valid_ip("192.168.256.1"))
print(is_valid_ip("192.168.1"))
print(is_valid_ip("192.168.01.1"))

def decimal_to_binary(n):
    if n == 0:
        return "0"
    if n == 1:
        return "1"
    return (decimal_to_binary(n//2) + str(n%2))

print(decimal_to_binary(10))

def binary_to_decimal(b):
    if b == "":
        return 0
    return int(b[0]) * 2 ** (len(b) - 1) + binary_to_decimal(b[1:])

print(binary_to_decimal("1010"))