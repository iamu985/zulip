# Generated by Django 3.2.13 on 2022-06-17 17:39
import orjson
from django.db import migrations
from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.migrations.state import StateApps


def remove_custom_field_values_for_deleted_options(
    apps: StateApps, schema_editor: BaseDatabaseSchemaEditor
) -> None:
    SELECT_TYPE = 3
    CustomProfileField = apps.get_model("zerver", "CustomProfileField")
    CustomProfileFieldValue = apps.get_model("zerver", "CustomProfileFieldValue")

    select_type_fields = CustomProfileField.objects.filter(field_type=SELECT_TYPE)
    for field in select_type_fields:
        field_data = orjson.loads(field.field_data)
        current_options = list(field_data.keys())
        CustomProfileFieldValue.objects.filter(field=field).exclude(
            value__in=current_options
        ).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0396_remove_subscription_role"),
    ]

    operations = [
        migrations.RunPython(
            remove_custom_field_values_for_deleted_options,
            elidable=True,
        ),
    ]