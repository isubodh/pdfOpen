PREFIX = "subo"

def getNextDate():
    for date in range(31):
        date += 1
        if date < 10:
            val = '0' + str(date)
        else :
            val =  str(date)
        yield val

def getNextMonth():
    for month in range(12):
        month += 1
        if month < 10:
            val = '0' + str(month)
        else:
            val = str(month)
        yield val

def main():
    if __name__ == "__main__":
        for month in getNextMonth():
            for date in getNextDate():
                print(PREFIX + str(date) + str(month))
    else :
        print("Not in main")

main()