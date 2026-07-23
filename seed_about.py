import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from apps.core.models import Mentor, CompanyValue

# Clear existing just in case
Mentor.objects.all().delete()
CompanyValue.objects.all().delete()

CompanyValue.objects.create(
    title="Global Reach",
    description="We bridge the gap between high-quality American products and international markets.",
    icon="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z",
    order=1
)
CompanyValue.objects.create(
    title="Uncompromised Quality",
    description="We ensure every product exported meets rigorous American agricultural standards.",
    icon="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z",
    order=2
)
CompanyValue.objects.create(
    title="Trusted Partnerships",
    description="Building long-term, reliable relationships with our buyers and distributors.",
    icon="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z",
    order=3
)

Mentor.objects.create(
    name="Sarah Jenkins",
    role="Director of International Trade",
    bio="Sarah brings 15+ years of experience in global supply chains, helping American farmers reach new markets in Asia and Europe.",
    order=1
)
Mentor.objects.create(
    name="David Chen",
    role="Head of Quality Assurance",
    bio="Former FDA inspector, David ensures that all exports maintain the strict quality standards expected of US agriculture.",
    order=2
)
Mentor.objects.create(
    name="Elena Rodriguez",
    role="Global Partnerships Lead",
    bio="Elena is an expert in forming robust distributor networks, fluent in 4 languages and specializing in the Latin American market.",
    order=3
)
print("Seeding complete.")
