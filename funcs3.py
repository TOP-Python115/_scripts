from pprint import pprint

def list_editor(numbers_list):
    i, v = map(int, input().split())
    numbers_list[i] = v

l = list(range(1, 10))
