from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
# Pour envoie mail Reservation
from reservations.models import Reservation



@receiver(post_save, sender=Reservation)
def envoyer_email_reservation(sender, instance, created, **kwargs):
    if created:  # Vérifie que c'est une nouvelle réservation
        # Préparer les détails de la réservation
        sujet = f"Nouvelle réservation pour {instance.location.name}"
        message = (
            f"Bonjour Admin,\n\n"
            f"Une nouvelle réservation a été effectuée. Voici les détails :\n\n"
            f" - Emplacement réservé : {instance.location.name}\n"
            f" - Description : {instance.location.description or 'N/A'}\n"
            f" - Dates : du {instance.start_date} au {instance.end_date}\n\n"
            f"Détails du client :\n"
            f" - Nom complet : {instance.user.first_name} {instance.user.last_name}\n"
            f" - Adresse e-mail : {instance.user.email}\n"
        )
        
        # Ajouter un champ phone si présent dans le modèle User
        if hasattr(instance.user, 'phone'):  # Vérifie si le champ phone existe
            message += f" - Téléphone : {instance.user.phone}\n"

        message += "\nMerci de confirmer ou de prendre les mesures nécessaires.\n\nCordialement,\nL'équipe."

        # Envoyer l'e-mail à l'administrateur
        send_mail(
            sujet,
            message,
            settings.EMAIL_HOST_USER,  # Adresse de l'expéditeur depuis le .env
            ['jeremy561000@gmail.com'],  # Remplacez par l'adresse de l'admin
            fail_silently=False,  # Active les erreurs visibles
        )

# A ajouté dans l'app pour recupere le signal de 
# from reservations.models import Reservation ou autre app 
def ready(self):
        import email_send.signals