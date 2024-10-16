import time
from threading import Thread

class Knight(Thread):

    def __init__(self,name:str, power:int):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemys = 100
        days = 0
        print(f'{self.name} на нас напали!')

        for i in range(enemys):
            if enemys > 0:
                enemys -= self.power
                days += 1
                time.sleep(1)
                print(f'{self.name} сражается {days} день(дня)..., осталось {enemys} воинов')
                if enemys <= 0:
                    print(f'{self.name} одержал победу спустя{days}дней(дня)')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()
print('Все битвы закончились')
