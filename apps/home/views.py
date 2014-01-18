# Import from Django
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    """
    This is the home page for both logged in and logged out users.
    We do not have a separate page for the two for now.
    """
    template_name = 'home/home_page.html'