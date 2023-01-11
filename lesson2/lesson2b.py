
2#

lang = input("enter the country: ")

match lang:
    case "USA":
        print("Dollar")

    case "israel":
        print("NIS")

    case "EU":
        print("Euro")

    case "UK":
        print("Pound")

    case _:
        print("I dont know")