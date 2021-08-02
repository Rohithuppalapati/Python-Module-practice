from shopp.shopping_cart import buy_cart
from shopp.billing_cart import shop_add,shop_divide

if __name__ == '__main__':
    cart=buy_cart('medicines','biscuits')
    print(cart)
    bill=shop_add(1050,400)
    print(bill)
    discount=shop_divide(bill,10)
    print(discount)
    final_bill=bill-discount
    print(final_bill)

