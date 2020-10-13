from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError


class Voucher(models.Model):
    """
    Voucher model. Includes code, name of voucher, percent/flat off, remaining uses, and creation date.
    A clean model and save model is also included to ensure that the discount is an exclusive type
    (percentage/flat).
    """

    code = models.CharField(max_length=50, unique=True, primary_key=True)
    name = models.CharField(max_length=100)

    # One and only one can exist per voucher
    percent_off = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)], blank=True, null=True)
    flat_off = models.PositiveIntegerField(
        validators=[MinValueValidator(1)], blank=True, null=True)

    # Below fields are automatically generated
    remaining = models.PositiveSmallIntegerField(
        default=3, validators=[MaxValueValidator(3)])
    created_at = models.DateTimeField(auto_now_add=True)

    # Integrity check to ensure percent_off and flat_off only exists one at a time
    def clean(self):
        # A voucher can only have a percent off or only a flat off
        if not self.percent_off and not self.flat_off:
            raise ValidationError(
                'A flat or percentage discount is required by the voucher.')
        if self.percent_off and self.flat_off:
            raise ValidationError(
                'Voucher can only be percentage based or flat rate based but not both.'
            )

    # Override save call to include custom clean validation

    def save(self, **kwargs):
        self.clean()
        return super(Voucher, self).save(**kwargs)
