from django.views.generic import ListView, DetailView, UpdateView, CreateView, TemplateView, DeleteView
from .models import Vendor, Project


class HomeView(TemplateView):
    """This is the home page of project app"""

    template_name = "budget/home.html"


class VendorsList(ListView):
    """In this we are showing all Vendors List and also add vendor related projects ,
    Branch , Projects budget and City """

    model = Vendor
    template_name = "budget/vendor_list.html"


class VendorDetailView(DetailView):
    """In this deetail page we are showing vendor details"""

    model = Vendor


class TotalBudgetView(TemplateView):
    """In this page we are showing projects budgets and vendors detail those will help in
    the calculation for total budget of the vendor, also showing
    total budgets of vendor's all projects"""

    model = Project
    template_name = "budget/budget.html"

    def get_context_data(self, **kwargs):
        context = super(TotalBudgetView, self).get_context_data(**kwargs)
        id = self.kwargs['pk']
        vendor = Vendor.objects.get(id=id)
        vendors = Vendor.objects.filter(vendor_name=vendor.vendor_name)
        context['vendors'] = Vendor.objects.filter(vendor_name=vendor.vendor_name)
        budget_list = [x.project.project_budget for x in vendors]
        context['total_budget'] = sum(budget_list)
        return context


class ContactView(TemplateView):
    template_name = "budget/contact.html"
