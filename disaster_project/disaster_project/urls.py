"""disaster_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path
from first_app import views
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',views.index, name= 'index'),
    path('help/',views.help, name= 'help'),
    path('AboutUs/',views.AboutUs, name= 'AboutUs'),
    path('Contact/',views.Contact, name= 'Contact'),
    path('Home/',views.Home, name= 'Home'),
    path('LogIn/',views.NewLogin, name= 'LogIn'),
    path('Base/',views.Base, name= 'Base'),
    path('adminPannel/',views.adminPannel, name= 'adminPannel'),
    path('changePass/',views.changePass, name= 'changePass'),
    path('editProfile/',views.editProfile, name= 'editProfile'),
    path('helpSupport/',views.helpSupport, name= 'helpSupport'),
    path('review/',views.review, name= 'review'),
    path('Dashboard/',views.Dashboard, name= 'Dashboard'),
    path('TypesOfDisaster/',views.viewTypesOfDisaster, name= 'TypesOfDisaster'),
    path('Organization/',views.viewOrganization, name= 'Organization'),
    path('Blog/',views.viewBlog, name= 'Blog'),
    path('Post/',views.Post, name= 'Post'),
    path('fileUpload/',views.Post, name= 'fileUpload'),
    path('NatDisV/',views.NatDisV, name= 'NatDisV'),
    path('NatDisVDynamic/',views.NatDisVDynamic, name= 'NatDisVDynamic'),
    path('DeathNatDis/',views.DeathNatDis, name= 'DeathNatDis'),
    path('DirDisGdp/',views.DirDisGdp, name= 'DirDisGdp'),
    path('Global/',views.Global, name= 'Global'),
    path('GlobPreci/',views.GlobPreci, name= 'GlobPreci'),
    path('place/',views.place, name= 'place'),
    path('GlobPreciDynamic',views.GlobPreciDynamic, name='GlobPreciDynamic'),
    path('DynamicVisual',views.DynamicVisual, name='DynamicVisual'),
    path('YearCountNatDisV',views.YearCountNatDisV, name='YearCountNatDisV'),
    path('TwoDisasYear',views.TwoDisasYear, name='TwoDisasYear'),
    path('DathDynamic',views.DathDynamic, name='DathDynamic'),
    path('DeathCoun',views.DeathCoun, name='DeathCoun'),
    path('YearDeath',views.YearDeath, name='YearDeath'),
    path('Forgot',views.Forgot, name='Forgot'),
    path('twoCountDeath',views.twoCountDeath, name='twoCountDeath'),
    path('DgdpDynamic',views.DgdpDynamic, name='DgdpDynamic'),
    path('DgdpCount',views.DgdpCount, name='DgdpCount'),
    path('YearDgdp',views.YearDgdp, name='YearDgdp'),
    path('twoCountDgdp',views.twoCountDgdp, name='twoCountDgdp'),
    path('InternalDisDynamic',views.InternalDisDynamic, name='InternalDisDynamic'),
    path('InternalCount',views.InternalCount, name='InternalCount'),
    path('YearInternalDis',views.YearInternalDis, name='YearInternalDis'),
    path('MaxInter',views.MaxInter, name='MaxInter'),
    path('MinInter',views.MinInter, name='MinInter'),
    path('Top5Inter',views.Top5Inter, name='Top5Inter'),
    path('twoInternalDis',views.twoInternalDis, name='twoInternalDis'),
    path('NewRegister',views.NewRegister, name='NewRegister'),
    path('Map',views.Map, name='Map'),
    path('VolcaMap',views.VolcaMap, name='VolcaMap'),
    path('MinNatDis',views.MinNatDis, name='MinNatDis'),
    path('MaxNatDis',views.MaxNatDis, name='MaxNatDis'),
    path('Top5NatDis',views.Top5NatDis, name='Top5NatDis'),
    path('MaxDeath',views.MaxDeath, name='MaxDeath'),
    path('MinDeath',views.MinDeath, name='MinDeath'),
    path('Top5Death',views.Top5Death, name='Top5Death'),
    path('earthform',views.earthform, name='earthform'),
    path('Globalgdp',views.Globalgdp, name='Globalgdp'),
    path('MaxDgdp',views.MaxDgdp, name='MaxDgdp'),
    path('MinDgdp',views.MinDgdp, name='MinDgdp'),
    path('Top5Dgdp',views.Top5Dgdp, name='Top5Dgdp'),
    path('MaxGlobgdp',views.MaxGlobgdp, name='MaxGlobgdp'),
    path('MinGlobgdp',views.MinGlobgdp, name='MinGlobgdp'),
    path('Top5Globgdp',views.Top5Globgdp, name='Top5Globgdp'),
    path('Subscribe',views.subscribe, name='Subscribe'), 
    path('LoginAdmin',views.LoginAdmin, name='LoginAdmin'),
    path('SubsAdmin',views.SubsAdmin, name='SubsAdmin'),
    path('MaxGlobPreci',views.MaxGlobPreci, name='MaxGlobPreci'),
    path('MinGlobPreci',views.MinGlobPreci, name='MinGlobPreci'),
    path('Top5GlobPreci',views.Top5GlobPreci, name='Top5GlobPreci'),
    path('Users',views.Users, name='Users'), 
    path('SendNot',views.SendNot, name='SendNot'), 
    path('NotificationSent',views.NotificationSent, name='NotificationSent'),
    
    path('viewBlogdetail/<int:id>',views.viewBlogdetail,name='viewBlogdetail'),
    path('viewTypesOfDisasterdetail/<int:id>',views.viewTypesOfDisasterdetail,name='viewTypesOfDisasterdetail'),
    path('viewOrganizationdetail/<int:id>',views.viewOrganizationdetail,name='viewOrganizationdetail'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

