from django.db import models
from django_quill.fields import QuillField

class Project(models.Model):
    STATUS_CHOICES = [
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
    ]

    title = models.CharField(max_length=200)
    description = QuillField()  # Replaced RichTextUploadingField with QuillField
    preview_image = models.ImageField(upload_to='media/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='ongoing')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Blog(models.Model):
    title = models.CharField(max_length=200)
    content = QuillField()  # Replaced RichTextUploadingField with QuillField
    short_description = models.TextField()
    preview_image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.author} on {self.blog}'

class Career(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
