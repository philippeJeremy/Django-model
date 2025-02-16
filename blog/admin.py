from django.contrib import admin
from .models import Post, Comment  # Importation des modèles Post et Comment

# Configuration de l'affichage du modèle Post dans l'interface d'administration Django


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Personnalisation de l'affichage du modèle Post dans l'admin Django.
    """
    list_display = ('title', 'author', 'created_at', 'updated_at')
    # Affiche ces champs dans la liste des articles
    search_fields = ('title', 'content')
    # Ajoute une barre de recherche sur le titre et le contenu des articles
    list_filter = ('created_at', 'author')
    # Permet de filtrer les articles par date de création et par auteur


# Configuration de l'affichage du modèle Comment dans l'administration Django
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Personnalisation de l'affichage du modèle Comment dans l'admin Django.
    """
    list_display = ('post', 'author', 'created_at', 'updated_at')
    # Affiche ces champs dans la liste des commentaires
    search_fields = ('content',)
    # Ajoute une barre de recherche sur le contenu des commentaires
    list_filter = ('created_at', 'author')
    # Permet de filtrer les commentaires par date de création et par auteur
