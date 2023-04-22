from blog.models import *

from rest_framework import serializers
import json







class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    tag = TagSerializer(many=True)
    class Meta:
        model = Blog
        fields = '__all__'


class popSerializer(serializers.ModelSerializer):
    tags = TagSerializer()
    tag = TagSerializer(many=True)
    class Meta:
        model = Blog
        fields = '__all__'


class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portfolio
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    # blog = BlogSerializer(many=True)
    class Meta:
        model = Service
        fields  = '__all__'


class ServiceDetailSerializer(serializers.ModelSerializer):
    # blog = BlogSerializer(many=True)
    class Meta:
        model = Service
        fields  = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ContactAboutEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailContact
        fields = '__all__'

class ContactAboutNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneContact
        fields = '__all__'


class ContactAboutSerializer(serializers.ModelSerializer):
    email  = ContactAboutEmailSerializer(many=True)
    number = ContactAboutNumberSerializer(many=True)
    class Meta:
        model = ContactSettings
        fields = '__all__'



class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SectionAbout
        fields = '__all__'

class AboutSerializer(serializers.ModelSerializer):
    section = AboutSectionSerializer(many=True)
    class Meta:
        model = About
        fields = '__all__'

############################################################################



class PorfolioCategorySerializer(serializers.ModelSerializer):
    portfolio_count = serializers.SerializerMethodField()

    def get_portfolio_count(self, obj):
        return obj.portfolio.count()
    class Meta:
        model = PortfolioCategory
        fields = ['id','name','portfolio_count']




class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = '__all__'


class PortfolioImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortfolioImages
        fields = '__all__'



class PortfolioSerializer(serializers.ModelSerializer):
    # image = PortfolioImagesSerializer(many=True)
    class Meta:
        model = Portfolio
        fields = ['id','name','main_image','video']



class PortfolioDetailSerializer(serializers.ModelSerializer):
    image = PortfolioImagesSerializer(many=True)
    class Meta:
        model = Portfolio
        fields = '__all__'




class OrderSerializer(serializers.ModelSerializer):

    # professionalNeed = serializers.ListField(
    #     child=serializers.CharField()
    # )

    class Meta:
        model = Order
        fields = '__all__'


    # def to_internal_value(self, data):
    #     if 'professionalNeed' in data:
    #         input_data = data['professionalNeed']
    #         if isinstance(input_data, str):
    #             try:
    #                 # Attempt to deserialize the input data from JSON
    #                 deserialized_data = json.loads(input_data)
    #             except json.JSONDecodeError:
    #                 raise serializers.ValidationError('Invalid input format')
    #         else:
    #             # If the input data is already a list, use it directly
    #             deserialized_data = input_data
    #         data['professionalNeed'] = deserialized_data
    #     return super().to_internal_value(data)

    # def create(self, validated_data):
    #     field_values = validated_data.pop('professionalNeed')
    #     professional_need_str = ','.join(field_values)
    #     order = Order.objects.create(professionalNeed=professional_need_str, **validated_data)
    #     return order


