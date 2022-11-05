from django.db.models import Count

from netbox.views import generic

from netbox_data_flows import filtersets, forms, models, tables


__all__ = (
    "ApplicationRoleView",
    "ApplicationRoleListView",
    "ApplicationRoleEditView",
    "ApplicationRoleDeleteView",
    "ApplicationRoleBulkImportView",
    "ApplicationRoleBulkEditView",
    "ApplicationRoleBulkDeleteView",
)


class ApplicationRoleView(generic.ObjectView):
    queryset = models.ApplicationRole.objects.all()

    def get_extra_context(self, request, instance):
        applications_table = tables.ApplicationTable(
            instance.applications.all()
        )
        applications_table.configure(request)

        return {
            "applications_table": applications_table,
        }


class ApplicationRoleListView(generic.ObjectListView):
    queryset = models.ApplicationRole.objects.annotate(
        application_count=Count("applications"),
    )
    table = tables.ApplicationRoleTable
    filterset = filtersets.ApplicationRoleFilterSet


class ApplicationRoleEditView(generic.ObjectEditView):
    queryset = models.ApplicationRole.objects.all()
    form = forms.ApplicationRoleForm


class ApplicationRoleDeleteView(generic.ObjectDeleteView):
    queryset = models.ApplicationRole.objects.all()


class ApplicationRoleBulkImportView(generic.BulkImportView):
    queryset = models.ApplicationRole.objects.all()
    model_form = forms.ApplicationRoleCSVForm
    table = tables.ApplicationRoleTable


class ApplicationRoleBulkEditView(generic.BulkEditView):
    queryset = models.ApplicationRole.objects.all()
    filterset = filtersets.ApplicationRoleFilterSet
    table = tables.ApplicationRoleTable
    form = forms.ApplicationRoleBulkEditForm


class ApplicationRoleBulkDeleteView(generic.BulkDeleteView):
    queryset = models.ApplicationRole.objects.all()
    filterset = filtersets.ApplicationRoleFilterSet
    table = tables.ApplicationRoleTable
