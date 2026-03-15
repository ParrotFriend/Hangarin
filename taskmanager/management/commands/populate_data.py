from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from taskmanager.models import Priority, Category, Task, Note, SubTask
import random

fake = Faker()

class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **kwargs):
        # Priorities
        for name in ['High', 'Medium', 'Low', 'Critical', 'Optional']:
            Priority.objects.get_or_create(name=name)

        # Categories
        for name in ['Work', 'School', 'Personal', 'Finance', 'Projects']:
            Category.objects.get_or_create(name=name)

        priorities = list(Priority.objects.all())
        categories = list(Category.objects.all())

        # Tasks
        for _ in range(20):
            task = Task.objects.create(
                title=fake.sentence(nb_words=5),
                description=fake.paragraph(nb_sentences=3),
                deadline=timezone.make_aware(fake.date_time_this_month()),
                status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                category=random.choice(categories),
                priority=random.choice(priorities),
            )

            # Notes
            for _ in range(random.randint(1, 3)):
                Note.objects.create(task=task, content=fake.paragraph())

            # SubTasks
            for _ in range(random.randint(1, 4)):
                SubTask.objects.create(
                    parent_task=task,
                    title=fake.sentence(nb_words=4),
                    status=fake.random_element(elements=["Pending", "In Progress", "Completed"]),
                )

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))