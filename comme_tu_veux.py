def number(chiffre):
    resultat = []

    for n in chiffre:
        resultat.append(transform_number(n))
        # a = transform_number(n)
        #         resultat.append(a)

    return resultat


def transform_number(n):
    if n % 5 == 0:
        var = n/5
    else:
        var = n*2

    return var



if __name__ == "__main__":
    assert number([2, 15, 25, 6, 13]) == [4, 3, 5, 12, 26]
