from django.urls import path

from apprecipebox import views

urlpatterns = [
    path('', views.index, name='homepage'),
    # path('recipeadd/', views.add),
    # path('authoradd/', views.authoradd),
    path('recipe/<int:id>', views.recipe_detail),
    path('author/<int:id>', views.author_detail)
]
