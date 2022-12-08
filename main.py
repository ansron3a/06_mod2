import datetime as DT
import datetime


def str_to_date(self_date, other_date):
    dt1 = self_date.split(".")
    dt2 = other_date.split(".")
    self_bdate = DT.date(int(dt1[2]), int(dt1[1]), int(dt1[0]))
    other_bdate = DT.date(int(dt2[2]), int(dt2[1]), int(dt2[0]))
    return self_bdate, other_bdate


class Car:
    def __init__(self, vin, nomer, marka, model, age, power, probeg, vladelec, price):
        self.vin = vin
        self.nomer = nomer
        self.marka = marka
        self.model = model
        self.age = age
        self.power = power
        self.probeg = probeg
        self.vladelec = vladelec
        self.price = price

    # Вывод информации о автомобиле
    def __str__(self):
        return f"VIN-код: {self.vin}, гос номер: {self.nomer}, марка: {self.marka}, модель: {self.model}," \
               f"год выпуска: {self.age}, мощность двигателя: {self.power}, пробег: {self.probeg}, " \
               f"кол-во владельцев: {self.vladelec}, стоимость: {self.price}"

    # Увеличивает пробег на указанное количество
    def set_mileage_km(self, summa):
        self.probeg += summa

    # Сравнение автомобилей >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        self_probeg, other_probeg = str_to_date(self.probeg, other.probeg)
        return self_probeg < other_probeg

    def __eq__(self, other):  # ==
        self_probeg, other_probeg = str_to_date(self.probeg, other.probeg)
        return self_probeg == other_probeg

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False

    def get_age(self):
        d = datetime.date.today().year
        return f"Возраст авто: {d - self.age}"


class Owner:
    def __init__(self, fio, nomer_vod, bdate, region, avto):
        self.fio = fio
        self.nomer_vod = nomer_vod
        self.bdate = bdate
        self.region = region
        self.avto = avto

    # Вывод информации о владельце
    def __str__(self):
        return f"ФИО: {self.fio}, номер водительского удостоверения: {self.nomer_vod}, " \
               f"дата рождения: {len(self.bdate)}, область: {self.region}, автомобили: {self.avto}"

    # Сравнение автовладельцев по возрасту >, >=, <, <=, ==, !=
    def __lt__(self, other):  # <
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate < other_bdate

    def __eq__(self, other):  # ==
        self_bdate, other_bdate = str_to_date(self.bdate, other.bdate)
        return self_bdate == other_bdate

    def __le__(self, other):  # <=
        if self.__eq__(other):
            return True

        if self.__lt__(other):
            return True
        else:
            return False


car_1 = Car('KSDUSUDH6KJHJ34FG2', 'А345РН750', 'LADA', 'Granta', 2020, 98, 1000, 1, 750000)
print(car_1)

man_1 = Owner("Иванов И.И.", 1316541237, '12.08.2000', 'Республика Мордовия', 'Kia')
man_2 = Owner("Сидоров С.С.", 2541236541, '10.01.1995', 'Ульяновская', 'Lada')
print(man_1)
print(man_2)

print(man_1 < man_2)
print(man_1 > man_2)
print(man_1 == man_2)
print(man_1 <= man_2)
print(man_1 >= man_2)

print(car_1.get_age())
