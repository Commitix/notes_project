from django.db import models

# Create your models here.


class Kunde(models.Model):
    """
    meine Model Classe für Objecte zum abspeichern von DB Werten
    """

    # Kundennummer
    kd_num = models.IntegerField(max_length=20)
    kd_name = models.CharField(max_length=100)
    kd_ansprechpartner = models.CharField(max_length=100, null=True, blank=True)
    kd_plz = models.IntegerField(max_length=5)
    # einmalig
    created_at = models.DateTimeField(auto_now_add=True)
    # bei jedem Update des Objects
    updated_at = models.DateTimeField(auto_now=True)
