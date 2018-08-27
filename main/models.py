from django.db import models

# это будет корзина куда добавляют заказ. на эту модель будут ссылатся все остальные
class Basket(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Pizz(models.Model):
    
    title = models.CharField(max_length=200,help_text="Добавь название")
    pizzphoto = models.ImageField( help_text="Добавь фото")
    aboutpizz = models.TextField(max_length=1000, help_text="Состав пиццы")
    price = models.CharField(max_length=200,help_text="Добавь цену")
    def __str__(self):
        
        return self.title
    
    
    def get_absolute_url(self):
        
        return reverse('pizz-detail', args=[str(self.id)])

#-----------------------------------------------------------------------------------------
class Drink(models.Model):
    
    title = models.CharField(max_length=200,help_text="Добавь название")
    drinkphoto = models.ImageField( help_text="Добавь фото")
    price = models.CharField(max_length=200,help_text="Добавь описание")
    
    def __str__(self):
        
        return self.title
    
    
    def get_absolute_url(self):
        
        return reverse('pizz-detail', args=[str(self.id)])

    def image_img(self):
        if self.drinkphoto:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(self.drinkphoto.url)
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

#--------------------------------------------------------------------------------


class Potato(models.Model):
    
    title = models.CharField(max_length=200,help_text="Добавь название")
    potatophoto = models.ImageField( help_text="Добавь фото")
    price = models.CharField(max_length=200,help_text="Добавь описание")
    
    def __str__(self):
        
        return self.title
    
    
    def get_absolute_url(self):
        
        return reverse('potato-detail', args=[str(self.id)])

    def image_img(self):
        if self.potatophoto:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(self.potatophoto.url)
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

#----------------------------------------------------------------------------------------


class Pasta(models.Model):
    
    title = models.CharField(max_length=200,help_text="Добавь название")
    pastaphoto = models.ImageField( help_text="Добавь фото")
    price = models.CharField(max_length=200,help_text="Добавь описание")
    
    def __str__(self):
        
        return self.title
    
    
    def get_absolute_url(self):
        
        return reverse('pasta-detail', args=[str(self.id)])

    def image_img(self):
        if self.pastaphoto:
            return u'<a href="{0}" target="_blank"><img src="{0}" width="50"/></a>'.format(self.pastaphoto.url)
        else:
            return '(Нет изображения)'
    image_img.short_description = 'Картинка'
    image_img.allow_tags = True