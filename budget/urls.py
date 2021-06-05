from django.urls import path
from django.views.generic import RedirectView

from budget.views import VendorsList, HomeView, VendorDetailView, TotalBudgetView, ContactView

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('list/', VendorsList.as_view()),
    path('vendor/<int:pk>/', VendorDetailView.as_view()),
    path('vendor/<int:pk>/budget/', TotalBudgetView.as_view()),
    path('', HomeView.as_view()),
    path('contact/', ContactView.as_view()),
    path('', RedirectView.as_view(url='vendor/')),

]
