def sort_products_by(py, sort_name):
    py.get('select.product_sort_container').select_by_text(sort_name)


def get_item_names(py):
    item_names = []
    for item in py.find(".inventory_item_name"):
        item_names.append(item.text())
    return item_names


def get_item_prices(py):
    item_prices = []
    for item in py.find(".inventory_item_price"):
        item_prices.append(float(item.text().strip('$')))
    return item_prices