from django.urls import path

from apprecipebox import views

urlpatterns = [
    path('', views.index, name='homepage'),
    path('error/', views.errorview, name='errorpage'),
    path('addauthor/', views.add_author),
    path('addrecipe/', views.add_recipe),
    path('recipe/<int:id>', views.recipe_detail),
    path('recipe/edit/<int:pk>', views.UpdateRecipeView.as_view()),
    path('recipe/favorite/<int:id>', views.add_to_favorite_view),
    path('author/<int:id>', views.author_detail),
    path('login/', views.loginview),
    path('logout/', views.logoutview)
]
