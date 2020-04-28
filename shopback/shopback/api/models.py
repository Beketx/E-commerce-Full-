from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return '{}'.format(self.name)
    def to_json(self):
        return{
            'id':self.id,
            'name':self.name
        }


class User(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    def __str__(self):
        return '{}'.format(self.username)

class Cart(models.Model):
    created_by = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    date = models.DateField(auto_now=True)
    subtotal = models.DecimalField(max_digits = 50, decimal_places=2, default=0.00)

    def __str__(self):
        return '{}'.format(self.created_by)




class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField(default='1')
    description = models.TextField(default='')
    # image = models.ImageField()
    count = models.IntegerField(default=0)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    cartitem = models.ForeignKey(Cart,default=1, on_delete=models.CASCADE,related_name='products')
    # cartitem = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.name)
    # def to_json(self):
    #     return{
    #         'id':self.id,
    #         'name':self.name,
    #         'price':self.price,
    #         'description':self.description,
    #         'count':self.count,
    #         'category_id':self.category_id.id
    #     }


# class Item(models.Model):
#     name = models.CharField(max_length=255)

class Feedback(models.Model):
    description = models.TextField(default='')
    products = models.ForeignKey(Product, on_delete = models.CASCADE, related_name='products')
    def __str__(self):
        return '{}'.format(self.products)



