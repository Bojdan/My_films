

class Film:

    def __init__(self, title, ganre, mature, year, actors, director, runtime, budget, box_office, language):
        self.title = title
        self.ganer = ganre
        self. mature = mature
        self.year = year
        self.actors = actors
        self.director = director
        self.runtime = runtime
        self.budget = budget
        self.box_office = box_office
        self.language = language

    def info(self):
        # Тернарный оператор. Возвращ значение слева при выполнении условия, иначе возвпащ. значение справа!
        mature = "18+" if self.mature else "0+"
        print(f"Фильм: {self.title} \n:Жанр: {self.ganer} \nВременя: {self.runtime} минут \nОграничение: {mature}" +
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




