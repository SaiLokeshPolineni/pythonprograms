from collections import defaultdict
def countTriplets(arr, r):
    v2 = defaultdict(int)
    v3 = defaultdict(int)
    count = 0
    for k in arr:
        count += v3[k]
        v3[k*r] += v2[k]
        v2[k*r] += 1

    return count

arr=[1, 5, 5, 25, 125]
r=5
print(countTriplets(arr, r))