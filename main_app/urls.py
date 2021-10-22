from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('jedis/', views.jedis_index, name='index'),
    path('jedis/<int:jedi_id>/', views.jedis_detail, name='detail'),
    path('jedis/create/', views.jediCreate.as_view(), name='jedis_create'),
    path('jedis/<int:pk>/update/', views.jediUpdate.as_view(), name='jedis_update'),
    path('jedis/<int:pk>/delete/', views.jediDelete.as_view(), name='jedis_delete'),
    path('jedis/<int:jedi_id>/add_training/', views.add_training, name='add_training'),
    path('jedis/<int:jedi_id>/assoc_weapon/<int:weapon_id>/', views.assoc_weapon, name='assoc_weapon'),


]