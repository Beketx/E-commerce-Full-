from rest_framework import serializers
from api.models import Product,Category,Feedback,Cart,User

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name','count','description','image','price','category_id']

class CategorySerailizer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=300)
    def create(self,validated_data):
        category = Category.objects.create(name=validated_data['name'])
        return category
    def update(self,instance,validated_data):
        instance.name = validated_data.get('name')
        instance.save()
        return instance

class CategoryWithProducsSerializer(serializers.Serializer):
    pass

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['description','products']
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['created_by','date','subtotal','order_item','Users']