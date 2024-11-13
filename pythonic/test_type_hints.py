from __future__ import annotations
from typing import Dict

# 02 from __future__ import annotations
# https://docs.python.org/ko/3.12/library/__future__.html
# future annotations 이 없을 경우 first_method에서 에러 발생
class FirstClass:
    def __init__(self):
        pass

    def first_method(self, input_class: SecondClass):
        pass

class SecondClass:
    def __init__(self):
        pass


if __name__ == "__main__":
    # 01 Type Hints Example
    dict_var01: Dict[str, str] = {'name', '12345678'}
    # error < python 3.9
    # Type Hinting Generics in Standard Collections
    # https://docs.python.org/3.9/whatsnew/3.9.html
    # dict_var02: dict[str, str] = {'name', '12345678'}
    dict_var02: dict = {'name', '12345678'}

    print(dict_var01)
    print(dict_var02)
