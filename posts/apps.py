from django.apps import AppConfig


class PostsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'posts'

    def ready(self):
        import posts.signals


# fa9f6409e47f789ea06c40334c7af991f6a14dfe
# fa9f6409e47f789ea06c40334c7af991f6a14dfe
