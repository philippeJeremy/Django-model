from . import views
from django.urls import path

# Espace de noms pour éviter les conflits avec d'autres applications Django
app_name = "blog"

urlpatterns = [
    path('post_list/', views.PostListView.as_view(), name="post_list"),
    # Affiche la liste de tous les articles du blog

    path('create/', views.CreatePostView.as_view(), name='post_create'),
    # Formulaire pour créer un nouvel article

    path('<int:pk>/detail/', views.DetailPostView.as_view(), name='post_detail'),
    # Affiche les détails d'un article spécifique, identifié par son ID (pk)

    path('<int:pk>/edit/', views.UpdatePostView.as_view(), name='post_edit'),
    # Permet de modifier un article existant

    path('<int:pk>/comment/', views.CreateCommentPostViaw.as_view(),
        name='post_comment_form'),
    # Permet d'ajouter un commentaire à un article

    path('<int:pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),
    # Supprime un article spécifique

    path('<int:pk>/comment_edit/',
        views.UpdateCommentView.as_view(), name='comment_edit'),
    # Modifie un commentaire spécifique

    path('<int:pk>/comment_delete/',
        views.DeleteCommentView.as_view(), name='comment_delete'),
    # Supprime un commentaire spécifique
]
