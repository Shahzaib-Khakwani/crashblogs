from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=88)
    slug = models.SlugField()

    class Meta:
        ordering = ('title',)
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/%s/' % self.slug

class Post(models.Model):
    ACTIVE = 'active'
    DRAFT = 'draft'

    options = ((ACTIVE, 'active'),(DRAFT, 'draft'))


    category = models.ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()
    intro = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=options, default = ACTIVE)
    image = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return '/%s/%s/' %  (self.category.slug, self.slug)

    class Meta:
        ordering = ('-created_at',)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author
