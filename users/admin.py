from django.contrib import admin
from .models import UserProfile,Event, Team, College,Match,Result,Result_Many

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'college', 'mobile_number', 'gender']
    search_fields = ['user__username', 'college', 'mobile_number']


admin.site.register(College)
admin.site.register(Event)
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(Result)
admin.site.register(Result_Many)