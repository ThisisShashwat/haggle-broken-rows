"""Deliberately broken: a test case for haggle's ship checks (Hour Detective). It drops the first project from predictions.csv, so a row is missing."""

import pandas as pd

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")
pd.DataFrame({"project_id": test["project_id"], "hours_spent": train["hours_spent"].mean()}).iloc[1:].to_csv("predictions.csv", index=False)
