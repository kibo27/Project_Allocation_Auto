from django.contrib import admin
from django.urls import path
from django.http import HttpResponseRedirect
from .models import Faculty,student,choice
from .forms import choices
# Register your models here.


class studentAdmin(admin.ModelAdmin):
    list_display =('user','name','cpi','gender')
    list_filter =('gender',)
    change_list_template='admin/student_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('immortal/', self.set_immortal),
            path('mortal/', self.set_mortal),
            path('resul/',self.set_result),
        ]
        return my_urls + urls

    def set_immortal(self, request):
        self.model.objects.all().update(to=True)
        self.message_user(request, "All heroes are now immortal")
        return HttpResponseRedirect("../")

    def set_mortal(self, request):
        self.message_user(request, "All heroes are now mortal")
        self.model.objects.all().update(to=False)
        return HttpResponseRedirect("../")


    def set_result(self, request):
        self.message_user(request, "Result is declared")
        x=self.model.objects.order_by('-cpi')
        form =choices()
        for i in x:
            ch=choice.objects.get(student=i)
            for j in form.fields:
                cd=getattr(ch,j)
                fac=Faculty.objects.get(id=cd)
                if(fac.saa == False):
                    i.sa=fac
                    i.fac_allocated=True
                    fac.sa=i.regno
                    fac.saa=True
                    i.save()
                    fac.save()
                    break
                elif(fac.sba == False):
                    i.sa=fac
                    i.fac_allocated=True
                    fac.sb=i.regno
                    fac.sba=True
                    i.save()
                    fac.save()
                    break
                elif(fac.sca == False):
                    i.sa=fac
                    i.fac_allocated=True
                    fac.sc=i.regno
                    fac.sca=True
                    i.save()
                    fac.save()
                    break
                else:
                    continue
        return HttpResponseRedirect("../")


class choiceAdmin(admin.ModelAdmin):
    list_display =('student','cfilled')

admin.site.register(Faculty)
admin.site.register(student,studentAdmin)
admin.site.register(choice,choiceAdmin)