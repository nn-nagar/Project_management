from django.db import models


# Create your models here.


class Project(models.Model):
    project_title = models.CharField(max_length=600)
    project_budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.project_title


class Branch(models.Model):
    branch_name = models.CharField(max_length=600)
    branch_city_name = models.CharField(max_length=600)

    def __str__(self):
        return self.branch_name


class Vendor(models.Model):
    vendor_name = models.CharField(max_length=600)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name="vendor_branch", verbose_name="vendor_branch")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name = "vendor_project", verbose_name="vendor_project")

    def __str__(self):
        return self.vendor_name
