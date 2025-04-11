from django.contrib.auth.models import User
from django.db import models

class College(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    mobile_number = models.CharField(max_length=15)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.user.username
    
class Event(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('X', 'Mixed'),
    ]

    name = models.CharField(max_length=255)
    sport = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    max_team_size = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.sport} - {self.get_gender_display()}"

class Team(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="teams")
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    members = models.ManyToManyField(UserProfile, blank=True)
    class Meta:
        unique_together = ('event', 'college')  # Ensures one team per college per event

    def is_full(self):
        return self.members.count() < self.event.max_team_size

    def __str__(self):
        return f"{self.college.name} - {self.event} - {', '.join([p.user.username for p in self.members.all()])}"
    
class Match(models.Model):
    start = models.TimeField()
    end = models.TimeField()
    contestants=models.ManyToManyField(Team, blank=True)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f"{self.event}"

class Result(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team=   models.ForeignKey(Team, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=20, choices=[
        ("Win", "Win"),
        ("Lose", "Lose"),
        ("Draw", "Draw"),
    ]) 
    scoretype= models.CharField(max_length=20, choices=[
        ("Runs","Runs Scored"),
        ("Goals","Goals Scored"),
        ("Sets's Won","Set's Won"),


    ])
    score=models.IntegerField()

    def __str__(self):
        return f"{self.team}-{self.get_outcome_display()}-{self.score}"

class Result_Many(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    team=   models.ForeignKey(Team, on_delete=models.CASCADE)
    outcome = models.CharField(max_length=20, choices=[
        ("Qualified", "Qualified"),
        ("Eliminated", "Eliminated"),
       
    ]) 
    rank=models.IntegerField()
    
    def __str__(self):
        return f"{self.team}-{self.get_outcome_display()}-{self.rank}"
