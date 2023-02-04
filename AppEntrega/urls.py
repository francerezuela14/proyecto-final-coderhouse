from django.urls import path

from AppEntrega import views

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('', views.inicio, name="Inicio"), 
    path('series', views.serie, name="Series"),
    path('premios', views.premios, name="Premios"),
    path('peliculas', views.peliculas, name="Peliculas"),
    path('login', views.login_request, name="Login"),
    path('register', views.register, name='Register'),
    path('logout', LogoutView.as_view(template_name='AppEntrega/logout.html'), name='Logout'),
    path('peliculas/list', views.PeliculasList.as_view(), name='Peliculas list'),
    path(r'^(?P<pk>\d+)$', views.PeliculasDetalle.as_view(), name='Pelicula detail'),
    path(r'^nuevo$', views.PeliculasCreacion.as_view(), name='Pelicula new'),
    path(r'^editar/(?P<pk>\d+)$', views.PeliculasUpdate.as_view(), name='Pelicula edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PeliculasDelete.as_view(), name='Peliculas delete'),
    path('premios/list', views.PremiosList.as_view(), name='Premios list'),
    path(r'^(?P<pk>\d+)$', views.PremiosDetalle.as_view(), name='Premios detail'),
    path(r'^nuevo$', views.PremiosCreacion.as_view(), name='Premios new'),
    path(r'^editar/(?P<pk>\d+)$', views.PremiosUpdate.as_view(), name='Premios edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.PremiosDelete.as_view(), name='Premios delete'),
    path('series/list', views.SeriesList.as_view(), name='Series list'),
    path(r'^(?P<pk>\d+)$', views.SeriesDetalle.as_view(), name='Series detail'),
    path(r'^nuevo$', views.SeriesCreacion.as_view(), name='Series new'),
    path(r'^editar/(?P<pk>\d+)$', views.SeriesUpdate.as_view(), name='Series edit'),
    path(r'^borrar/(?P<pk>\d+)$', views.SeriesDelete.as_view(), name='Series delete')
]
