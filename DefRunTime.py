import time

def calculate_run_time(dif,arg):
    start = time.perf_counter()
    dif(arg)
    end = time.perf_counter()
    return (end - start)