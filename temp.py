from woocommerce import API

wcapi = API(
    url="https://splitovik.ru",
    consumer_key="ck_b386c34cc21c495c288913d37a8ecde73ffcffaa",
    consumer_secret="cs_fba9bb4212f793e19e4dfca6f6bc65ca750bb293",
    wp_api=True,
    version="wc/v3"
)

print(wcapi.get("").json())
print()
print(wcapi.get("products").json())
print()
print(wcapi.get("products/2126").json())