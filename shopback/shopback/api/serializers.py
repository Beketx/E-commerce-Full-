from rest_framework import serializers
from api.models import*

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

class CategoryWithProductsSerializer(serializers.Serializer):
    pass
#     products = serializers.StringRelatedField(many=True,read_only=True)
#     class Meta:
#         model = Cart
#         fields = ['created_by','products']

class FeedbackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feedback
        fields = ['description','products']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['created_by','date','subtotal','order_item']

# class CartWithProductsSerializer(serializers.Serializer):
#     products = serializers.StringRelatedField(many=True,read_only=True)
#     class Meta:
#         model = Cart
#         fields = ['created_by','products']