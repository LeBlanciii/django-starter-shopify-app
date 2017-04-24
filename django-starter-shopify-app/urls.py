from django.conf.urls import url, include

import stats.views

urlpatterns = [
    url(r'login/', include('shopify_auth.urls')),
    url(r'^$', stats.views.home, name='home')
]
