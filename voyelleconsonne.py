def replace(mot):

    voyelles = ""
    consonnes = "."
    result = ""

    for letter in mot:
        if letter in "aeiouy":
            result += ""
        else:
            result += "."

    return result

if __name__ == "__main__":
    print("bonjour")
    print(replace("bonjour"))
    print("voiture")
    print(replace("voiture"))
    assert (replace("bonjour")) == "...."
    assert (replace("voiture")) == "...*"