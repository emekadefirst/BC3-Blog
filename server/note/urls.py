from django.urls import path
from . import views

urlpatterns = [
    path("", views.main, name="main"),
    path("all/", views.all_note, name="all_notes"),
    path("detail/<int:note_id>/", views.detail_note, name="note_detail"),
    path("create/", views.create_note, name="create_note"),
    path("edit/<int:note_id>/", views.edit_note, name="edit_note"),
    path("delete/<int:note_id>/", views.delete, name="delete_note"),
]
