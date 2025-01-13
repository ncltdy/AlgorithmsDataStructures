import bisect

# bisect.insort, bisect.bisect (nebo verze left right)
# Spoj a serad dva seznamy do jednoho
def merge_two_lists(list1, list2):
        list_total = list1 + list2
        result = []
        for num in list_total:
            bisect.insort(result, num)
        return result

print(merge_two_lists([2, 8, 3], [87, 75, 6]))  # -> [2,3,6,8,75,87]