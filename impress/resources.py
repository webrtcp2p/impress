from import_export import resources
from .models import Impress

class PersonResource(resources.ModelResource):
    class Meta:
        model = Impress
