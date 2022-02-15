from threading import Thread, Event
import time

time1=time.time()
event_1 = Event()
event_2 = Event()
fizz = 3
buzz = 5
def func_1(ev1, ev2, thread_name=str):
    for i in range(1, 1000001, 2):
        ev2.wait()  # wait for the second thread to hand over
        ev2.clear()  # clear the flag
        print('threadname=',thread_name,' ', 
              i if i%fizz != 0 and i%buzz != 0 else '',
              'Fizz' if i%fizz == 0 else '',
              'Buzz' if i%buzz == 0 else '', 
              sep='')
        ev1.set()  # wake the second thread

def func_2(ev1, ev2, thread_name=str):
    for i in range(2, 100001, 2):
        ev2.set()  # wake the first thread
        ev1.wait()  # wait for the first thread to hand over
        ev1.clear()  # clear the flag
        print('threadname=',thread_name,' ', 
              i if i%fizz != 0 and i%buzz != 0 else '',
              'Fizz' if i%fizz == 0 else '',
              'Buzz' if i%buzz == 0 else '', 
              sep='')
    time2=time.time()
    print(time2-time1)
t1 = Thread(target=func_1, args=(event_1, event_2, 'Thread 1'))
t2 = Thread(target=func_2, args=(event_1, event_2, 'Thread 2'))

t1.start()
t2.start()