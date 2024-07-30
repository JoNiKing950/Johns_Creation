def bottles_of_beer(beer):
    if beer < 1:
        print("Нет бутылок пива на стене , нет бутылок пива.")
        return

    pop = beer
    beer -= 1
    print("""{} бутылок пива на стене , {} бутылок пива.
            возьми одну , пусти по кругу , {} бутылок пива на стене.""".format(pop , pop, beer))
    try:
        bottles_of_beer(beer)
    except(NameError , ValueError , TypeError , ZeroDivisionError):
        print("Упс! Не удалось посчитать сколько бутылок пива на стене , сколько бутылок пива")
        


try:    
    h = int(input("Введи сколько бутылок пивандопола , Bitch!"))
    bottles_of_beer(h)
except ValueError:
    print("Упс! Не удалось посчитать сколько бутылок пива на стене , сколько бутылок пива")

