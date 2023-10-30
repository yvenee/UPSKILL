from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Event(models.Model):
    title = models.CharField(verbose_name="Título", max_length=100) # verbose_name é para aparecer o nome do atributo na view
    description = models.TextField(verbose_name="Descrição", blank=True, null=True) # Por default o campo é NOT NULL
    event_date = models.DateTimeField(verbose_name="Data do Evento")
    create_date = models.DateTimeField(verbose_name="Data da Criação", auto_now=True) # auto_now: hora atual automatica
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Utilizador",)
    active = models.BooleanField(verbose_name="Active",default=False)

    def __str__(self):
        return self.title

# Por default ele cria a tabela dessa forma:
# nomedoapp_nomedaclasse
# ex: core_event
# Para criar uma tabela com nome específico, deve fazer da seguinte forma:
    # dentro da classe da tabela:
    # class Meta:
       # db_table = 'event'   # event = nome desejado
    
    def get_event_date(self):
        return self.event_date.strftime('%d/%m/%Y às %H:%M')
    
    def get_date_input_event(self):
        return self.event_date.strftime('%Y-%m-%dT%H:%M')
    
    def get_late_event(self):
        if self.event_date < datetime.now():
            return True
        else:
            return False

    def delete_old_events():
        two_months_ago = datetime.now() - timedelta(weeks=8)
        Event.objects.filter(active=False, event_date__lt=two_months_ago).delete()
   
   