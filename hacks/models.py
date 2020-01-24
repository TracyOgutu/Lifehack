from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Profile(models.Model):
    '''
    Class that contains User Profile details
    '''
    profile_photo=models.ImageField(upload_to='images/',blank=True)
    bio=models.CharField(max_length=100)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        '''
        Setting up self 
        '''
        return self.bio

    @classmethod
    def get_profile(cls):
        '''
        Method to retrieve the profile details
        '''
        profile=cls.objects.all()
        return profile

    def save_profile(self):
        '''
        Method to save the created profile
        '''
        self.save()

    def delete_profile(self):
        '''
        Method to delete the profile
        '''
        self.delete()
    @classmethod
    def single_profile(cls,user_id):
        '''
        function gets a single profile posted by id
        '''
        profile=cls.objects.get(editor=user_id)
        return profile

    @classmethod
    def get_profilepic_id(cls,imageId):
        '''
        function that gets a profilepic id    
        '''
        image_id=cls.objects.filter(id=imageId)
        return image_id

class Category(models.Model):
    '''
    Class that contains the categories available 
    '''
    category=models.CharField(max_length=30)

    def __str__(self):
        '''
        Setting up self
        '''
        return self.category
    
class Hack(models.Model):
    '''
    Class that has details for the image that is posted 
    '''
    image=models.ImageField(upload_to='images/',blank=True)
    hack_category=models.ForeignKey(Category,on_delete=models.CASCADE)
    hack_caption=models.CharField(max_length=100)
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    profile=models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)
    likes=models.ManyToManyField(User,related_name="likes",blank=True)
    followers=models.ManyToManyField(User,related_name="followers",blank=True)
    # comments=models.ForeignKey(Comments,null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        Setting up self
        '''
        return self.hack_caption

    def save_hack(self):
        '''
        Method for saving the image
        '''
        self.save()

    def delete_hack(self):
        '''
        Method for deleting the image
        '''
        self.delete()
    
    @classmethod
    def get_hacks(cls):
        '''
        Method for retrieving all hack
        '''
        hack=cls.objects.all()
        return hack

    @classmethod
    def search_by_category(cls,category):
        '''
        Method for searching for a hack using the category
        '''

        category_result=cls.objects.filter(hack_category__category__icontains=category)
        return category_result

    @classmethod
    def get_hack_id(cls,hackId):
        '''
        function that gets a hack id    
        '''
        hack_id=cls.objects.filter(id=hackId)
        return hack_id

    @classmethod
    def single_hack(cls,hack_id):
        '''
        function gets a single hack posted by id
        '''
        hack_posted=cls.objects.get(id=hack_id)
        return hack_posted

    @classmethod
    def user_hacks(cls,user_id):
        '''
        function gets images posted by id
        '''
        hack_posted=cls.objects.filter(editor=user_id)
        return hack_posted    

class Comments(models.Model):
    '''
    Class that contains the deatils of the comments made by the users
    '''
    detail= HTMLField()
    editor = models.ForeignKey(User,on_delete=models.CASCADE)
    comment_date = models.DateTimeField(auto_now_add=True)
    hack_foreign=models.ForeignKey(Hack, on_delete=models.CASCADE)

    def __str__(self):
        '''
        Setting up self
        '''
        return self.detail

    @classmethod
    def get_comments(cls):
        '''
        Method for getting all the comments posted
        '''
        comment=cls.objects.all()
        return comment

    @classmethod
    def get_singlepost_comments(cls, id):
        '''
        function that gets comments for a single post
        '''
        comments=cls.objects.filter(hack_foreign__in=id)
        return comments
    def save_comment(self):
        '''
        function that saves a new comment
        '''
        self.save()

    def delete_comment(self):
        '''
        function that deletes a comment
        '''
        self.delete()
    

class NewsLetterRecipients(models.Model):
    '''
    Class that contains details of users who subscribe to the website newsletter
    '''
    name = models.CharField(max_length = 30)
    email = models.EmailField()


