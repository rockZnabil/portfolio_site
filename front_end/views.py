from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView

from front_end.models import Publication, Book, Cover, Conference


class HomepagePageView(TemplateView):
    template_name = 'homepage_page.html'


class PublicationPageView(TemplateView):
    template_name = 'publication_page.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['covers'] = Cover.objects.all()
        ctx['publications'] = Publication.objects.all().order_by('-publication_index')
        ctx['books'] = Book.objects.all().order_by('-book_index')
        ctx['conferences'] = Conference.objects.all().order_by('-conference_index')
        return ctx


class ProfPageView(TemplateView):
    template_name = 'prof_page.html'


class PhdPageView(TemplateView):
    template_name = 'phd_page.html'


class MScPageView(TemplateView):
    template_name = 'msc_page.html'


class BScPageView(TemplateView):
    template_name = 'bsc_page.html'


class ContactPageView(TemplateView):
    template_name = 'contact_page.html'


class Nano_assemblyPageView(TemplateView):
    template_name = 'nano_assembly_page.html'


class NanofabricationPageView(TemplateView):
    template_name = 'nanofabrication_page.html'


class Nano_bioPageView(TemplateView):
    template_name = 'nano_bio_page.html'


class Nano_energyPageView(TemplateView):
    template_name = 'nano_energy_page.html'


class wearable_devPageView(TemplateView):
    template_name = 'wearable_dev_page.html'


class smart_microPageView(TemplateView):
    template_name = 'smart_micro_page.html'


class iod_devPageView(TemplateView):
    template_name = 'iod_dev_page.html'


class ActivitiesPageView(TemplateView):
    template_name = 'activities_page.html'


# class IoDPageView(TemplateView):
#     template_name = 'iod_page.html'
