from models.product import Product

class ProductRepository:
    @staticmethod
    def get_all():
        return Product.objects.all()
    
    @staticmethod
    def get_by_id(product_id):
        return Product.objects.get(id=product_id)
    
    @staticmethod
    def create(product_data):
        product = Product(**product_data)
        product.save()
        return product
    
    @staticmethod
    def update(product_id, product_data):
        product = Product.objects.get(id=product_id)
        product.update(**product_data)
        return Product.objects.get(id=product_id)
    
    @staticmethod
    def delete(product_id):
        product = Product.objects.get(id=product_id)
        product.delete()
        return True