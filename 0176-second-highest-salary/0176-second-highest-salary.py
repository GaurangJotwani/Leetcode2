import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    employee = employee.drop_duplicates(["salary"])
    if len(employee["salary"].unique()) < 2:
        return pd.DataFrame({"SecondHighestSalary": [np.NaN]})
    
    emp = employee.sort_values("salary", ascending=False)
    emp.drop("id", axis=1, inplace = True)

    emp.rename({"salary": "SecondHighestSalary"}, axis = 1, inplace = True)

    return emp.head(2).tail(1)