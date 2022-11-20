import time
import random

def time_counter(function):

    def wrapper(*args, **kwargs):

        before_time = time.time()
        value = function(*args, **kwargs)
        after_time = time.time()

        delta_time = after_time - before_time

        print(f"You slept for {delta_time}")

    return wrapper


@time_counter
def go_to_sleep(sleep_time):
    print("Sleep time:", sleep_time)
    time.sleep(sleep_time)

       
sleep_time = random.choice([1,3,5,7])

go_to_sleep(sleep_time)



