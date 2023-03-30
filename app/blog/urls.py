from django.urls import path
from blog.views import *

urlpatterns = [
    path('',index,name="index"),
    path("blog/", BlogView.as_view({'get': 'list',}), name="blog"),
    path("popblog_tags/", PopTagAPIView.as_view(), name="popblog_tags"),
    path("blog/<pk>/", BlogDetailView.as_view({'get': 'retrieve',}), name="blog_detail"),
    path("service/", ServiceView.as_view({'get': 'list',}), name="services"),
    path("service/<pk>/", ServiceDetailView.as_view({'get': 'retrieve',}), name="service_detail"),
    path("contact/", ContactView.as_view({'post': 'create',}), name="contact"),
    path("contact_about/", ContactAboutView.as_view({'get': 'list',}), name="contact_about"),
    path("about/", AboutView.as_view({'get': 'list',}), name="about"),
    path("achivement/", AchivementView.as_view({'get': 'list',}), name="achivement"),
    path("send_email/", send_email, name="send_email"),
    path("subscribe/", SubscribeView.as_view({'post': 'create',}), name="subscribe"),
    path("portfolio/", PortfolioView.as_view({'get': 'list',}), name="portfolio"),
    path("portfolio/<pk>/", PortfolioDetailView.as_view({'get': 'retrieve',}), name="portfolio_detail"),
    path("blog_search/", BlogSearchViewSet.as_view(), name="blog_search"),





]
