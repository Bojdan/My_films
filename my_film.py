from films1 import Film, Actor
import datetime


def connekt_kino(film, *actors):
    """
    Связь актёра и фильма
    """
    for actor in actors:
        film.actors.append(actor)
        actor.films.append(film)
    film.show_actors()



x = Film("Kill Bill 3", "Драмма", True, {"Нью-Йорк": 2004, "Москва": 2005, "Токио": 2006},
         "Tarantino", 99, 8000000, 10000000, ["Rus", "Eng"], "Нормальный фильм, идите и посмотрите!"
         )

x2 = Film("Властелин колец", "Фентези", True, {"Аризона": 2003},
          "Питер Джексон", 180, 2000000, 30000000, ["Rus", "Eng"], "топ кинцо"
          )

x3 = Film("Мишка фредди", "Мультмк", False, {"Аргентина": 2012},
          "Франк Берни", 131, 180000, 22000000, ["Rus", "Eng"], "Ужс"
          )


film_list = [x, x2, x3]

def yers_serch(film_list):
    for m in film_list:
        if not m.mature:
            print(m)

def raiting_serch(min_rating, max_rating, actor_list):
    for a in actor_list:
        if a.rating >= min_rating and a.rating <= max_rating:
            print(a)


actor1 = Actor("Джони", "Дэпп", datetime.date(1988, 5, 1),
               4.7, "крутой чел", "фото нет")
actor2 = Actor("Роберт", "Дауни", datetime.date(1987, 4, 13), 4.0, "Сложный", "Фото нет")
actor3 = Actor("Том", "Харди", datetime.date(1876, 5, 4), 4.3, "Сложный", "Фото нет")



actor_list = [actor3, actor2, actor1]


# connekt_kino(x, actor1, actor2, actor3)

raiting_serch(4.5, 5, actor_list)

yers_serch(film_list)