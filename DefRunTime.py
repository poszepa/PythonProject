import time

def calculate_run_time(dif,arg, how_many_times = 1):
    sumTime = 0
    for i in range(0, how_many_times):
        start = time.perf_counter()
        dif(arg)
        end = time.perf_counter()
        sumTime += (end - start)
    return sumTime