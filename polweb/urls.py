from django.urls import path
from .views import HomeView,Empowerment_detail, \
Emp_detail,Quotes_detail,Bill_detail,Project_detail,Proj_detail, About_detail, Bill_list


urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('about/', About_detail.as_view(), name='about'),
    path('bill&motion/', Bill_list.as_view(), name='bill'),
    path('bill&motion/<int:pk>/', Bill_detail.as_view(), name='bill-detail'),
    path('quotes/', Quotes_detail.as_view(), name='quotes'),
    path('project&achievements/', Proj_detail.as_view(), name='project'),
    path('project&achievements/<int:pk>/', Project_detail.as_view(), name='project-detail'),
    path('empowerment/', Emp_detail.as_view(), name='empowerment'),
    path('empowerment/<int:pk>/', Empowerment_detail.as_view(), name='empowerment-detail'),
]
