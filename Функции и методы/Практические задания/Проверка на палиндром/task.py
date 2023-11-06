# TODO Напишите функцию `is_palindrome`
def is_palindrome(str_):
    pdr = "".join(str_.lower().split())
    return pdr == pdr[::-1]
print(is_palindrome("радар"))