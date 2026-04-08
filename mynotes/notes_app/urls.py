"""
notes_app/urls.py (URLs der notes_app-App)
"""

from django.urls import path, include
from notes_app.views import myfunction


urlpatterns = [
    # http://127.0.0.1:8000/notes/myfunction
    path("myfunction", myfunction, name="myfunction"),
]
