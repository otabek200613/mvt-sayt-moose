from .models import Footer

def footer_context(request):
    return {
        'footer': Footer.objects.filter(is_published=True).first()
    }
