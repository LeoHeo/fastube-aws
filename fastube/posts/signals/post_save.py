from django.db.models.signals import post_save
from django.dispatch import receiver

from posts.models import Post


@receiver(post_save, sender=Post)
def post_save_post(sender, instance, created, **kwargs):
    if not instance.hash_id:
        from hashids import Hashids
        hash_ids = Hashids(salt="rksksk", min_length=8)

        instance.hash_id = hash_ids.encode(instance.id)
        instance.save()
