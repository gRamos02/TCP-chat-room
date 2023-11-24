# funcion xor
# TODO: cambiar la funcion para usar enteros en lugar de arreglos
def xor(a, b):
    result = []

    for i in range(0, len(b)):
        if a[i] == b[i]:
            result.append("0")
        else:
            result.append("1")

    return "".join(result)


# TODO: Lo mimso
def mod2div(dividendo, divisor):
    pick = len(divisor)
    tmp = dividendo[0:pick]

    while pick < len(dividendo):
        if tmp[0] == "1":
            tmp = xor(divisor, tmp) + dividendo[pick]
        else:
            tmp = xor("0" * pick, tmp) + dividendo[pick]
        pick += 1

        if tmp[0] == "1":
            xor(divisor, tmp)
        else:
            xor("0" * pick, tmp)

        checkword = tmp
        return checkword


if __name__ == "__main__":
    print("PRUEBA XOR")
    # c=xor(a, b)
    print(mod2div(["1", "1", "1", "0", "1"], ["1", "0", "0", "1"]))

