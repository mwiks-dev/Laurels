from django.test import TestCase
from .models import Profile,Project,Rating
from django.contrib.auth.models import User


class ProfileTestClass(TestCase):
    #Set Up method
    def setUp(self):
        self.maryann = Profile(prof_photo = 'image.png',bio = 'I love Music',phone_number = '0712345678')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.maryann,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.maryann.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Rating.objects.all().delete()

    # Testing Update Method
    def test_update_method(self):
        self.maryann.update_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

    def test_get_profile_by_user(self):
        user = 1
        profile = Profile.get_profile_by_user(user)
        self.assertFalse(len(profile)>0)

class ProjectTestClass(TestCase):
    def setUp(self):
        self.project1 = Project(image = 'image.png',project_name ='Project1',description='new',category='new',location='Kenya',url='https.me.com',pub_date='12/02/2021')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.project1,Project))

    # Testing Save Method
    def test_save_method(self):
        self.project1.save_project()
        project1 = Project.objects.all()
        self.assertTrue(len(project1) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Rating.objects.all().delete()

    # Testing display Method
    def test_display_projects(self):
        projects = Project.display_all_projects()
        self.assertFalse(len(projects) > 0 )

    def test_search_project_by_name(self):
        project_name = 'Test'
        project = Project.search_by_project_name(project_name)
        self.assertFalse(len(project)>0)

    def test_get_all_projects(self):
        projects = Project.get_all_projects()
        self.assertFalse(len(projects) > 0)

class RatingTestClass(TestCase):
    def setUp(self):
        self.rate = Rating(design_rate='7',usability_rate = '8',content_rate ='9',average='11')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.rate,Rating))

    # Testing Save Method
    def test_save_method(self):
        self.rate.save_rate()
        rate1 = Rating.objects.all()
        self.assertTrue(len(rate1) > 0)

    def tearDown(self):
        Profile.objects.all().delete()
        Project.objects.all().delete()
        Rating.objects.all().delete()
    
    def test_get_project_rates(self):
        rates = Rating.get_project_rates()
        self.assertTrue(len(rates) > 0)

    