def reverse_number(n: int) -> int:
    rev = 0
    while n >0:
        digit = n % 10
        rev = rev * 10 + digit
        n = n // 10
    return rev

if __name__ == "__main__":
    n = int(input())
    print(reverse_number(n))
3) find max and min ele?
def find_max_min(arr):
    if not arr:
        return none, None
    max_ele = arr[0]
    min_ele = arr[0]
    for num in arr:
        if num > max_ele:
            max_ele = num
            if num < min_ele:
                min_ele = num
            return max_ele, min_ele
        if num < min_ele:
            min_ele = num
            return max_ele, min_ele
        if num == max_ele:
            return max_ele, min_ele
        if num == min_ele:
            