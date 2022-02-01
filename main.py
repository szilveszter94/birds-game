import pandas
import turtle
#Turtle modul konfigurálása
teknos = turtle.Turtle()
teknos.hideturtle()
teknos.penup()
hatter = turtle.Screen()
hatter.setup(width=768, height=768)
hatter.bgpic("madar.gif")
#adatbázis olvasása, listák létrehozása
data = pandas.read_csv("madar_nevek.csv")
data_list = data.names.to_list()
eltalalt_nevek = []
game = True
tanulando_nevek = []
eredmeny = 0
#játék indítása végtelen ciklussal, amíg a game=igaz
while game:
    kerdes = hatter.textinput(title=f"Elért eredmény: {eredmeny}/9", prompt=("Írd be a madár nevét: \nHa nincs már "
                                                                             "tipped, írd "
                                                                             "be: Feladom")).lower()
    #válasz vizsgálata, ha igaz, akkor kiírja feketével
    if kerdes in data_list and kerdes not in eltalalt_nevek:
        eltalalt_nevek.append(kerdes)
        koord_lista = data[data.names == kerdes]
        teknos.goto(int(koord_lista.x), int(koord_lista.y))
        teknos.color("black")
        teknos.pencolor("black")
        teknos.write(arg=kerdes, align="center", font=("Impact", 20, "normal"))
        eredmeny += 1
        # ha 9 helyes, akkor vége a játéknak
    if eredmeny == 9:
        teknos.color("magenta")
        teknos.goto(-200, 0)
        teknos.write(arg="Gratulálok, nyertél!",align = "left", font=("Impact", 40, "bold"))
        # ha feladja, akkor a nem eltalált neveket pirossal kiírja
        break
    if kerdes == "feladom":
        for i in data_list:
            if i not in eltalalt_nevek:
                teknos.color("red")
                tanulando_koord = data[data.names == i]
                teknos.goto(int(tanulando_koord.x), int(tanulando_koord.y))
                teknos.write(arg=i, align="center", font=("Impact", 20, "normal"))
        break

hatter.mainloop()
