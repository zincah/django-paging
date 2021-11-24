from django.shortcuts import render
from .models import Board
from django.core.paginator import Paginator
from django.utils import timezone

# Create your views here.

def index(request):
    page = request.GET.get('page', 1)
    b = Board.objects.all().order_by('-bdate')
    pag = Paginator(b, 10)
    obj = pag.get_page(page)
    context = {
        "blist" : obj,
    }
    return render(request, "board/index.html", context)