import pandas as pd

results = pd.read_csv('wyniki.csv')

def searchReco(searchItem):
    recoList = results[results.item1 == searchItem] \
        [["item2", "score"]] \
        .sort_values("score", ascending=[0])

    print("Rekomendacje dla przedmiotu o id ", searchItem, "\n", recoList)

searchReco(1322)