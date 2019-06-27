from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, PageChooserPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class BlogIndexPage(Page):

    templates = "templates/myblog/blog_index_page.html"

    blog_index_title = models.CharField(max_length=255, blank=False, null=True)
    blog_index_subtitle = RichTextField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('blog_index_title'),
        FieldPanel('blog_index_subtitle'),
    ]

    def get_context(self, request):
        context = super().get_context(request)
        blogindexpages = super(BlogIndexPage, self).get_context(request)
        blogs = BlogPage.objects.child_of(self).live()
        context = {
            'blogindexpages': blogindexpages,
            'blogs': blogs,
        }
        return context
    

    class Meta:
        verbose_name = "Blog Index Page"
        verbose_name_plural = "Blog Index Pages"

class BlogPage(Page):

    templates = "templates/myblog/blog_page.html"

    blog_title = models.CharField(max_length=255, blank=False, null=True)
    blog_subtitle = models.CharField(max_length=255, blank=False, null=True)
    blog_body = RichTextField(null=True, blank=True)
    blog_content = models.FileField(null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('blog_subtitle'),
        FieldPanel('blog_body'),
        FieldPanel('blog_content'),
    ]

    class Meta:
        verbose_name = "blog Page"
        verbose_name_plural = "Blog  Pages"