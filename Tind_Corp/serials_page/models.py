from django.db import models
import os

def get_upload_path(instance, filename):
    return f"serials/{instance.slug}/{filename}"

#Створюємо модель Base(для серіалів)
class Base(models.Model):
    title = models.CharField("Назва", max_length=75)
    serias = models.CharField("Серії", max_length=75, default="none")
    poster = models.ImageField("Постер", max_length=75, default="none", upload_to=get_upload_path)
    top1 = models.CharField("Перший топ", max_length=150, default="none")
    top2 = models.CharField("Другий топ", max_length=150, default="none")
    top3 = models.CharField("Третій топ", max_length=150, default="none")
    years_go = models.CharField("Вихід серілу", max_length=75, default="none")
    country = models.CharField("Країни", max_length=75, default="USA")
    djanrs = models.CharField("Жанри", max_length=50)
    about = models.TextField("Про:")
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Серіал"
        verbose_name_plural = "Серіали"

#Створюємо модель serias для серій
class serias(models.Model):
    title_series = models.CharField("Серія", max_length=75)
    video_series = models.FileField(upload_to=get_upload_path)
    Base = models.ForeignKey(Base, on_delete=models.CASCADE, related_name='Base_Serials')

    def __str__(self):
        return self.title_series

    @property
    def slug(self):
        return self.Base.slug
