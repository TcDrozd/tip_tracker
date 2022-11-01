from django.db import models

# Create your models here.


class Tip_Type(models.Model):
    """ The type of tip to be entered """
    TipType = models.TextChoices('Cash', 'Credit Card')
    name = models.CharField(max_length=60)
    tip = models.CharField(blank=True,
                           choices = TipType.choices,
                           max_length=10,
                           )
    class Meta:
        verbose_name_plural = 'tip types'

class Tip_Entry(models.Model):
    """ An entry into the tip logger of type tip_type """
    tip_type = models.ForeignKey(
        Tip_Type,
        on_delete=models.CASCADE,
        default=0
    )
    amt = models.FloatField()
    date_added = models.DateField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'tip entries'

    def __float__(self):
        """ Return a string representation of the model. """
        return self.amt