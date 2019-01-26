from django.urls import path
from front_end.views import (PublicationPageView, ProfPageView,
                             PhdPageView, MScPageView,
                             BScPageView, ContactPageView, HomepagePageView, ActivitiesPageView,
                             Nano_assemblyPageView, NanofabricationPageView, iod_devPageView,
                             Nano_bioPageView, Nano_energyPageView, smart_microPageView,
                             wearable_devPageView)

urlpatterns = [
    path('', HomepagePageView.as_view()),
    path('index', HomepagePageView.as_view()),
    path('publications', PublicationPageView.as_view()),
    path('professor', ProfPageView.as_view()),
    path('phd', PhdPageView.as_view()),
    path('ms', MScPageView.as_view()),
    path('bs', BScPageView.as_view()),
    path('contact', ContactPageView.as_view()),
    path('nano_assembly', Nano_assemblyPageView.as_view()),
    path('nanofabrication', NanofabricationPageView.as_view()),
    path('nano_bio', Nano_bioPageView.as_view()),
    path('wearable_dev', wearable_devPageView.as_view()),
    path('iod_dev', iod_devPageView.as_view()),
    path('smart_micro', smart_microPageView.as_view()),
    path('nano_energy', Nano_energyPageView.as_view()),
    path('activities', ActivitiesPageView.as_view()),
    # path('iod', IoDPageView.as_view()),
]
