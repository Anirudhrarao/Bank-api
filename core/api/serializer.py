from rest_framework import serializers
from core.models import Currency,Category, Transactions
from django.contrib.auth.models import User

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Category
        fields = '__all__'
        
class WriteTransactionsSerializer(serializers.ModelSerializer):
    # currency = serializers.CharField(source='currency.name',read_only=True)
    # category = serializers.CharField(source='category.name',read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    currency = serializers.SlugRelatedField(slug_field="code",queryset=Currency.objects.all())
    class Meta:
        model = Transactions
        # fields = '__all__'
        exclude = ('id',)

    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        user = self.context['request'].user
        self.fields['category'].queryset = Category.objects.filter(user=user)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name')
        read_only_fields = fields

class ReadTransactionsSerializer(serializers.ModelSerializer):
    # currency = serializers.CharField(source='currency.name',read_only=True)
    # category = serializers.CharField(source='category.name',read_only=True)
    user = UserSerializer()
    currency = CurrencySerializer()
    category = CategorySerializer()
    class Meta:
        model = Transactions
        fields = ('id','amount','currency','date','desc','category','user')
        read_only_fields = fields