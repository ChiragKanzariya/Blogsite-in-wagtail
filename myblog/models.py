from django.db import models
from django import forms

from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from modelcluster.fields import ParentalKey, ParentalManyToManyField

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.models import register_snippet


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
        blogs = BlogPage.objects.child_of(self).live().order_by('-first_published_at')
        context = {
            'blogindexpages': blogindexpages,
            'blogs': blogs,
        }
        return context
    

    class Meta:
        verbose_name = "Blog Index Page"
        verbose_name_plural = "Blog Index Pages"


class BlogTagIndexPage(Page):
    
    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogs = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogs'] = blogs
        return context


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )


class BlogPage(Page):

    templates = "templates/myblog/blog_page.html"

    blog_title = models.CharField(max_length=255, blank=False, null=True)
    blog_subtitle = models.CharField(max_length=255, blank=False, null=True)
    blog_creator_name = models.CharField(max_length=255, blank=False, null=True)
    blog_date = models.DateField("Blog Post date", null=True, blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    blog_categories = ParentalManyToManyField('myblog.BlogCategory', blank=True)
    blog_body = RichTextField(null=True, blank=True)
    blog_content = RichTextField(features=['embed', 'document-link', 'image'], null=True, blank=True)
    

    content_panels = Page.content_panels + [
        FieldPanel('blog_title'),
        FieldPanel('blog_subtitle'),
        FieldPanel('blog_creator_name'),
        MultiFieldPanel([
            FieldPanel('blog_date'),
            FieldPanel('tags'),
            FieldPanel('blog_categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('blog_body'),
        FieldPanel('blog_content'),
        InlinePanel('extra_detail', label="Add Extra blog content ",
                    heading="Blog Extra Content"),
    ]

    class Meta:
        verbose_name = "blog Page"
        verbose_name_plural = "Blog  Pages"


class BlogExtraDetail(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='extra_detail')
    add_subtitle = models.CharField(max_length=255, null=True, blank=True)
    add_more_content = RichTextField(null=True, blank=True)

    panels = [
        FieldPanel('add_subtitle'),
        FieldPanel('add_more_content'),
    ]


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'