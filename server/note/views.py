from django.shortcuts import render, get_object_or_404, redirect
from .models import Note


# Landing Page
def main(request):
    return render(request, "landing.html")


# View All Notes
def all_note(request):
    notes = Note.objects.all()  # Fetch all notes from the database
    return render(request, "note.html", {"notes": notes})


# View Note Details
def detail_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    return render(request, "edit.html", {"note": note})


# Create Note
def create_note(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        Note.objects.create(title=title, content=content)
        return redirect("all_notes")  # Ensure 'all_notes' is a valid URL name
    return render(request, "edit.html")


# Edit Note
def edit_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if request.method == "POST":
        note.title = request.POST.get("title")
        note.content = request.POST.get("content")
        note.save()
        return redirect("all_notes")
    return render(request, "edit.html", {"note": note})


# Delete Note
def delete(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    note.delete()
    return redirect("all_notes")
