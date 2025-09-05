from django.core.management.base import BaseCommand
from pages.factories import CommentFactory


class Command(BaseCommand):
    help = 'Seed the database with comments'
    
    def handle(self, *args, **kwargs):
        CommentFactory.create_batch(3)
        self.stdout.write(self.style.SUCCESS('Successfully seeded comments'))
