from django.contrib import admin

# Register your models here.
from tip_tracker_app.models import Tip_Entry, Tip_Type

admin.site.register(Tip_Entry)
admin.site.register(Tip_Type)