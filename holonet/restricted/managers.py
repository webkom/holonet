from django.db.models import Manager


class RestrictedMappingManager(Manager):

    def active(self):
        return self.get_queryset().filter(is_used=False)
