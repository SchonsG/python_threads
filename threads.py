from time import sleep
from threading import Thread


class MyThread(Thread):
    def __init__(self, text, time):
        self.text = text
        self.time = time

        super().__init__()

    def run(self):
        sleep(self.time)
        print(self.text)


t1 = MyThread('Thread 1', 4)
t1.start()

t2 = MyThread('Thread 2', 5)
t2.start()

t3 = MyThread('Thread 3', 6)
t3.start()

for i in range(20):
    print(i)
    sleep(1)

