"""
URL configuration for hrgen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hrgen import views 

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", views.IndexView.as_view()),
    path("generate", views.CreateDescView.as_view()),
    path("positions", views.PositionsView.as_view()),
    path("position/<int:pk>", views.PositionView.as_view(), name="position"),
    path("interview-select", views.InterviewSelectView.as_view(), name="interview-select"),
    path("interview-generate/<int:position_id>", views.InterviewView.as_view(), name="interview-generate"),
    path("summary", views.SummaryView.as_view(), name="summary")
]
