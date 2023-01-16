import glob
import time

path = '/Users/yzhao/ccc/2022/senior/s3/'


def countSample(n, m, k):
    res = []
    if k < n:
        print("no solution due to too small samples")
        return [-1]

    for i in range(n):
        if k == n-i:
            # happy path
            # just need to append the same value to the result list and return
            val = res[-1] if res else 1
            res.extend([val for i in range(k)])
            return res

        curSamples = min(k-(n-i-1), m)
        if curSamples <= i:
            res.append(res[-curSamples])
        else:
            curSamples = i+1
            res.append(i+1)
        k -= curSamples

    if k == 0:
        print("special result, last one is not repeated")
        return res
    # if k>0, there is no solution
    print("no solution due to too many samples")
    return [-1]


files = glob.glob(path + 's3*.in')
# files = glob.glob(path + 's3.4-99.in')
files.sort()
for file_name in files:
    with open(file_name, "r") as file:
        start = time.time()
        [n, m, k] = [int(v) for v in file.readline().split()]
        print("input: {}, {}, {}".format(n, m, k))

        res = countSample(n, m, k)
        duration = time.time() - start
        print(file_name)
        print("took {:.6f} sec".format(duration))
        # print("music: {}".format(res))
