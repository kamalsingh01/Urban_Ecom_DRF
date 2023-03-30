#CUSTOM FIELD CREATION
# In this we manipulate or gather the data, prepare the data before the models save method.
# Each instance of order field's instance passes through here first then goes to save the data in DB

from django.db import models
from django.core import checks
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
    
    description = "Ordering field on a Unique field"

    #making unique_for_field available for whole class.
    def __init__(self, unique_for_field=None, *args, **kwargs):
        self.unique_for_field = unique_for_field
        super().__init__(*args, **kwargs)

    #for validating unique_for_field is included for order field.
    def check(self, **kwargs):
        return [
            *super().check(**kwargs),
            *self._check_for_field_attribute(**kwargs)
        ]
    def _check_for_field_attribute(self, **kwargs):
        if self.unique_for_field is None:
            return [
                checks.Error("OrderField must define a 'unique_for_field' attribute")
            ]
        elif self.unique_for_field not in [f.name for f in self.model._meta.get_fields()]:
            return [
                checks.Error("OrderField entered doesn't match an existing model field")
            ]
        return []
    
    #overriding models pre_save method
    #whatever instance we create for order field, first passes through this pre_save method
    def pre_save(self, model_instance, add):
        print("Hello")
        print(model_instance)

        if getattr(model_instance, self.attname) is None:
            qs = self.model.objects.all()
            try:
                query = {self.unique_for_field : getattr(model_instance, self.unique_for_field)}
                print(query)
                qs = qs.filter(**query)
                last_item = qs.latest(self.attname)
                #print(self.attname)  #ORDER
                value = last_item.order +1
            
            except ObjectDoesNotExist:
                value=1
            return value
        else:
            return super().pre_save(model_instance,add)