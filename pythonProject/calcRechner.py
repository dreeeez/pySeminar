def calculateTemp(temp, unit):
    temp = float(temp)
    if (unit == 'c' or unit == 'C'):
        return (temp * 9 / 5) + 32
    elif (unit == 'f' or unit == 'F'):
        return (temp - 32) * 5 / 9
    else:
        return "invalid"

def main():
    while True:
        einheit = input("Bitte Einheit angeben: (C°/F°)\n")
        temp = input("Temp eingeben\n")
        print(calculateTemp(temp, einheit))
        einheit = input("Aufhören? (j/n)\n")
        if(einheit == 'j'):
            break

if __name__ == "__main__":
    main()
