def f(mot):
    consonne = ""
    voyelle = ""

    for lettre in mot:
        if lettre not in "aeiouy":
            consonne += lettre
        else :
            voyelle += lettre

    return consonne + voyelle




if __name__ == "__main__":
    print(f("bonjour"))
    assert f("bonjour") == "bnjroou"
