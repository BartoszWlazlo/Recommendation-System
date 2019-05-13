import pandas as pd

data = pd.read_excel('data.xlsx')
productsData = pd.DataFrame(data, columns= ['product_id','id_order'])
productsData.head()
print(productsData)

#print(userItemData)

# Lista unikatowych produktow
itemList = list(set(productsData["product_id"].tolist()))

# Liczba transakcji
orderCount = len(set(productsData["product_id"].tolist()))

# utworzenie pustej tabelii dla wyyliczonych podobieństw
itemAffinity = pd.DataFrame(columns=('item1', 'item2', 'score'))
rowCount = 0


# dla każdego produktu w liscie, porownanie z innymi
for ind1 in range(len(itemList)):

    # lista transakcji, w ktorych zawarty jest produkt 1
    item1Orders = productsData[productsData.product_id == itemList[ind1]]["id_order"].tolist()
    print("Item 1 ", item1Orders)

    # weź produkt 2 - produkty, ktore nie sa produktem 1 albo te, ktore nie sa przeanalizowane
    for ind2 in range(ind1, len(itemList)):

        if (ind1 == ind2):
            continue

        # lista transakcji, ktore zawierają produkt 2
        item2Orders = productsData[productsData.product_id == itemList[ind2]]["id_order"].tolist()
        print("Item 2 ",item2Orders)

        # lista transakcji z produktami 1 oraz 2, podzielenie przez ogolna liczbe transakcji

        commonOrders = len(set(item1Orders).intersection(set(item2Orders)))
        score = commonOrders / orderCount

        # Add a score for item 1, item 2
        # dodanie wyniku dla produktu 1, produktu 2
        itemAffinity.loc[rowCount] = [itemList[ind1], itemList[ind2], score]
        rowCount += 1
        # Dodanie wyniku dla produktu 1, produktu 2. Ten sam wynik odnosi sie do niezależnych sekwencji.
        itemAffinity.loc[rowCount] = [itemList[ind2], itemList[ind1], score]
        rowCount += 1

# sprawdzenie wynikow
itemAffinity.head()

searchItem = 6034

recoList=itemAffinity[itemAffinity.item1==searchItem]\
        [["item2","score"]]\
        .sort_values("score", ascending=[0])

print("Rekomendacje dla przedmiotu o id ", searchItem, "\n", recoList)