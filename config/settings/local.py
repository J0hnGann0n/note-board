from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='*e*$w(sb#kdeeb7m@vq%yv7(^l(b^wm_osd!or)!nykvww(^b2')

DEBUG = env.bool('DJANGO_DEBUG', True)