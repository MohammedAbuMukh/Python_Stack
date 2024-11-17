from django.db import models

class Description(models.Model):
    content = models.TextField()

class CourseManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        name = postData.get('name', '')
        description_content = postData.get('description_content', '')

        if len(name) < 5:
            errors["name"] = "Course name must be more than five characters long."
        if len(description_content) < 15:
            errors["description_content"] = "Description must be more than 15 characters long."

        return errors

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.OneToOneField(Description, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()