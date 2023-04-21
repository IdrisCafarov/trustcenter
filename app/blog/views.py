from rest_framework import generics
from rest_framework.response import Response
from blog.serializers import *
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework import viewsets
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.decorators import api_view
from celery import shared_task
from django.core.mail import EmailMessage
from rest_framework import filters




def index(request):
    return redirect('admin/')



class BlogView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = BlogSerializer




class BlogDetailView(viewsets.ModelViewSet):
    queryset = Blog.objects.all()

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = BlogSerializer




    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        tags = instance.tag.all()
        print(tags)
        blogs = Blog.objects.filter(tag__in=tags).exclude(id=instance.id).distinct()
        serializer1 = self.get_serializer(instance)
        serializer2 = BlogSerializer(blogs, many=True)
        data = {'blog': serializer1.data, 'similar_blogs': serializer2.data}
        return Response(data)




    def perform_create(self, serializer):
        return serializer.save()




class PopTagAPIView(APIView):
    def get(self, request):
        blog = Blog.get_most_clicked()
        tag = Tag.objects.all()
        serializer1 = BlogSerializer(blog)
        serializer2 = TagSerializer(tag, many=True)
        data = {'popular_blog': serializer1.data, 'tags': serializer2.data}
        return Response(data)


class ServiceView(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ServiceSerializer



class ServiceDetailView(viewsets.ModelViewSet):
    queryset = Service.objects.all()

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ServiceDetailSerializer




    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        services = Service.objects.filter(id=instance.id)
        service = services.first()

        portfolios = Portfolio.objects.filter(service__in=services)
        blogs = Blog.objects.filter(service=service)

        serializer1 = self.get_serializer(instance)
        serializer2 = PortfolioSerializer(portfolios, many=True)
        serializer3 = BlogSerializer(blogs, many=True, context={'request': request})
        data = {'service': serializer1.data, 'portfolio': serializer2.data, 'related_blogs':serializer3.data}
        return Response(data)



class ContactView(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = ContactSerializer


class ContactAboutView(viewsets.ModelViewSet):
    queryset = ContactSettings.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class  = ContactAboutSerializer


class AboutView(generics.ListAPIView):
    def get(self, request):
        # about = Blog.get_most_clicked()
        about = About.objects.all().first()
        # serializer1 = BlogSerializer(blog)
        serializer2 = AboutSerializer(about)
        data = {'about': serializer2.data}
        return Response(data)




class AchivementView(viewsets.ModelViewSet):
    queryset = PortfolioCategory.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PorfolioCategorySerializer


class SubscribeView(viewsets.ModelViewSet):
    queryset = Subscribe.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = SubscribeSerializer


class PortfolioView(viewsets.ModelViewSet):

    queryset = Portfolio.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PortfolioSerializer



class PortfolioDetailView(viewsets.ModelViewSet):
    queryset = Portfolio.objects.all()

    parser_classes = (MultiPartParser, FormParser)
    serializer_class = PortfolioDetailSerializer



    def retrieve(self, request, *args, **kwargs):

        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)



class BlogSearchViewSet(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title',]

class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = OrderSerializer

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            field_values = serializer.validated_data['professionalNeed']
            # Process the list of field values here
            return Response({'success': True})
        else:
            return Response(serializer.errors, status=400)


############## send mail #########################

@shared_task
def send_email_task(subject, message, html_content=None):
    subs = Subscribe.objects.all()
    emails = [i.email for i in subs]
    if html_content:
        email = EmailMultiAlternatives(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=emails
        )
        email.attach_alternative(html_content, 'text/html')
    else:
        email = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.EMAIL_HOST_USER,
            to=emails
        )

    email.send()

@api_view(['POST'])
def send_email(request):
    subject = request.data['subject']
    message = request.data['message']
    # recipient_list = request.data['recipient_list']
    html_content = request.data.get('html_content')

    send_email_task.delay(subject, message, html_content)

    return Response({'message': 'Email sent successfully'})