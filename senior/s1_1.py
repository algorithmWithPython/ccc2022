import glob
import time
import os

path = '/Users/yzhao/ccc/2022/senior/s1/'


def find_ways1(num):
    count = 0
    for i in range(num // 4 + 1):
        for j in range(num // 5 + 1):
            if i * 4 + j * 5 == num:
                count += 1
    return count


files = glob.glob(path + 's1.*.in')
files.sort()
for file_name in files:
    with open(file_name, "r") as file:
        for line in file:
            print("working on {}".format(file_name))
            start1 = time.time()
            res1 = find_ways1(int(line))
            time1 = time.time() - start1
            print(file_name)
            print("way1 took {:.6f} sec".format(time1))
            expected = -1
            with open(file_name.replace("in", "out")) as ofile:
                expected = int(ofile.readline())
            if res1 != expected:
                print("way1 wrong answer, expected {}, result {}".format(
                    expected, res1))
