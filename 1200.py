from collections import defaultdict
# def minimumAbsDifference(arr):
#     # works but inefficient and times out
#     diffs = defaultdict(list)
#     length = len(arr)
#     for i in range(length):
#         for j in range(length):
#             if j > i:
#                 a = arr[i]
#                 b = arr[j]
#                 if a < b:
#                     diffs[abs(b-a)].append([a, b])
#                 else:   
#                     diffs[abs(b-a)].append([b, a])
#     minimum = min(list(diffs.keys()))
#     res = sorted(diffs[minimum], key = lambda x: x[0])
#     return res

def minimumAbsDifference(arr):
    arr.sort()
    # rev = sorted(arr, reverse=True)
    minimum = max(arr)
    for x in range(len(arr) - 1):
        a = arr[x]
        b = arr[x + 1]
        diff = abs(b - a)
        if diff < minimum: minimum = diff

    # minimum = min([abs(b - a) for b, a in zip(arr,rev)], abs(arr[-2] - arr[-1]), abs(arr[1] - arr[0]))
    i = 0
    j = 1
    pairs = []
    while j < len(arr):
        b = arr[j]
        a = arr[i]
        diff = abs(b - a)
        if diff > minimum:
            i+=1
        elif diff < minimum:
            j+=1
        else:
            pairs.append([a, b])
            j+=1
        if i == j:
            j+=1
    return pairs
        

if __name__ == "__main__":
    test = [4,2,1,3] # ==> [[1,2],[2,3],[3,4]]
    # test = [1,3,6,10,15]  # ==> [[1,3]]
    # test = [40,11,26,27,-20] # ==> [[26,27]]
    res = minimumAbsDifference(test) 
    print(res)