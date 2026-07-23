from .models import SiteSettings, NavigationLink, FooterLink

def site_context(request):
    try:
        settings = SiteSettings.objects.get()
    except SiteSettings.DoesNotExist:
        # Fallback if no settings exist (they should be created by migration)
        settings = None

    nav_links = NavigationLink.objects.filter(is_active=True)
    footer_links = FooterLink.objects.filter(is_active=True)

    return {
        'site_settings': settings,
        'nav_links': nav_links,
        'footer_links': footer_links,
    }
