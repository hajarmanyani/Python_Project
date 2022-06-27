from django.db import models
from Auteur.models import Auteur
# Create your models here.
class product(models.Model):
    id=models.AutoField(primary_key=1)
    nom=models.CharField(max_length=20)
    description=models.CharField(max_length=200)
    prix=models.IntegerField()
<<<<<<< HEAD
    ecrivain=models.CharField (max_length=50)
=======
    ecrivain=models.CharField (max_length=50,default="Book author")
>>>>>>> 8be79b34c5469a9341f0101d2a141bbadde9eb1b
    auteur= models.ForeignKey(Auteur, on_delete=models.CASCADE, default="")
    image=models.FileField(upload_to="static/images",default=" ")
    def _str_(self):
      return self.nom
