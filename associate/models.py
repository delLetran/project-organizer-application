from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import get_user_model

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.db.models.signals import pre_save
from django.db.models.signals import m2m_changed

USER = get_user_model()

class Associate(models.Model):
  class STATUS(models.TextChoices):
    ONHOLD = 'Waiting', 
    ACCEPTED = 'Accepted',
    DECLINED = 'Declined',
    DISSOCIATED = 'Dissociated'
  sender = models.ForeignKey(USER, verbose_name=_("sender"), related_name="sender", on_delete=models.DO_NOTHING, blank=True, null=True)
  receiver = models.ForeignKey(USER, verbose_name=_("receiver"), related_name="receiver", on_delete=models.DO_NOTHING)
  is_active = models.BooleanField(_("invitation active"), default=True)
  status = models.CharField(_("invite status"), max_length=50, choices=STATUS.choices, blank=True, null=True)

  def __str__(self):
    return f"{str(self.sender)} --> {str(self.receiver)}"

  class Meta:
    unique_together = [['sender', 'receiver']]
    db_table = ''
    managed = True
    verbose_name = 'Associate'
    verbose_name_plural = 'Associates'

  def accept_peer_invite(self):
    self.status = self.STATUS.ACCEPTED
    self.save()
    return self.status

  def decline_peer_invite(self):
    self.status = self.STATUS.DECLINED
    self.save()
    return self.status

  def cancel_peer_invite(self):
    self.status = self.STATUS.DISSOCIATED
    self.save()
    return 'Cancelled'

  def dissociate_peer(self):
    self.status = self.STATUS.DISSOCIATED
    self.save()
    return self.status

  # def cancel_peer_invite(self):
  #   self.delete()
  #   return self.status

@receiver(pre_save, sender=Associate)
def pre_save_associate(sender, instance, *args, **kwargs):
  _sender = instance.sender
  _receiver = instance.receiver
  _status = instance.status
  if _status=='Accepted' or _status=='Declined' or _status=='Dissociated':
    instance.is_active  = False #sender & receiver can't send another invite
  if _status=='Waiting':
    instance.is_active  = True


@receiver(post_save, sender=Associate)
def post_save_associate(sender, instance, created, *args, **kwargs):
  _sender = instance.sender
  _receiver = instance.receiver
  _status = instance.status
  if created:
    instance.status='Waiting' 
    instance.save()
  if not created:
    if _status=='Waiting':
      _sender.associates.remove(_receiver)
      _receiver.associates.remove(_sender)

    elif _status=='Accepted':
      _sender.associates.add(_receiver)
      _receiver.associates.add(_sender)

    elif _status=='Declined':
      _sender.associates.remove(_receiver)
      _receiver.associates.remove(_sender)
      instance.delete()

    elif _status=='Dissociated':
      _sender.associates.remove(_receiver)
      _receiver.associates.remove(_sender)
      instance.delete()


@receiver(m2m_changed, sender=USER.associates.through)
def user_associates_change(sender, instance, action, *args, **kwargs):
  if action == 'pre_add':
    qs = kwargs.get("model").objects.filter(pk__in=kwargs.get('pk_set'))

    