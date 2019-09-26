from collections import defaultdict
def minimumAbsDifference(arr):
    # works but inefficient and times out
    diffs = defaultdict(list)
    length = len(arr)
    for i in range(length):
        for j in range(length):
            if j > i:
                a = arr[i]
                b = arr[j]
                if a < b:
                    diffs[abs(b-a)].append([a, b])
                else:   
                    diffs[abs(b-a)].append([b, a])
    minimum = min(list(diffs.keys()))
    res = sorted(diffs[minimum], key = lambda x: x[0])
    return res
        

if __name__ == "__main__":
    test = [4,2,1,3] # ==> [[1,2],[2,3],[3,4]]
    res = minimumAbsDifference(test)
    print(res)