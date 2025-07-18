from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Universities(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    website = models.URLField()
    faculty = models.CharField()
    type = models.CharField(max_length=10, choices=[('Public', 'Public'), ('Private', 'Private')])
    phone_number = models.CharField(max_length=15)

    class Meta:
        verbose_name = "University"
        verbose_name_plural =" University"


    def __str__(self):
        return self.name

class Interns(models.Model):
    first_name = models.CharField(max_length= 30)
    last_name = models.CharField(max_length= 30)
    university = models.ForeignKey(Universities, on_delete=models.SET_NULL, related_name='interns', null='true',)
    reg_no = models.CharField(max_length= 30)
    program = models.CharField(max_length= 200)
    phone_number = models.CharField(max_length= 10)
    
    def __str__(self):

        return self.first_name

class InternshipDay(models.Model):
    Internship_days=[
        ('Day1', 'Day1'),
        ('Day2', 'Day2'),
        ('Day3', 'Day3'),
        ('Day4', 'Day4'),
        ('Day5', 'Day5'),
        ('Day6', 'Day6'),
        ('Day7', 'Day7'),
        ('Day8', 'Day8')

    ]
    Internship_day = models.CharField(max_length=5, choices=Internship_days)
    field_supervisors = [
        ('Sifu', 'Sifu'),
        ('Solomon', 'Solomon')
    ]
    field_supervisor = models.CharField(max_length=20,choices=field_supervisors)

    class Meta:
        verbose_name = "Internship Day"
        verbose_name_plural =" Internship Day"

    def __str__(self):
        return self.Internship_day
    

class Task(models.Model):
    task = models.CharField(max_length=500, unique=True)
    day = models.ForeignKey(InternshipDay, on_delete=models.SET_NULL, null=True , related_name="tasks", blank="true")

    def __str__(self):
        return self.task


class Tool(models.Model):
    tool_name = models.CharField(max_length=200)
    activity = models.ForeignKey(Task, on_delete=models.CASCADE, null=True ,related_name="tools")
    
    def __str__(self):
        return self.tool_name

class Skill(models.Model):
    skill = models.CharField(max_length=200)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True, related_name="skills")  

    def __str__(self):
        return self.skill
  

class Experience(models.Model):
    experience = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True ,related_name="experiences")
      
    def __str__(self):
        return self.experience


class Challenge(models.Model):
    challenge = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True ,related_name="challenges", blank=True)
    def __str__(self):
        return self.challenge
    

class Suggestion(models.Model):
    suggestion = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True ,related_name="suggestions", blank=True)
    def __str__(self):
        return self.suggestion
    
class TaskImage(models.Model):
    task_image = models.ImageField(upload_to='task_images/', null=True, blank=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE, null=True ,related_name="task_images",  blank=True)
    def __str__(self):
        return self.task_image.url
    




    
    






