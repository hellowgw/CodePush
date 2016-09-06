from django.db import models

# Create your models here.


class PushTarget(models.Model):
    target_name = models.CharField(max_length=32)
    target_cname = models.CharField(max_length=64)

    def __unicode__(self):
        return self.target_cname


class ProductionLine(models.Model):
    pl_name = models.CharField(max_length=32)
    pl_cname = models.CharField(max_length=64)
    target = models.ForeignKey('PushTarget')

    def __unicode__(self):
        return self.pl_cname


class Production(models.Model):
    p_name = models.CharField(max_length=32)
    p_cname = models.CharField(max_length=64)
    production_line = models.ForeignKey('ProductionLine')

    def __unicode__(self):
        return self.p_cname


class HostInfo(models.Model):
    ip = models.GenericIPAddressField()
    port = models.IntegerField(default=22)
    push_path = models.CharField(max_length=64)
    production = models.ManyToManyField('Production')

    def __unicode__(self):
        return self.ip

