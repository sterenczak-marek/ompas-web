from datetime import date

from django.db import models
from wagtail.admin.edit_handlers import StreamFieldPanel, RichTextFieldPanel
from wagtail.contrib.settings.models import BaseSetting
from wagtail.contrib.settings.registry import register_setting
from wagtail.core import blocks
from wagtail.core.fields import StreamField, RichTextField
from wagtail.core.models import Page


class HomePage(Page):
    body = StreamField(
        block_types=[
            ('heading', blocks.CharBlock(classname='full title')),
            ('column', blocks.RichTextBlock()),
        ],
        verbose_name="Informacje o wydarzeniu"
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]

class ContactPage(Page):
    body = StreamField(
        block_types=[
            ('heading', blocks.CharBlock(classname='full title')),
            ('text', blocks.RichTextBlock()),
        ],
        verbose_name="Informacje kontaktowe"
    )

    content_panels = Page.content_panels + [
        StreamFieldPanel('body', classname="full"),
    ]


@register_setting(icon='calendar')
class EventSettings(BaseSetting):

    start_date = models.DateField(
        "Data rozpoczęcia turnieju",
        default=date(2018,9,29)
    )
    end_date = models.DateField(
        "Data końca turnieju",
        default=date(2018,9,30)
    )

    facebook = models.URLField(
        "Adres wydarzenia na FB",
        null=True
    )

    class Meta:
        verbose_name = 'Dane wydarzenia'
