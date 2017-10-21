from django.db import models #открывает доступ к коду из других файлов
                              #т.е. вместо того, чтобы копировать и вставлять один и тот же код во все файлы,
                              # ты можешь сослаться на него при помощи from ... import ..
from django.utils import timezone #открывает доступ к коду из других файлов
class Post(models.Model): #определяет наш объект где class - слово для опредления объектов
	                      #post - имя нашей модели
	                      #models.Model -означает что post явл моделью джанго 
	author = models.ForeignKey('auth.User') #ссылка на другую модель 
	title = models.CharField(max_length=200)#определ поле с ограничением на кол-во символов
	text = models.TextField()#тут определяется поле для неограниченно длинного текста
	created_date = models.DateTimeField(
		default=timezone.now) 
	published_date = models.DateTimeField(
		blank=True, null=True)
	

	def publish(self):# деф- создается ф-ция/метод а паблиш - название метода
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title