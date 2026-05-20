from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)
    score = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        users = [
            User.objects.create_user(username='superman', email='superman@dc.com', password='pass', first_name='Clark', last_name='Kent'),
            User.objects.create_user(username='batman', email='batman@dc.com', password='pass', first_name='Bruce', last_name='Wayne'),
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass', first_name='Tony', last_name='Stark'),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass', first_name='Peter', last_name='Parker'),
        ]

        # Activities
        Activity.objects.create(user='superman', type='flight', duration=120)
        Activity.objects.create(user='batman', type='training', duration=90)
        Activity.objects.create(user='ironman', type='engineering', duration=150)
        Activity.objects.create(user='spiderman', type='web-swinging', duration=60)

        # Leaderboard
        Leaderboard.objects.create(user='superman', score=1000)
        Leaderboard.objects.create(user='batman', score=900)
        Leaderboard.objects.create(user='ironman', score=950)
        Leaderboard.objects.create(user='spiderman', score=870)

        # Workouts
        Workout.objects.create(name='Super Strength', description='Lift heavy objects')
        Workout.objects.create(name='Martial Arts', description='Hand-to-hand combat training')
        Workout.objects.create(name='Tech Building', description='Build and test new tech')
        Workout.objects.create(name='Agility', description='Improve flexibility and reflexes')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
