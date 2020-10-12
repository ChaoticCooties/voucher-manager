from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Voucher(models.Model):
    v_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    percent_off = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True, null=True)
    flat_off = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], blank=True, null=True)
    remaining = models.PositiveSmallIntegerField(
        default=3, validators=[MaxValueValidator(3)])
    created_at = models.DateTimeField(auto_now_add=True)
