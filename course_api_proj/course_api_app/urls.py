from django.urls import path
from .views import *


# function based views
# urlpatterns = [
#     path('',course_view,name = 'course_view'),
#     path('course_detail_view/<int:pk>',course_detail_view,name = 'course_detail_view'),
#
# ]

# # class based views and mixins and generics can use below api's
urlpatterns = [
    path('', Course_View.as_view(), name='course_view'),
    path('course_detail_view/<int:pk>', Course_Detail_View.as_view(), name='course_detail_view'),

]

