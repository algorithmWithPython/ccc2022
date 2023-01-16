import glob
import time

path = '/Users/yzhao/ccc/2022/senior/s2j4/'


def violation(rule1, rule2, groups):
    names = {}
    repeated = []
    for gIdx, g in enumerate(groups):
        for p in g:
            if p in names:
                print("person in multiple group: {}".format(p))
            names[p] = gIdx

    count = 0
    for [n1, n2] in rule1:
        if (n1 not in names) or (n2 not in names) or (names[n1] != names[n2]):
            count += 1

    for [n1, n2] in rule2:
        if (n1 in names) and (n2 in names) and (names[n1] == names[n2]):
            count += 1

    return count


files = glob.glob(path + 's2*.in')
# files = glob.glob(path + 's2.sample-02.in')
files.sort()
for file_name in files:
    with open(file_name, "r") as file:
        start = time.time()
        r1Num = int(file.readline())
        rule1 = [file.readline().strip().split() for i in range(r1Num)]
        # print(rule1)
        r2Num = int(file.readline())
        rule2 = [file.readline().strip().split() for i in range(r2Num)]
        # print(rule2)
        gNum = int(file.readline())
        groups = [file.readline().strip().split() for i in range(gNum)]
        # print(groups)
        res = violation(rule1, rule2, groups)
        duration = time.time() - start
        print(file_name)
        print("took {:.6f} sec".format(duration))
        expected = -1
        with open(file_name.replace("in", "out")) as ofile:
            expected = int(ofile.readline())
        if res != expected:
            print("wrong answer, expected {}, result {}".format(expected, res))
