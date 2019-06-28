from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel


class HomePage(Page):
    
    templates = "templates/home/home_page.html"

    welcome_title = models.CharField(max_length=255, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('welcome_title')
    ]

    class Meta:
        verbose_name = 'Welcome Page'
        verbose_name_plural = 'Welcome Pages'
