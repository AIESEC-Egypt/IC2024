from django.db import models
from django.utils import timezone


SIZE_OPTIONS = [
  (None ,'------'),
  ('10-50 Employee', '10-50 Employee'),
  ('50-100 Emmployee', '50-100 Emmployee'),
  ('100-300 Employee', '100-300 Employee'),
  ('300+ Employee', '300+ Employee'),

]

class Partner(models.Model):
  created_at = models.DateTimeField(default=timezone.now, blank=True)

  company_name = models.CharField(max_length=200, null=True, blank=True)
  company_field = models.CharField(max_length=200, null=True, blank=True)
  company_size = models.CharField(max_length=200, null=True, blank=True, choices=SIZE_OPTIONS)
  linkedin = models.CharField(max_length=200, null=True, blank=True)
  website = models.CharField(max_length=200, null=True, blank=True)
  reason_for_interest = models.CharField(max_length=200, null=True, blank=True)
  person_name = models.CharField(max_length=200, null=True, blank=True)
  person_email = models.EmailField(max_length=200, null=True, blank=True)
  person_mobile = models.CharField(max_length=200, null=True, blank=True)
  person_position = models.CharField(max_length=200, null=True, blank=True)

  def __str__(self):
    return self.company_name