import time

input('Press ENTER to start')
print()
print()

start_time = time.time()

x = 8
s = 3


def check_number(number):
    check_start_time = time.time()
    sum = 1
    print(number)
    if number % 10 == 6 or number % 10 == 8:
        for i in range(2, int(number ** 0.5)+1):
            if sum > number:
                break
            if number % i == 0:
                sum += i + number / i

    print(str(sum == number) + ' - time all: ' + str(round((time.time()-start_time) * 1000)) + ' milliseconds - check time: '
          + str(round((time.time()-check_start_time) * 1000)) + ' milliseconds - 2^' + str(s))
    print()


while True:
    check_number(int(x-(x/2)**0.5))
    x *= 4
    s += 2

