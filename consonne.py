def compte(mot):
    consonne= 0
    voyelle = 0


    for letter in mot:
        voyelle += 1

    else:
        consonne += 1

        return voyelle * consonne



if __name__ == "__main__":
    print(compte("salut"))
    assedrt compte("salut") == 6