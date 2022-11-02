from django.db import models

# Create your models here.

TIP_TYPE = (
    ('Cash', 'cash'),
    ('CC', 'credit card'),
)
class Tip_Type(models.Model):
    """ The type of tip to be entered """
    #name = models.CharField(max_length=30)
    type = models.CharField(
        choices=TIP_TYPE,
        default='Cash',
        max_length=15
    )
    class Meta:
        verbose_name_plural = 'tip types'
    def __str__(self):
        """ Returns a string representation of the model """
        return self.type

class Tip_Entry(models.Model):
    """ An entry into the tip logger of type tip_type """
    #name = models.FloatField(default=0)
    type = models.ForeignKey(
        Tip_Type,
        on_delete=models.CASCADE,
        related_name='tiptype'
    )
    tip = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'tip entries'