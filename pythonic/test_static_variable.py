from typing import List
import numpy as np
import pandas as pd


def func_counter() -> None:
    func_counter.cnt += 1
    print(f"cnt: {func_counter.cnt}")


def sum_calculator_list(num: float) -> float:
    sum_calculator_list.sum_list.append(num)
    sum_value = np.sum(sum_calculator_list.sum_list)
    return sum_value


def sum_calculator_pd(df: pd.DataFrame) -> float:
    sum_calculator_pd.sum_df = pd.concat([sum_calculator_pd.sum_df, df], ignore_index=True)
    sum_value = sum_calculator_pd.sum_df.mean(axis=0)
    sum_value = sum_value.values[0]
    return sum_value


if __name__ == "__main__":
    print("func_counter")
    func_counter.cnt: int = 0
    for i in range(10):
        func_counter()
    print()        

    print("sum_calculator_list")
    sum_calculator_list.sum_list: List = []
    for i in range(1, 11):
        sum_value = sum_calculator_list(i)
        print(f"sum: {sum_value}")
    print()

    print("sum_calculator_pd")
    sum_calculator_pd.sum_df: pd.DataFrame = pd.DataFrame()
    for i in range(1, 11):
        df: pd.DataFrame = pd.DataFrame([i for i in range(i, 11)], columns=['value'])
        sum_value = sum_calculator_pd(df)
        print(f"sum: {sum_value}")
    print()        

# reference:
# [1] https://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
