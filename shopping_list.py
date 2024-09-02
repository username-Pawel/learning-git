shops = {
    "piekarnia": ["chleb", "pączek", "bułki"],
    "warzywniak": ["marchew", "seler", "rukola"]
}

total_products = 0

for shop, products in shops.items():
    shop_title = shop.title() 
    print(f"Idę do {shop_title} i kupuję tam:")
    for product in products:
        product_title = product.title()  
        print(f" - {product_title}")
        total_products += 1

print(f"W sumie kupuję {total_products} produktów.")