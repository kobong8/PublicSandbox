from typing import Optional

if __name__ == "__main__":
    num01: Optional[int] = None
    num02: Optional[int] = 2
    num03: Optional[int] = num01 or num02

    print(f"None or 2    : {num03}")

    num01: Optional[int] = None
    num02: Optional[int] = None
    num03: Optional[int] = num01 or num02

    print(f"None or None : {num03}")

    # None or 2    : 2
    # None or None : None
    