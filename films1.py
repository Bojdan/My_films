


class Film:

    def __init__(self, title, ganre, mature, year, director, runtime, budget, box_office, language, description):
        self.title = title
        self.ganer = ganre
        self. mature = mature
        self.year = year
        self.actors = []
        self.director = director
        self.runtime = runtime
        self.budget = budget
        self.box_office = box_office
        self.language = language
        self.description = description

    def __str__(self):
        return f"{self.title}"

    def info(self):
        # Тернарный оператор. Возвращ значение слева при выполнении условия, иначе возвпащ. значение справа!
        mature = "18+" if self.mature else "0+"
        print(f"Фильм: {self.title} \nЖанр: {self.ganer} \nДлительность: {self.runtime} минут \nОграничение: {mature}" +
              "\n" + "Приятного просмотра")

    def show_actors(self):
        print("\n" + "Главные герои:")
        for act in self.actors:
            print(act)

    def leng_translate(self, leng):  # Передаём название. Данный язык в фильме присутствует
        if leng in self.language:
            return True

    def date_releas(self, countre):
        print("Релиз в этом городе: ")
        print(self.year[countre])


class Actor:

    def __init__(self, name, surname, date, rating, biografia, photo):
        self.name = name
        self.surname = surname
        self.data = date
        self._rating = rating
        self.biografia = biografia
        self.photo = photo
        self.films = []

    def __str__(self):
        return f"{self.name} {self.surname}"

    @property
    def rating(self):
        """
        Метод Геттер рейтинга.
        """
        return self._rating

    @rating.setter
    def rating(self, value):
        if value > 5:
            self._rating = 5
        elif value < 1:
            self._rating = 1
        else:
            self._rating = value

    def display_info(self):
        print(self.name, self.surname, self.data)

    def show_films(self):
        print("\n" + "Снимался:")
        for fil in self.films:
            print(fil)

    def get_raitinf(self):
        if self.rating <= 3.0 and self.rating >= 2.0:
            print("Актёр с сложным характером")
        elif self.rating > 3.0 and self.rating <= 4.5:
            print("Харизматичный и умелый актёр")
        elif self.rating > 4.5 and self.rating <= 5.0:
            print("Глаынй претендент на Оскар")
        else:
            print("Ужасный актёр")


