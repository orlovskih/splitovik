from woocommerce import API
import pandas as pd

wcapi = API(
    url="https://splitovik.ru",
    consumer_key="ck_b386c34cc21c495c288913d37a8ecde73ffcffaa",
    consumer_secret="cs_fba9bb4212f793e19e4dfca6f6bc65ca750bb293",
    wp_api=True,
    version="wc/v3"
)

print(wcapi.get("products").json())
listOfProductFromSite = wcapi.get("products").json()

file = 'Каталог (7).xlsx'
priceData = pd.read_excel(file)

for i in range(priceData.shape[0]):
    priceDataString = pd.read_excel(file).to_dict(orient='records')
    print(df[i])

priceList = ['31407', 'X4734166']

for i in range(len(listOfProductFromSite)):
    for j in range(len(sku_base)):
        try:
            if str(listOfProductFromSite[i]['sku']) == priceList[j]:
                get_id = listOfProductFromSite[i]['id']
                listOfProductFromSite[i].clear()
                print(get_id)
        except:
            print(Exception)

print(listOfProductFromSite)


'''for i in listOfProductFromSite:
    try:
        pass

#id = listOfProductFromSite[0]['id']
price = '333'
#id_prod = 2126
id_prod = 'X4734166'
str_id_prod = 'products/'+str(id_prod)

print(str_id_prod)
data = {
    "regular_price": price
}
print(wcapi.get(str_id_prod).json())
print('111')
wcapi.put(str_id_prod, data)

print(wcapi.get("products/2126").json())'''