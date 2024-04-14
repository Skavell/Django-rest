import json
from django.core.management.base import BaseCommand
from tutorial.quickstart.models import BoardGame


class Command(BaseCommand):
    help = 'Converts BoardGame objects to JSON'

    def handle(self, *args, **options):
        boardgames = BoardGame.objects.all()
        data = []
        for boardgame in boardgames:
            boardgame_data = {
                'title': boardgame.title,
                'description': boardgame.description,
                'price': str(boardgame.price),
                'category': boardgame.category.name,
                'image': boardgame.image.url,
            }
            data.append(boardgame_data)

        output_file = 'boardgames.json'
        with open(output_file, 'w') as f:
            json.dump(data, f, indent=2)

        self.stdout.write(self.style.SUCCESS(f'Successfully converted {len(data)} boardgames to {output_file}'))
