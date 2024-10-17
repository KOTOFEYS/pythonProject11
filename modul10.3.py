import time
import random
from threading import Thread, Lock
class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()


    def deposit(self):
        for i in range(0,100):
            rand_numb = random.randint(50,500)
            self.balance += rand_numb
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение:{rand_numb}. Баланс:{self.balance}.')
            time.sleep(0.001)

    def take(self):
        for self.balance in range(0, 100):
            rand_numb = random.randint(50, 500)
            print(f'Запрос на {rand_numb}.')
            time.sleep(0.001)
            if rand_numb <= self.balance:
                self.balance -= rand_numb
                print(f'Снятие: {rand_numb}. Баланс: {self.balance}.')
                time.sleep(0.001)
            if rand_numb >= self.balance:
                print(f'Запрос отклонён, недостаточно средств.')
                time.sleep(0.001)
                self.lock.acquire()




bk = Bank()
th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')