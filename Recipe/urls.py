
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


from Recipe import views

urlpatterns = [
    path('', views.home , name = "home"),
    path('recipe/', views.recipe , name = "recipe"),
    path('recipe_delete/<int:id>', views.recipe_delete , name = "recipe-delete"),
    path('update_recipe/<int:id>', views.update_recipe , name = "update-recipe"),
    path('recipe_delete_all/', views.recipe_delete_all , name = "recipe-delete-all"), 
    path('login/', views.login_view , name = "login"),
    path('register/', views.register , name = "register"), 
    path("logout/", views.logout_view, name= "logout"),
    path("students/", views.get_students, name= "students"),
    path("marks/<int:id>", views.marks, name= "marks"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


