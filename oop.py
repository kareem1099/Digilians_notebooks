class product:
    def __init__(self,name,price,quantatiy=1000):
        self.name=name
        self.price=price
        self.quantatiy=quantatiy
    def restock(product,quantaty):
        product.quantatiy+=quantaty
        print(f"restock {product.name} with {quantaty} so new quantity is {product.quantatiy}")
    
    def sell(product,quantaty):
        if quantaty<product.quantatiy:
            product.quantatiy-=quantaty
            print(f"sold {quantaty} {product.name}. remaining is {product.quantatiy} and amount is {quantaty*product.price}")
        else:
            print(f"NO enough {product.name}s")
laptops=product(name="laptop",price=8000,quantatiy=1000)
product.sell(laptops,10000)
product.restock(laptops,20)