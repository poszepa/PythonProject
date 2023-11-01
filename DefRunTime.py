import time

def calculate_run_time(func, how_many_times = 1, *arg):
    sumTime = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(*arg)
        end = time.perf_counter()
        sumTime += (end - start)
    return sumTime


def calculate_run_time_more_args(func,arg, arg2 = "", how_many_times = 1):
    sumTime = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        func(arg, arg2)
        end = time.perf_counter()
        sumTime += (end - start)
    return sumTime