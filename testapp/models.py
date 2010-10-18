from django.db import models


class Shirt(models.Model):
    name = models.CharField(max_length=80)
    
    def __unicode__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=80)

    def __unicode__(self):
        return self.name


class ShirtColorPrice(models.Model):
    shirt = models.ForeignKey(Shirt)
    color = models.ForeignKey(Color)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    
    def __unicode__(self):
        # return u"Price for %s %s is %s" % (self.color, self.shirt, self.price)
        return u"ShirtColorPrice"
    