# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from app.views import domain,maps,moreinfo,inventory,SRs

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('domain/', domain),
    path('maps/', maps),
    path('moreinfo/<int:id>', moreinfo),
    path('inventory/<int:id>', inventory),
    path('SRs/<int:id>', SRs),
    #path('mapa_coord/', mapa_coord),
    

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
