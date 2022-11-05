from django import forms

from netbox.forms import (
    NetBoxModelForm,
    NetBoxModelBulkEditForm,
    NetBoxModelCSVForm,
    NetBoxModelFilterSetForm,
)
from utilities.forms import (
    CommentField,
    CSVModelChoiceField,
    DynamicModelChoiceField,
    DynamicModelMultipleChoiceField,
    TagFilterField,
)

from ipam.models import Service

from netbox_data_flows.models import (
    Application,
    ApplicationRole,
)


__all__ = (
    "ApplicationForm",
    "ApplicationBulkEditForm",
    "ApplicationCSVForm",
    "ApplicationFilterForm",
)

#
# Object forms
#


class ApplicationForm(NetBoxModelForm):
    role = DynamicModelChoiceField(
        queryset=ApplicationRole.objects.all(), required=False
    )
    services = DynamicModelMultipleChoiceField(
        queryset=Service.objects.all(), required=False
    )
    comments = CommentField()

    fieldsets = (
        (
            "Application",
            (
                "name",
                "role",
                "description",
                "tags",
            ),
        ),
        ("Services", ("services",)),
    )

    class Meta:
        model = Application
        fields = (
            "name",
            "role",
            "description",
            "services",
            "comments",
            "tags",
        )


#
# Bulk forms
#


class ApplicationBulkEditForm(NetBoxModelBulkEditForm):
    model = Application

    description = forms.CharField(max_length=200, required=False)
    role = DynamicModelChoiceField(
        queryset=ApplicationRole.objects.all(), required=False
    )

    fieldsets = (
        (
            "Application",
            (
                "role",
                "description",
            ),
        ),
    )
    nullable_fields = (
        "role",
        "description",
    )


class ApplicationCSVForm(NetBoxModelCSVForm):
    role = CSVModelChoiceField(
        queryset=ApplicationRole.objects.all(),
        required=False,
        to_field_name="name",
        help_text="Role of the application",
    )

    class Meta:
        model = Application
        fields = (
            "name",
            "description",
            "role",
        )


#
# Filter forms
#


class ApplicationFilterForm(NetBoxModelFilterSetForm):
    model = Application
    tag = TagFilterField(model)

    role = forms.ModelMultipleChoiceField(
        queryset=ApplicationRole.objects.all(), required=False
    )
