import  pandas as pd

income = 7500
budget = {
"categoory": [
"food",
"tranportion",
"oersonal",
"enterament",
 "saving"

],
"amount": [800, 300, 600, 200, 2000]
}

df = pd.DataFrame(budget)
print(df)
print('total', df["amount"].sum())

