from django.db import models
from django.urls import reverse

class Weapon(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
# Create your models here.
class Jedi(models.Model):
    name = models.CharField(max_length=100)
    rank = models.CharField(max_length=100)
    age = models.IntegerField()
    weapons = models.ManyToManyField(Weapon)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'jedi_id': self.id})



Training_Type = (('F','Force'), ('L','Lightsaber'), ('M','Mind Tricks'))

class Training(models.Model):
    date = models.DateField('Training date')
    type = models.CharField(max_length=1,
    choices=Training_Type,
    default=Training_Type[0][0]
    )
    jedi = models.ForeignKey(Jedi, on_delete=models.CASCADE)


    def __str__(self):
        return f"Trained {self.get_type_display()} on {self.date}"
    
    class Meta:
        ordering = ['-date']