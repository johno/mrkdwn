from django.shortcuts import render

from notepad.models import Note

def index(request):
    note_list = Note.objects.all()
    context   = {'note_list': note_list }

    return render(request, 'notes/index.html', context)

def detail(request, note_id):
    return HttpResponse("Hello, world. You're at the notepad detail view for note %s" % note_id)
