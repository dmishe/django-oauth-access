from django.contrib import admin

from oauth_access.models import UserAssociation

admin.site.register(UserAssociation, list_display=['user', 'service'])