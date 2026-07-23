from django.db import migrations

def seed_data(apps, schema_editor):
    SiteSettings = apps.get_model('core', 'SiteSettings')
    NavigationLink = apps.get_model('core', 'NavigationLink')
    FooterLink = apps.get_model('core', 'FooterLink')
    Category = apps.get_model('products', 'Category')
    Product = apps.get_model('products', 'Product')
    ServiceType = apps.get_model('services', 'ServiceType')
    OfficeLocation = apps.get_model('contact', 'OfficeLocation')

    # Seed SiteSettings
    if not SiteSettings.objects.exists():
        SiteSettings.objects.create(
            site_name="Trade California International",
            tagline="Connecting American Products with International Markets",
            hero_headline="Expand Your Global Reach",
            hero_subtext="Premium Trade & International Business Platform",
            hero_cta_text="Register Now",
            hero_cta_link="/registration/",
            about_text="<p>Trade California International is your trusted partner for expanding business globally.</p>",
            contact_email="contact@tradecalifornia.com",
            contact_phone="+1 (800) 123-4567"
        )

    # Seed Navigation Links
    nav_items = [
        ("Home", "/", 1),
        ("About Us", "/about/", 2),
        ("Trade", "/products/", 3),
        ("Services", "/services/", 4),
        ("Registration", "/registration/", 5),
        ("Contact", "/contact/", 6),
    ]
    for label, url, order in nav_items:
        NavigationLink.objects.get_or_create(label=label, defaults={'url': url, 'order': order})
        FooterLink.objects.get_or_create(label=label, defaults={'url': url, 'order': order})

    # Seed Categories
    cats = [
        ("Wheat", "wheat", "Premium American Wheat"),
        ("Cotton", "cotton", "High-quality Cotton"),
        ("Sunflower Oil", "sunflower-oil", "Pure Sunflower Oil"),
        ("American Produce", "american-produce", "Fresh American Produce"),
    ]
    for name, slug, desc in cats:
        Category.objects.get_or_create(slug=slug, defaults={'name': name, 'description': desc})

    # Seed Products
    wheat_cat = Category.objects.filter(slug='wheat').first()
    if wheat_cat:
        Product.objects.get_or_create(
            slug='premium-hard-red-wheat',
            defaults={
                'name': 'Premium Hard Red Wheat',
                'category': wheat_cat,
                'origin_country': 'USA',
                'is_featured': True,
                'description': 'High protein hard red wheat ideal for baking.'
            }
        )

    # Seed Services
    services = [
        ("Buyer", "buyer", "Find the best American products for your market."),
        ("Seller", "seller", "Expand your reach and sell globally."),
        ("Distributor", "distributor", "Partner with us to distribute premium goods."),
    ]
    for title, slug, desc in services:
        ServiceType.objects.get_or_create(slug=slug, defaults={'title': title, 'short_description': desc})

    # Seed Office Locations
    offices = [
        ("Head Office", "123 Business Ave, Suite 100\nLos Angeles, CA 90001", "+1 (800) 123-4567", 1),
        ("Orange County Office", "456 Trade Blvd\nIrvine, CA 92614", "+1 (800) 765-4321", 2),
    ]
    for name, address, phone, order in offices:
        OfficeLocation.objects.get_or_create(name=name, defaults={'address': address, 'phone': phone, 'order': order})

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
        ('products', '0001_initial'),
        ('services', '0001_initial'),
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(seed_data),
    ]
