list1 = [1,2,3,4,5]

def list_sum(numbers):
    if not numbers:     # nebo if len(numbers == 0)
        return 0
    return numbers[0] + list_sum(numbers[1:])

print(list_sum(list1))



def count_char(some_string: str, character: str) -> int:
    if not some_string:
        return 0
    #match = 1 if some_string[0] == character else 0
    #return match + count_char(some_string[1:], character)
    return (some_string[0] == character) + count_char(some_string[1:], character)



print(count_char("Algoritmy jsou super zabava", "a")) # -> 3


def fibo_rec(n):
    if n == 0 or n == 1:
        return n
    return fibo_rec(n - 1) + fibo_rec(n - 2)

def is_palindrome_rec(text):
    pass


def is_palindrome(text):
    text = text.replace(" ", "").lower()
    return text == text[::-1]
