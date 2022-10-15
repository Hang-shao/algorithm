
# 冒泡排序
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):  #[0,n)
        for j in range(1, n - i):   #[1,n-1)
            if lst[j - 1] > lst[j]:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
    return lst

# 选择排序
def selection_sort(lst):
    n=len(lst)
    for i in range(n- 1):
        min_index = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i] #交换位置
    return lst

# 快速排序
def quick_sort(lst):
    n = len(lst)
    if n <= 1:
        return lst
    baseline = lst[0]
    left = [lst[i] for i in range(1, n) if lst[i] < baseline]   #取baseline左边序列
    right = [lst[i] for i in range(1, n) if lst[i] >= baseline] #取baseline右边序列
    return quick_sort(left) + [baseline] + quick_sort(right)

# 归并排序
def merge_sort(lst):
    def merge(left,right):
        i = 0
        j = 0
        result = []
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result = result + left[i:] + right[j:]
        return result
    n = len(lst)
    if n <= 1:
        return lst
    mid = n // 2
    left = merge_sort(lst[:mid])    # [0,mid)
    right = merge_sort(lst[mid:])   # [mid n)
    return merge(left,right)

# 堆排序
def heap_sort(lst):
    def adjust_heap(lst, i, size):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        largest_index = i
        if left_index < size and lst[left_index] > lst[largest_index]:
            largest_index = left_index
        if right_index < size and lst[right_index] > lst[largest_index]:
            largest_index = right_index
        if largest_index != i:
            lst[largest_index], lst[i] = lst[i], lst[largest_index]
            adjust_heap(lst, largest_index, size)

    def built_heap(lst, size):
        for i in range(len(lst)//2)[::-1]:
            adjust_heap(lst, i, size)

    size = len(lst)
    built_heap(lst, size)
    for i in range(len(lst))[::-1]:
        lst[0], lst[i] = lst[i], lst[0]
        adjust_heap(lst, 0, i)
    return lst

# 插入排序
def insertion_sort(lst):
    for i in range(len(lst) - 1):   #[0,n-1)
        cur_num, pre_index = lst[i+1], i
        while pre_index >= 0 and cur_num < lst[pre_index]:
            lst[pre_index + 1] = lst[pre_index]
            pre_index -= 1
        lst[pre_index + 1] = cur_num
    return lst

# 希尔排序
def shell_sort(lst):
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            for j in range(i, gap - 1, -gap):
                if lst[j] < lst[j - gap]:
                    lst[j], lst[j - gap] = lst[j - gap], lst[j] #交换
                else:
                    break
        gap //= 2
    return lst

# 计数排序
def counting_sort(lst):
    nums_min = min(lst)
    bucket = [0] * (max(lst) + 1 - nums_min)
    for num in lst: #统计次数
        bucket[num - nums_min] += 1
    i = 0
    for j in range(len(bucket)):
        while bucket[j] > 0:
            lst[i] = j + nums_min
            bucket[j] -= 1
            i += 1
    return lst

# 桶排序
def bucket_sort(lst, defaultBucketSize=4):
    maxVal, minVal = max(lst), min(lst)
    bucketSize = defaultBucketSize
    bucketCount = (maxVal - minVal) // bucketSize + 1
    buckets = [[] for i in range(bucketCount)]  #桶划分
    for num in lst: #数据入桶
        buckets[(num - minVal) // bucketSize].append(num)
    lst.clear()
    for bucket in buckets:
        bubble_sort(bucket)     #桶内排序
        lst.extend(bucket)      #数据合并
    return lst

# 基数排序
def radix_sort(lst):
    mod = 10
    div = 1
    mostBit = len(str(max(lst)))
    buckets = [[] for row in range(mod)]
    while mostBit:
        for num in lst:
            buckets[num // div % mod].append(num)   #取个/十/百..位数
        i = 0
        for bucket in buckets:
            while bucket:
                lst[i] = bucket.pop(0)  #将桶中的数值串起来
                i += 1
        div *= 10
        mostBit -= 1
    return lst

def print_hi(name):
    LL=[12,53,23,64,76,31,97,89,46]
    # LL=bubble_sort(LL)
    # LL=selection_sort(LL)
    # LL = quick_sort(LL)
    # LL = merge_sort(LL)
    # LL = heap_sort(LL)
    # LL = insertion_sort(LL)
    # LL = shell_sort(LL)
    # LL = counting_sort(LL)
    # LL = bucket_sort(LL)
    LL = radix_sort(LL)

    print(f'正序：{LL}')

if __name__ == '__main__':
    print_hi('PyCharm')
