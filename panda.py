import pandas as pd

data = {
" policy_id": [1001, 1002, 1003, 1004, 1005],
  "customer": ["Dana", "Maya", "Dean", "Blake", "Ron"],
   "premium": [350, 620, 480, 750, 290],
    "status": ["Active", "Active", "Cancelled", "Active", "Cancelled"]
}
df = pd.DataFrame(data)


print(df["customer"])
print(df[df["premium"] > 400])
print(df[df["status"] == "Active"])
print(df[df["status"] == "Cancelled"])