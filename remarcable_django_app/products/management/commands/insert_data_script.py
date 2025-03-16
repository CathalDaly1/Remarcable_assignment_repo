from django.core.management.base import BaseCommand
from products.models import Category, Tag, Product
from decimal import Decimal

class Command(BaseCommand):
    help = 'Inserts data into the database'

    def add_arguments(self, parser):
            parser.add_argument('--clear', action='store_true', help='Clear all data without seeding')

    def handle(self, *args, **kwargs):
        # Clear data if --clear is specified
        if kwargs['clear']:
            Product.objects.all().delete()
            Category.objects.all().delete()
            Tag.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Database cleared successfully!'))
            return

        # Music-Related Categories
        instruments = Category.objects.create(name='Instruments')
        accessories = Category.objects.create(name='Accessories')
        vinyl = Category.objects.create(name='Vinyl Records')
        audio = Category.objects.create(name='Audio Equipment')
        merch = Category.objects.create(name='Merchandise')

        # Music-Related Tags
        tags = {
            'new-release': Tag.objects.create(name='new-release'),
            'on-sale': Tag.objects.create(name='on-sale'),
            'popular': Tag.objects.create(name='popular'),
            'limited-edition': Tag.objects.create(name='limited-edition'),
            'vintage': Tag.objects.create(name='vintage'),
            'trending': Tag.objects.create(name='trending'),
            'top-chart': Tag.objects.create(name='top-chart'),
            'studio-quality': Tag.objects.create(name='studio-quality'),
            'collectible': Tag.objects.create(name='collectible'),
            'budget-friendly': Tag.objects.create(name='budget-friendly'),
        }

        # Music-Related Products
        products = [
            ('Electric Guitar', 'Classic rock electric guitar.', instruments, [tags['new-release'], tags['popular']], '299.99'),
            ('Guitar Strings', 'Pack of durable guitar strings.', accessories, [tags['on-sale'], tags['budget-friendly']], '9.99'),
            ('Rock Vinyl', 'Classic rock album on vinyl.', vinyl, [tags['new-release'], tags['top-chart']], '24.99'),
            ('Studio Headphones', 'High-fidelity headphones for mixing.', audio, [tags['trending'], tags['studio-quality']], '149.99'),
            ('Band T-Shirt', 'Official tour t-shirt.', merch, [tags['popular'], tags['collectible']], '19.99'),
            ('Acoustic Guitar', 'Warm-toned acoustic for folk music.', instruments, [tags['limited-edition'], tags['vintage']], '399.99'),
            ('Drumsticks', 'Pair of maple drumsticks.', accessories, [tags['budget-friendly'], tags['trending']], '7.99'),
            ('Jazz Vinyl', 'Ray Charles record.', vinyl, [tags['vintage'], tags['collectible']], '39.99'),
            ('Bluetooth Speaker', 'Portable speaker for music.', audio, [tags['on-sale'], tags['popular']], '59.99'),
            ('Tour Poster', 'Signed concert poster.', merch, [tags['limited-edition'], tags['top-chart']], '29.99'),
            ('Keyboard', '88-key digital piano.', instruments, [tags['new-release'], tags['studio-quality']], '499.99'),
            ('Guitar Pick', 'Set of 10 assorted picks.', accessories, [tags['budget-friendly'], tags['on-sale']], '4.99'),
            ('Pop Vinyl', 'Latest pop album on vinyl.', vinyl, [tags['trending'], tags['new-release']], '22.99'),
            ('Amplifier', 'Compact guitar amp.', audio, [tags['popular'], tags['budget-friendly']], '89.99'),
            ('Band Hoodie', 'Cozy hoodie with band logo.', merch, [tags['collectible'], tags['trending']], '34.99'),
            ('Drum Set', 'Complete drum kit for beginners.', instruments, [tags['on-sale'], tags['top-chart']], '599.99'),
            ('Metronome', 'Digital metronome for practice.', accessories, [tags['studio-quality'], tags['new-release']], '19.99'),
            ('Classical Vinyl', 'Dvorak Symphony No. 7 on vinyl.', vinyl, [tags['vintage'], tags['limited-edition']], '34.99'),
            ('Microphone', 'Condenser mic for recording.', audio, [tags['studio-quality'], tags['popular']], '129.99'),
            ('Keychain', 'Music note-shaped keychain.', merch, [tags['budget-friendly'], tags['collectible']], '5.99'),
        ]

        for name, desc, cat, tag_list, price in products:
            product = Product.objects.create(
                name=name,
                description=desc,
                category=cat,
                price=Decimal(price)
            )
            product.tags.set(tag_list)

        self.stdout.write(self.style.SUCCESS('Successfully seeded database with 5 music-related categories, 10 tags, and 20 products!'))