from django.core import checks
from django.core.exceptions import ObjectDoesNotExist
from django.db import models


class OrderField(models.PositiveIntegerField):
    description = "Ordering Field For Unique Products"

    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_unique_for_field(**kwargs),
        ]

    def _check_unique_for_field(self, **kwargs):
        field_object = self.model._meta.get_fields()
        field_list = []

        for obj in field_object:
            field_list.append(obj.name)

        if self.unique_for_field is None:
            return [
                checks.ERROR(
                    "OrderField must have a unique_for_field",
                    obj=self,
                    id='product.E001',
                )
            ]
        elif self.unique_for_field not in field_list:
            return [
                checks.ERROR(
                    "unique_for_field not found",
                    obj=self,
                    id='product.E002',
                )
            ]
        else:
            return []

    def pre_save(self, model_instance, add):

        if getattr(model_instance, self.attname) is None:
            try:
                all_pl = self.model.objects.all()
                filter_query = {
                    self.unique_for_field: getattr(model_instance, self.unique_for_field),
                }
                filtered_pl = all_pl.filter(**filter_query)
                last_item = filtered_pl.latest(self.attname)
                # value = getattr(last_item, self.attname) + 1
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 1

            return value

        else:
            return getattr(model_instance, self.attname)
