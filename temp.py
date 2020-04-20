from woocommerce import API

wcapi = API(
    url="https://splitovik.ru",
    consumer_key="ck_b386c34cc21c495c288913d37a8ecde73ffcffaa",
    consumer_secret="cs_fba9bb4212f793e19e4dfca6f6bc65ca750bb293",
    wp_api=True,
    version="wc/v3"
)

#print(wcapi.get("products").json())
#print()

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

print(wcapi.get("products/2126").json())
