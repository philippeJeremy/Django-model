from django import forms
from .models import Post, Comment  # Importation des modèles Post et Comment

# Formulaire pour la création et la modification d'un article (Post)


class PostForm(forms.ModelForm):
    """
    Formulaire permettant de créer ou modifier un article.
    """
    class Meta:
        model = Post  # Associe le formulaire au modèle Post
        fields = ['title', 'content']  # Champs inclus dans le formulaire


# Formulaire pour la création d'un commentaire
class CommentForm(forms.ModelForm):
    """
    Formulaire permettant d'ajouter un commentaire à un article.
    """
    class Meta:
        model = Comment  # Associe le formulaire au modèle Comment
        # Champs inclus dans le formulaire (uniquement le contenu du commentaire)
        fields = ['content']
