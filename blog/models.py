from django.db import models
from django.conf import settings
from django.utils import timezone

# Modèle représentant un article de blog


class Post(models.Model):
    """
    Modèle pour les articles du blog.
    """
    title = models.CharField(max_length=200, verbose_name="Titre")
    # Champ de texte pour le titre, limité à 200 caractères
    content = models.TextField(verbose_name="Contenu")
    # Champ de texte long pour le contenu de l'article
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name="Auteur"
    )
    # Lien vers l'utilisateur qui a créé l'article, suppression en cascade si l'utilisateur est supprimé
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Créé le")
    # Date de création, avec la date actuelle par défaut
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Mis à jour le")
    # Date de mise à jour automatique lors de modifications

    def __str__(self):
        """
        Retourne une représentation lisible de l'objet.
        """
        return self.title


# Modèle représentant un commentaire sur un article
class Comment(models.Model):
    """
    Modèle pour les commentaires associés à un article.
    """
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Post lié"
    )
    # Lien vers l'article auquel le commentaire est associé, suppression en cascade si l'article est supprimé
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name="Auteur"
    )
    # Lien vers l'utilisateur ayant posté le commentaire
    content = models.TextField(verbose_name="Contenu du commentaire")
    # Champ de texte long pour le contenu du commentaire
    created_at = models.DateTimeField(
        default=timezone.now, verbose_name="Créé le")
    # Date de création du commentaire, par défaut l'heure actuelle
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Mis à jour le")
    # Date de mise à jour automatique lors de modifications

    def __str__(self):
        """
        Retourne une représentation lisible du commentaire.
        """
        return f'Commentaire de {self.author.username} sur {self.post.title}'
