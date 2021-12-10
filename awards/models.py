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

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id = id).update(name = name)

    @classmethod
    def display_all_categories(cls):
        return cls.objects.all()

class Location(models.Model):
    loc = models.CharField(max_length=50)

    def __str__(self):
        return self.loc
        
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    @classmethod
    def update_location(cls,id,name):
        cls.objects.filter(id = id).update(loc = name)

    @classmethod
    def display_all_locations(cls):
        return cls.objects.all()

class Picture(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=2000)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    location = models.ForeignKey('Location',on_delete=models.CASCADE,null=True)
    pub_date = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_all_pictures(cls):
        pictures = Picture.objects.all()
        return pictures

    @classmethod
    def search_by_category(cls,search_term):
        galleria = cls.objects.filter(category__name__icontains=search_term)
        return galleria

    @classmethod
    def filter_by_location(cls, location):
        pictures = Picture.objects.filter(location__name=location)
        return pictures

    @classmethod
    def display_all_images(cls):
        return cls.objects.all()

    def save_picture(self):
        self.save()

    def update_picture(self,name,description,category):
        self.name = name,
        self.description = description,
        self.category = category
        self.save()

    def get_picture_by_id(cls,id):
        pic = Picture.objects.get(id=id)
        return pic


    class Meta:
        ordering = ['-pub_date']