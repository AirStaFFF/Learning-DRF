from django.urls import path

from .views import (JobOfferListApiView,
                    JobOfferDetailsApiView,
                    CompanyListApiView,
                    CompanyDetailsApiView)

urlpatterns = [
    path('joboffers/', JobOfferListApiView.as_view(), name='joboffer-list'),
    path('joboffers/<int:pk>', JobOfferDetailsApiView.as_view(), name='joboffer-delail'),
    path('companies/', CompanyListApiView.as_view(), name="company-list"),
    path('companies/<int:pk>', CompanyDetailsApiView.as_view(), name="company-detail"),

]
