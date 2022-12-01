from store.models import Product
from decimal import Decimal

class Basket():
    
    def __init__(self, request):
        self.session = request.session
        # 'skey' = cookie for session key
        basket = self.session.get('skey')

        # checks wheter user has an active session or not
        if 'skey' not in request.session:
            # generate session information through dict
            basket = self.session['skey'] = {}

        self.basket = basket


    # add item to basket for current session
    def add(self, product, qty):
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'price': str(product.price), 'qty': qty}
        else:
            self.basket[product_id]['qty'] = qty

        self.save()


    # delete item from basket for current session
    def delete(self, product):
        product_id = str(product)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()


    # update item from basket for current session
    def update(self, product, qty):
        product_id = str(product)
        if product_id in self.basket:
            self.basket[product_id]['qty'] = qty

        self.save()


    # let django know that session has been modified
    def save(self):
        self.session.modified = True


    def get_total_price(self):
        return sum(Decimal(item['price']) * item['qty'] for item in self.basket.values())


    # return products based on product_id from the session data
    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.products.filter(id__in=product_ids)
        
        basket = self.basket.copy()
        # iterate through products from db, then add data to the basket
        for product in products:
            basket[str(product.id)]['product'] = product

        # compute the total price for every item
        for item in basket.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['qty']
            yield item


    # count the items
    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())