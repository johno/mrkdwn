from django.shortcuts import render

from notepad.models import Note

def index(request):
    note_list = Note.objects.all()

    return render(request, 'notes/index.html', {'note_list': note_list })

def detail(request, note_id):
    try:
        note = Note.objects.get(pk=note_id)
    except Note.DoesNotExist:
        raise Http404

    return render(request, 'notes/detail.html', {'note': note})
