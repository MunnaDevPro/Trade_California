import os
import django
import urllib.request
from django.core.files import File
from urllib.error import URLError

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.dev')
django.setup()

from apps.products.models import Category, Product, ProductImage
import tempfile

def download_image(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        with urllib.request.urlopen(req) as response:
            fd, path = tempfile.mkstemp()
            with os.fdopen(fd, 'wb') as f:
                f.write(response.read())
            return path
    except URLError as e:
        print(f"Failed to download {url}: {e}")
        return None

# Clear existing
print("Clearing existing products...")
Category.objects.all().delete()
Product.objects.all().delete()
ProductImage.objects.all().delete()

print("Creating categories...")
cat_ag = Category.objects.create(
    name="Agricultural Produce",
    description="Premium California-grown fruits, nuts, and vegetables ready for export."
)
cat_wine = Category.objects.create(
    name="Wines & Beverages",
    description="World-renowned California wines and artisanal beverages."
)
cat_tech = Category.objects.create(
    name="Industrial Tech",
    description="Cutting-edge manufacturing and agricultural technology."
)

print("Creating products...")

# Products for Agricultural Produce
p1 = Product.objects.create(
    category=cat_ag,
    name="California Almonds (Nonpareil)",
    origin_country="USA",
    is_featured=True,
    description="Premium grade Nonpareil almonds sourced directly from California's Central Valley. Perfect for roasting, snacking, or culinary applications. Available in 50lb cartons."
)
p2 = Product.objects.create(
    category=cat_ag,
    name="Fresh Hass Avocados",
    origin_country="USA",
    is_featured=False,
    description="Rich, creamy, and packed with healthy fats. Our Hass avocados are carefully hand-picked and exported in climate-controlled shipping containers."
)

# Products for Wines
p3 = Product.objects.create(
    category=cat_wine,
    name="Napa Valley Cabernet Sauvignon",
    origin_country="USA",
    is_featured=True,
    description="A bold and complex Cabernet Sauvignon with notes of dark cherry, cedar, and vanilla. Aged 18 months in French oak. Minimum order: 50 cases."
)

# Products for Tech
p4 = Product.objects.create(
    category=cat_tech,
    name="Automated Irrigation System V4",
    origin_country="USA",
    is_featured=False,
    description="Smart irrigation controllers leveraging AI and localized weather data to optimize water usage in large scale farming operations."
)

products = [
    (p1, "https://images.unsplash.com/photo-1505253758473-96b7015fcd40?w=800&q=80"), # Almonds
    (p2, "https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?w=800&q=80"), # Avocados
    (p3, "https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?w=800&q=80"), # Wine
    (p4, "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?w=800&q=80"), # Tech
]

print("Downloading and attaching images...")
for product, img_url in products:
    print(f"Fetching image for {product.name}...")
    temp_path = download_image(img_url)
    if temp_path:
        with open(temp_path, 'rb') as f:
            img_obj = ProductImage(product=product, is_primary=True)
            img_obj.image.save(f"{product.slug}.jpg", File(f), save=True)
        os.remove(temp_path)
    else:
        print(f"Skipped image for {product.name}")

print("Seeding complete!")
