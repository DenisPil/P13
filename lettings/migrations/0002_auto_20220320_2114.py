from django.apps import apps as global_apps
from django.db import migrations


def duplicate_table(apps, schema_editor):

    try:
        Adress = apps.get_model("oc_lettings_site", "Address")
    except LookupError:
        return
    Adress = apps.get_model("oc_lettings_site", "Address")
    Letting = apps.get_model("oc_lettings_site", "Letting")
    NewAdress = apps.get_model("lettings", "Address")
    NewLettings = apps.get_model("lettings", "Letting")

    for address in Adress.objects.all():
        address_new = NewAdress(
            number=address.number,
            street=address.street,
            city=address.city,
            state=address.state,
            zip_code=address.zip_code,
            country_iso_code=address.country_iso_code,)
        address_new.save()
        
        for letting in Letting.objects.filter(address=address):
            letting_new = NewLettings(title=letting.title, address=address_new)
            letting_new.save()


class Migration(migrations.Migration):


    dependencies = [("lettings", "0001_initial")]

    operations = [migrations.RunPython(duplicate_table)]

    if global_apps.is_installed("oc_lettings_site"):
        dependencies.append(("oc_lettings_site", "0001_initial"))
