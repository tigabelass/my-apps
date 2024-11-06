from django.shortcuts import render,get_object_or_404
from . import models, forms
from django.http import JsonResponse

# Create your views here.

def note_list(request):
    notes = models.Note.objects.all()
    form = forms.NoteForm()
    context = {
        'notes': notes,
        'form': form,
        'title': 'Your Note',
        'heading': 'Semua Catatan'
    }
    return render(request, 'notes/note_list.html', context)

def add_note(request):
    if request.method == "POST":
        form = forms.NoteForm(request.POST)
        if form.is_valid():
            note = form.save()
            return JsonResponse({
                'id': note.id,
                'title':note.title,
                'content': note.content,
                'create_at': note.create_at.strftime('%Y-%m-%d %H:%M:%S')
            })
    return JsonResponse({'error': 'Invalid form data'}, status=400)