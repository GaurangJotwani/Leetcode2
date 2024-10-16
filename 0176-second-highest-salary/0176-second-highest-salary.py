import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    
    
    distinct_salaries = employee['salary'].drop_duplicates()

    if len(distinct_salaries) < 2:
        second_highest_salary = None
    else:
        top_two_salaries = distinct_salaries.nlargest(2)
        second_highest_salary = top_two_salaries.iloc[-1]
    
    return pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
