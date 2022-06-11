from django.urls import path

from.import views

urlpatterns = [
    
    path('',views.show_data),
    path('student-data',views.student_data),
    path('show-data',views.backbtn)
]
