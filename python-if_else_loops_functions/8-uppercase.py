def uppercase(str):
    for lettre in str:
        if ord('a') <= ord(lettre) <= ord('z'):
            lettre = chr(ord(lettre) - 32)
        print(f"{lettre}", end="")
    print("")
