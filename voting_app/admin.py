from django.contrib import admin

from .models import Voters,Question,Question_Setter

class VotersAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','vote')
    
class QuestionAdmin(admin.ModelAdmin):
    list_display=('title','question','option1','option2','option3','option4')
    
admin.site.register(Voters,VotersAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(Question_Setter)