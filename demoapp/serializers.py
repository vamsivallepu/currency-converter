from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        # fields = "__all__"
        fields = ["title", "author", "price"]
        # exclude = ['title']
    
    def validate_price(self, value):
        if value<0:
            raise serializers.ValidationError("Price can't be negative")
        return value
    


# 10
# 8

# class BookSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=100)
#     author = serializers.CharField(max_length=100)
#     price = serializers.FloatField()

#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Book.objects.create(**validated_data)
    

