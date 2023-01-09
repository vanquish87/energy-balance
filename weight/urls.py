from django.urls import path
from . import views


urlpatterns = [
    path('create-entry/', views.create_entry, name='create-entry'),
    path('import-csv/', views.import_csv, name='import-csv'),
]