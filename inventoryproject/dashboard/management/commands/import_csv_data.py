from django.core.management.base import BaseCommand, CommandParser
from dashboard.models import Tile
import csv

class Command(BaseCommand):

    help = "Add stock to the database!"

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('csv_file', 
                             type=str,
                             help='path to csv filepath')
        
    def handle(self, *args, **options):
        csv_file = options['csv_file']

        with open(csv_file, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tile = Tile(
                    product_name=row['Product Name'],
                    product_quantity=row['Product Quantity'],
                    dealer_name=row['Dealer Name']
                )
                tile.save()

                self.stdout.write(self.style.SUCCESS(f'Successfully added tile: {tile.product_name}'))