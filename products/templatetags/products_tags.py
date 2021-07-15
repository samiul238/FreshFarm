from django import template
from base.views import printer
from products.models import ReplyReview

register = template.Library()


@register.filter
def evaler(lst):
    return eval(lst)


@register.filter
def reply(review):
    replies = ReplyReview.objects.filter(review=review)
    replies = list(replies)
    replies.reverse()
    return replies
