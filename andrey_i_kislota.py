# n = int(input())
a = list(map(int, input().split()))
n = len(a)


def solution(arr):
    count = 0
    for i in range(n - 1):
        if arr[i] < 0:
            return -1
        if arr[i] <= arr[i + 1]:
            liters = arr[i + 1] - arr[i]
            if liters > 0:
                count += liters
        else:
            return -1

    return count


print(solution(a))
