"""gnuhealth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('health.urls')),
    path('health-account/', include('health_account.urls')),
    path('health-account-invoice/', include('health_account_invoice.urls')),
    path('health-account-invoice-stock/', include('health_account_invoice_stock.urls')),
    path('health-account-product/', include('health_account_product.urls')),
    path('health-archives/', include('health_archives.urls')),
    path('health-caldav/', include('health_caldav.urls')),
    path('health-calendar/', include('health_calendar.urls')),
    path('health-company/', include('health_company.urls')),
    path('health-country/', include('health_country.urls')),
    path('health-crypto/', include('health_crypto.urls')),
    path('health-crypto-lab/', include('health_crypto_lab.urls')),
    path('health-currency/', include('health_currency.urls')),
    path('health-disability/', include('health_disability.urls')),
    path('health-ems/', include('health_ems.urls')),
    path('health-federation/', include('health_federation.urls')),
]
