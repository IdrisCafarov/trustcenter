from blog.models import *

from rest_framework import serializers






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
    class Meta:
        model = Order
        fields = '__all__'
