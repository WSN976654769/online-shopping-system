from collections import defaultdict


class Cart:
    def __init__(self):
        self._line_items = defaultdict(int)

    def add_to_cart(self, item_code, qty):
        self._line_items[item_code] += qty

    def update(self, item_code, qty):
        self._line_items[item_code] = qty

    def remove(self, item_code):
        del self._line_items[item_code]

    def purchase_cart(self):
        """Normally purchasing the cart will do more"""
        self._line_items.clear()

    def checkout(self, inventory):
        cart_items = []
        total_cost = 0
        for i in self._line_items.items():
            item = inventory.get_item(i[0])
            cost = item.price * i[1]
            total_cost += cost
            cart_items.append((item, i[1], cost))

        table = {
            'items': cart_items,
            'total': total_cost
        }
        return table
