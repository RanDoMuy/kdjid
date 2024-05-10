from django.apps import AppConfig


class WealthOriginAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wealth_origin_app'

    #def ready(self):
        #from . import updater
        #updater.start()

