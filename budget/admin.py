from django.contrib import admin

# Register your models here.
from budget.models import Project, Branch, Vendor


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['project_title', 'project_budget']
    list_filter = ['project_title']
    save_on_top = True

class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch_name', 'branch_city_name']
    list_filter = ['branch_name']
    save_on_top = True

class VendorAdmin(admin.ModelAdmin):
    list_display = ['vendor_name', 'branch', 'project']
    list_filter = ['vendor_name']
    save_on_top = True








admin.site.register(Project, ProjectAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Vendor, VendorAdmin)
