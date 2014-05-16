from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the notepad index.")

def detail(request, note_id):
    return HttpResponse("Hello, world. You're at the notepad detail view for note %s" % note_id)

