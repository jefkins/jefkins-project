from django.apps import AppConfig


class CaremarketplaceappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CareMarketplaceApp'

    def ready(self):
        import CareMarketplaceApp.signals

 
 
    
