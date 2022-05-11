from django import template


register = template.Library()


@register.filter()
def censor(text):
   return f'{text}!'

'''

BAD_WORDS = ['сурки']


@register.filter()
def censor(text):
   for word in text.split():
       if word.lower() in BAD_WORDS:
           censored = word[0] + "*"*(len(word)-1)
           text = text.replace(word, censored)
           return text

'''