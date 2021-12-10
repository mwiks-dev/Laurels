from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User



# Create your models here.
class Profile(models.Model):
    prof_photo = CloudinaryField('image')
    bio = models.TextField(max_length=1000, blank=True, null=True)
    phone_number = models.CharField(max_length=10, blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        self.save()

    def update_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile


class Project(models.Model):
    image = CloudinaryField('image')
    project_name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    category = models.TextField(max_length=20)
    location = models.TextField(max_length=20)
    url = models.URLField(max_length=60,null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.project_name

    @classmethod
    def get_all_projects(cls):
        projects = Project.objects.all()
        return projects

    @classmethod
    def search_by_project_name(cls,search_term):
        name = cls.objects.filter(project_name__name__icontains=search_term)
        return name

    @classmethod
    def display_all_projects(cls):
        return cls.objects.all()

    def save_project(self):
        self.save()

    def update_project(self,project_name,description,category):
        self.project_name = project_name,
        self.description = description,
        self.category = category
        self.save()


    class Meta:
        ordering = ['-pub_date']