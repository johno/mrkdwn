from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from notepad.models import Note

def index(request):
    note_list = Note.objects.all()
    return render(request, 'notes/index.html', {'note_list': note_list })

def detail(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/detail.html', {'note': note})

def edit(request, note_id):
    note = get_object_or_404(Note, pk=note_id)
    return render(request, 'notes/edit.html', {'note': note})

def update(request, note_id):
    note = get_object_or_404(Note, pk=note_id)

    note.title   = request.POST['title']
    note.content = request.POST['content']
    note.save()

    return HttpResponseRedirect(reverse('notes:index'))
