import glob
import time


def violation(num):
    count = 0
    for i in range(num // 4 + 1):
        for j in range(num // 5 + 1):
            if i * 4 + j * 5 == num:
                count += 1
    return count


def find_ways2(num):
    count = 0
    for i in range(num // 4 + 1):
        j = (num - 4*i)//5
        if i*4+j*5 == num:
            count += 1
    return count


files = glob.glob("/Users/yzhao/ccc/2022/senior/s1/s2.*.in")
sorted(files)
for file_name in files:
    with open(file_name, "r") as file:
        for line in file:
            print("working on {}".format(file_name))
            start1 = time.time()
            res1 = find_ways1(int(line))
            time1 = time.time() - start1
            print(file_name)
            print("way1 took {} sec".format(time1))
            start2 = time.time()
            res2 = find_ways2(int(line))
            time2 = time.time() - start2
            print("way2 took {} sec".format(time2))
            expected = -1
            with open(file_name.replace("in", "out")) as ofile:
                expected = int(ofile.readline())
            if res1 != expected:
                print("way1 wrong answer, expected {}, result {}".format(
                    expected, res1))
            if res2 != expected:
                print("way1 wrong answer, expected {}, result {}".format(
                    expected, res2))
