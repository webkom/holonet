# -*- coding: utf8 -*-

from django.db import models


class Domain(models.Model):

    domain = models.CharField(max_length=200, unique=True, db_index=True)

    def __str__(self):
        return self.domain

    def save(self, *args, **kwargs):
        self.domain = self.domain.lower()
        return super(Domain, self).save(*args, **kwargs)

    @classmethod
    def lookup_domain(cls, domain_name):
        try:
            domain = cls.objects.get(domain=domain_name.lower())
            return domain
        except cls.DoesNotExist:
            pass

        return None

    @classmethod
    def list_domains(cls):
        domains = cls.objects.all()
        return list(map(lambda domain: str(domain), domains))
