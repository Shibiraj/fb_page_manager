from django.db import models
from django.contrib.auth.models import User

class UserPageInfo(models.Model):
	# Stores the user's FB page information
    user = models.ForeignKey(User)
    page_id = models.CharField(max_length=255, default='')
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
		