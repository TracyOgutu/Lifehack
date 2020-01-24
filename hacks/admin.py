from django.contrib import admin
from .models import Profile,Hack,Comments,NewsLetterRecipients,Category

# Register your models here.
admin.site.register(Profile)
admin.site.register(Hack)
admin.site.register(Comments)
admin.site.register(NewsLetterRecipients)
admin.site.register(Category)