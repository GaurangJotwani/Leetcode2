import pandas as pd

def is_triangle(row):
    return (
        "Yes"
        if (row['x'] + row['y'] > row['z']) 
        and (row['y'] + row['z'] > row['x'])
        and (row['z'] + row['x'] > row['y'])
        else "No"
    )

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    triangle["triangle"] = triangle.apply(is_triangle, axis = 1)
    return triangle
