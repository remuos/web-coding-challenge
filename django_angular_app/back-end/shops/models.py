from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
	titre = models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	img_url = models.CharField(max_length=200)
	pub_date =  models.DateTimeField('date published')

	def __str__(self):
		return self.titre


class Cart(models.Model):
	userId =  models.ForeignKey(User, on_delete=models.CASCADE)
	item_id = models.ForeignKey(Item, related_name='carts', on_delete=models.CASCADE)
	date_creation =  models.DateTimeField()
	class Meta:
		unique_together = ('userId', 'item_id')
		ordering = ['date_creation']
	def __unicode__(self):
		return '%d: %s' % (self.userId, self.date_creation)
		#return {"userId": self.userId,"item_id": self.item_id,"date_creation":self.date_creation}
	def __str__(self):
		return str(self.item_id)

