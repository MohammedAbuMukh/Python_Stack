from django.db import models
from django.utils import timezone



class ShowManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['title']) < 2:
            errors["title"] = "title should be at least 2 characters"
        
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters" 
            
        if len(postData['desc']) < 10 :
            errors['desc'] = "Description should be at least 10 characters"  
        
        if Show.objects.filter(title =postData['title']).exists():
            errors["title"] = "A show with this title already exists"
        
        released_date = timezone.datetime.strptime(postData['released_date'], "%Y-%m-%d").date()
        if released_date > timezone.datetime.today().date():
            errors["released_date"] = "Release date cannot be in the future."  
                
            
        return errors    
    
      
        
            

class Show(models.Model):
    title = models.CharField(max_length=50)
    network = models.CharField(max_length=50)
    released_date = models.DateField()
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()

def get_all_shows():
    return Show.objects.all()

def get_show_by_id(id):
    return Show.objects.get(id = id)

def create_show(data):
    title = data['title']
    network = data['network']
    released_date = data['released_date']
    desc = data['desc']
    Show.objects.create(title=title, network=network, released_date=released_date, desc=desc)

def delete_show(id):
    c = Show.objects.get(id=id)
    c.delete()

def update(data):
       id = int(data['id'])
       c= Show.objects.get(id =id )
       c.title = data['title']
       c.network = data['network']
       c.released_date = data['released_date']
       c.desc = data['desc']
       c.save()
       
       
