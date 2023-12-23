from django.apps import AppConfig


# class ViewsExConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'products'


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'

    def ready(self):
        from . import signals