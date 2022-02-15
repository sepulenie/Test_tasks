import time

time1=time.time()
fizz = 3
buzz = 5
for i in range(1,1000001):
    print(i if i%fizz != 0 and i%buzz != 0 else '',
          'Fizz' if i%fizz == 0 else '',
          'Buzz' if i%buzz == 0 else '', 
           sep='')
time2=time.time()
print(time2-time1)