from threading import Thread, Lock
from time import sleep


class Ticket:
    def __init__(self, stock):
        self.stock = stock
        self.lock = Lock()

    def buy(self, quantity):
        # To lock the method
        self.lock.acquire()

        if self.stock < quantity:
            print("Não temos ingressos suficientes")
            self.lock.release()
            return

        sleep(1)

        self.stock -= quantity

        print(f"Você comprou {quantity} ingressos.")
        print(f"Ainda temos {self.stock}")

        self.lock.release()

if __name__ == "__main__":
    tickets = Ticket(10)

    for i in range(1,20):
        t = Thread(target=tickets.buy, args=(i,))
        t.start()

