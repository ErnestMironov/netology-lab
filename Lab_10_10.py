def get_user_input():
    products = {}
    while True:
        product_name = input("Введите название товара (или 'стоп' для завершения): ")
        if product_name.lower() == 'стоп':
            break
        products[product_name] = {}
        while True:
            store_name = input(f"Введите название магазина для {product_name} (или 'стоп' для завершения): ")
            if store_name.lower() == 'стоп':
                break
            price = float(input(f"Введите цену для {product_name} в магазине {store_name}: "))
            products[product_name][store_name] = price
    return products

def calculate_savings(products):
    stores_total = {}
    for product, stores in products.items():
        for store, price in stores.items():
            if store not in stores_total:
                stores_total[store] = 0
            stores_total[store] += price

    cheapest_store = min(stores_total, key=stores_total.get)
    most_expensive_store = max(stores_total, key=stores_total.get)
    savings = stores_total[most_expensive_store] - stores_total[cheapest_store]

    return cheapest_store, most_expensive_store, savings, stores_total

def main():
    user_products = get_user_input()
    cheapest_store, most_expensive_store, savings, stores_total = calculate_savings(user_products)

    print(f"Общая стоимость покупок в каждом магазине: {stores_total}")
    print(f"Самый дешевый магазин: {cheapest_store}, Самый дорогой магазин: {most_expensive_store}")
    print(f"Максимальная экономия: {savings} руб.")

if __name__ == "__main__":
    main()
