import concurrent
import math
import multiprocessing
import time
from datetime import datetime

import requests
from concurrent.futures import ThreadPoolExecutor, Future, ProcessPoolExecutor


# seconds=int(input("Insert secondes: "))
# while seconds>0:
#     print(round(seconds,1))
#     time.sleep(0.1)
#     seconds-=0.1
#
# print("DONE")


import sys
from math import factorial
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor, as_completed
from time import perf_counter


def calc_factorial(num):
    return factorial(num)


def calc_factorials(nums: list):
    with ThreadPoolExecutor(len(nums)) as thread_executor:
        tfutures = [thread_executor.submit(factorial, num) for num in nums]
        data = [tfuture.result() for tfuture in tfutures]
        return data, nums


def main(factorials):
    n_workers = 12
    with ProcessPoolExecutor(n_workers) as process_executor:
        pfutures = []
        chunksize = round(len(factorials) / n_workers)
        for i in range(0, len(factorials), chunksize):
            facts = factorials[i:(i + chunksize)]
            pfuture = process_executor.submit(calc_factorials, facts)
            pfutures.append(pfuture)
        for future in as_completed(pfutures):
            data, nums = future.result()
            for d, n in zip(data, nums):
                print(f"{n}! = {d}")


if __name__ == '__main__':
    factorials = [1550 for _ in range(100)]
    start = perf_counter()
    main(factorials)
    end = perf_counter()
    print("Done")
    print(f"[runtime: {end - start}s]")