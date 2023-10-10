from django.urls import include
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Rutas para el modelo Autobus
    path('autobuses/', views.AutobusListCreate.as_view(), name='autobus-list-create'),
    path('autobuses/<int:pk>/', views.AutobusRetrieveUpdateDestroy.as_view(), name='autobus-retrieve-update-destroy'),

    # Rutas para el modelo Horario
    path('horarios/', views.HorarioListCreate.as_view(), name='horario-list-create'),
    path('horarios/<int:pk>/', views.HorarioRetrieveUpdateDestroy.as_view(), name='horario-retrieve-update-destroy'),

    # Rutas para el modelo ProgramacionAutobuses
    path('programacion-autobuses/', views.ProgramacionAutobusesListCreate.as_view(), name='programacion-autobuses-list-create'),
    path('programacion-autobuses/<int:pk>/', views.ProgramacionAutobusesRetrieveUpdateDestroy.as_view(), name='programacion-autobuses-retrieve-update-destroy'),

    # Rutas para el modelo Cargador
    path('cargadores/', views.CargadorListCreate.as_view(), name='cargador-list-create'),
    path('cargadores/<int:pk>/', views.CargadorRetrieveUpdateDestroy.as_view(), name='cargador-retrieve-update-destroy'),

    # Rutas para el modelo ProgramacionCargadores
    path('programacion-cargadores/', views.ProgramacionCargadoresListCreate.as_view(), name='programacion-cargadores-list-create'),
    path('programacion-cargadores/<int:pk>/', views.ProgramacionCargadoresRetrieveUpdateDestroy.as_view(), name='programacion-cargadores-retrieve-update-destroy'),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),

]
