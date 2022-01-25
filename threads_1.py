from time import sleep
from threading import Thread


def gonna_take_a_while(text, time):
    sleep(time)
    print(text)


t1 = Thread(target=gonna_take_a_while, args=("hello world!", 15))
t1.start()

t2 = Thread(target=gonna_take_a_while, args=("hello world 2!", 1))
t2.start()

t3 = Thread(target=gonna_take_a_while, args=("hello world 3!", 2))
t3.start()

for i in range(5):
    print(i)
    sleep(.5)

while t1.is_alive():
    print("Esperando a thread 1 acabar")
    sleep(2)

