import pandas as pd

uczestnicy_csv = pd.read_csv("PPK_Uczestnicy.csv",error_bad_lines=False, delimiter=';')
pracodawcy_csv = pd.read_csv("PPK_Pracodawcy.csv",sep=';')
merged = pd.merge(
    uczestnicy_csv,
    pracodawcy_csv,
    how='left',
    left_on='EMPL_ID',
    right_on='ID'
)
merged.drop(columns=["MEMBER_ID","LOGICAL_FACTOR_1","LOGICAL_FACTOR_2","ID","PKD_CODE","PPK_BANK","NUMERICAL_VALUE"],inplace=True)

print(merged)
