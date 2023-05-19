from django.db import models

def get_upload_path(instance, filename):
    return f"films/{instance.slug}/{filename}"

#Створюємо модель films
class films(models.Model):
    title = models.CharField("Назва", max_length=75)
    poster = models.ImageField("Постер", max_length=75, default="none", upload_to=get_upload_path)
    top1 = models.CharField("Перший топ", max_length=150, default="none")
    top2 = models.CharField("Другий топ", max_length=150, default="none")
    top3 = models.CharField("Третій топ", max_length=150, default="none")
    years_go = models.CharField("Вихід серілу", max_length=75, default="none")
    country = models.CharField("Країни", max_length=75, default="USA")
    djanrs = models.CharField("Жанри", max_length=50)
    about = models.TextField("Про:")
    slug = models.SlugField(max_length=200, unique=True)
    video = models.FileField(upload_to=get_upload_path)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фільм"
        verbose_name_plural = "Фільми"