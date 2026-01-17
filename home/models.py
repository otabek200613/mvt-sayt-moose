from django.db import models





class Home(models.Model):
    page_title = models.CharField(max_length=50, verbose_name="Page title")
    name_part1 = models.CharField(max_length=50, verbose_name="Ism 1-qism")
    name_part2 = models.CharField(max_length=50, verbose_name="Ism 2-qism")
    name_part3 = models.CharField(max_length=50, verbose_name="Ism 3-qism")
    bio_title = models.TextField(verbose_name="Bio title")
    bio_content = models.TextField(verbose_name="Bio content")
    photo = models.ImageField(upload_to='photos/%Y/%m', verbose_name="Photo")
    full_name = models.CharField(max_length=50, verbose_name="Full name")
    description = models.TextField(verbose_name="Description")
    twitter = models.URLField(verbose_name="Twitter",null=True,blank=True)
    facebook = models.URLField(verbose_name="Facebook",null=True,blank=True)
    instagram = models.URLField(verbose_name="Instagram",null=True,blank=True)
    is_published = models.BooleanField(verbose_name="Is published?",default=True)
    def __str__(self):
        return f"{self.name_part1}{self.name_part2}{self.name_part3}"
class Tags(models.Model):
    tag_name = models.CharField(max_length=50, verbose_name="Tag name")

    def __str__(self):
        return f"{self.tag_name}"


class Article(models.Model):
    tags = models.ManyToManyField(Tags, verbose_name="Tags")
    image = models.ImageField(upload_to='photos/%Y/%m', verbose_name="Photo")
    title = models.CharField(max_length=50, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    how_it_works = models.TextField(verbose_name="How it works")
    created = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(verbose_name="Is published?",default=True)
    def __str__(self):
        return f"{self.title}"

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    full_name = models.CharField(max_length=50, verbose_name="Full name")
    email = models.EmailField(verbose_name="Email")
    message = models.TextField(verbose_name="Message")
    created = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(verbose_name="Is published?", default=False)

    def __str__(self):
        return f"{self.full_name} - {self.article}"



class Contact_me(models.Model):
    address = models.TextField(verbose_name="Address")
    phone = models.TextField(verbose_name="Phone")
    email = models.TextField(verbose_name="Email")
    website = models.TextField(verbose_name="Website")
    website_link = models.URLField(verbose_name="Website link")

    is_published = models.BooleanField(verbose_name="Is published?",default=True)
    def __str__(self):
        return f"{self.phone}"
    def clean(self):
        if self.phone and not self.phone.startswith('+'):
            self.phone = '+' + self.phone

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)



class Contact(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    subject = models.TextField(verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    is_read = models.BooleanField(verbose_name="Is read?",default=False)
    def __str__(self):
        return f"{self.full_name}"

class About(models.Model):
    title = models.CharField(max_length=150, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    how_i_work = models.TextField(verbose_name="How I work")
    is_published = models.BooleanField(verbose_name="Is published?",default=True)



class Footer(models.Model):
    address = models.TextField(verbose_name="Address")
    phone = models.TextField(verbose_name="Phone")
    telegram = models.URLField(verbose_name="Telegram")
    is_published = models.BooleanField(verbose_name="Is published?",default=True)





































