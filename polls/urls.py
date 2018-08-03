from django.urls import path

from . import views

urlpatterns = [
    path('listing/', views.listing, name='listing'),
    path('breadcrumb/', views.breadcrumb, name='breadcrumb'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
