import pandas as pd
import numpy as n
import matplotlib.pyplot as plt
import os


# 1 способ
def calculate_amortization_line(C, T, L):
    C_ost = C
    Am_lst = []
    C_ost_lst = []
    for i in range(T):
        Am = (C - L) / T
        C_ost -= Am
        Am_lst.append(round(Am, 2))
        C_ost_lst.append(round(C_ost, 2))
    print("1 способ (линейный)")
    print(f"Am_lst: {Am_lst}")
    print(f"C_ost_lst: {C_ost_lst}")
    return Am_lst, C_ost_lst


# Что это за функция?
# Реализация 2 способа (ускоренный)
# 5/5
def calculate_amortization_fast(C, T, L, k):
    C_ost = C
    Am_lst = []
    C_ost_lst = []
    Aj = 0
    for i in range(T):
        Am = k * (1 / T) * (C - Aj)
        Aj += Am
        C_ost -= Am
        Am_lst.append(round(Am, 2))
        C_ost_lst.append(round(C_ost, 2))
    print("\n2 способ (ускоренный)")
    print(f"Am_lst_2: {Am_lst}")
    print(f"C_ost_lst_2: {C_ost_lst}")
    return Am_lst, C_ost_lst


# Зачем нужна эта функция?
# Она нужна для вызова функций calculate_amortization_line и calculate_amortization_fast
# 4/5
def main():
    # Индивидуальная задача №6
    print("\nИндивидуальная задача №6")
    C = 15000
    T = 6
    L = 0
    k = 2
    Am_lst, C_ost_lst = calculate_amortization_line(C, T, L)
    Am_lst_2, C_ost_lst_2 = calculate_amortization_fast(C, T, L, k)
    login = os.environ["Maslov_login"]
    password = os.environ["Maslov_password"]
    token = os.environ["Maslov_token"]
    print(f"login: {login}")
    print(f"password: {password}")
    print(f"token: {token}")


main()
