from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='marvel')
        dc = Team.objects.create(name='dc')

        # Users
        users = [
            User.objects.create(email='ironman@marvel.com', name='Iron Man', team='marvel'),
            User.objects.create(email='captain@marvel.com', name='Captain America', team='marvel'),
            User.objects.create(email='batman@dc.com', name='Batman', team='dc'),
            User.objects.create(email='superman@dc.com', name='Superman', team='dc'),
        ]

        # Activities
        Activity.objects.create(user='ironman@marvel.com', activity_type='run', duration=30, date='2026-04-01')
        Activity.objects.create(user='captain@marvel.com', activity_type='cycle', duration=45, date='2026-04-02')
        Activity.objects.create(user='batman@dc.com', activity_type='swim', duration=25, date='2026-04-01')
        Activity.objects.create(user='superman@dc.com', activity_type='fly', duration=60, date='2026-04-03')

        # Leaderboard
        Leaderboard.objects.create(user='ironman@marvel.com', points=120)
        Leaderboard.objects.create(user='captain@marvel.com', points=110)
        Leaderboard.objects.create(user='batman@dc.com', points=130)
        Leaderboard.objects.create(user='superman@dc.com', points=140)

        # Workouts
        Workout.objects.create(name='Pushups', description='Do 20 pushups', difficulty='easy')
        Workout.objects.create(name='Pullups', description='Do 10 pullups', difficulty='medium')
        Workout.objects.create(name='Squats', description='Do 30 squats', difficulty='easy')
        Workout.objects.create(name='Flying', description='Fly for 10 minutes', difficulty='super')

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
