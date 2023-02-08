from django.db import models

# Create your models here.
class Post(models.Model):
    '''Information about post'''
    title = models.CharField('Title', max_length=100)
    description = models.TextField('Main text')
    author = models.CharField('Author name', max_length=100)
    date = models.DateField('Date')
    img = models.ImageField('Image', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}, {self.date}'

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comments(models.Model):
    '''Comment'''
    email = models.EmailField()
    name = models.CharField('Name', max_length=50)
    text_comments = models.TextField('Comment text', max_length=2000)
    post = models.ForeignKey(Post, verbose_name='Publication', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

class Likes(models.Model):
    '''Add likes'''
    ip = models.CharField('IP-address', max_length=100)
    pos = models.ForeignKey(Post, verbose_name='Publication', on_delete=models.CASCADE)