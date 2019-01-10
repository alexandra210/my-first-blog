from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Medicine
from .models import Request
from .forms import MedicineForm
from .forms import RequestForm
from django.shortcuts import redirect

def post_list(request):
    search_query = request.GET.get('search', '')

    if search_query:
        posts = Medicine.objects.filter(Название__icontains=search_query)
    else:
        posts = Medicine.objects.order_by('Название')
        
    return render(request, 'blog/post_list.html', {'posts': posts})



def request_list(request):
    lists = Request.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/request_list.html', {'lists': lists})


def post_detail(request, pk):
    post = get_object_or_404(Medicine, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def request_detail(request, pk):
    list = get_object_or_404(Request, pk=pk)
    return render(request, 'blog/request_detail.html', {'list': list} )

def post_new(request):
    if request.method == "POST":
        form = MedicineForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = MedicineForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def request_new(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            list = form.save(commit=False)
            list.published_date = timezone.now()
            list.save()
            return redirect('request_detail', pk=list.pk)
    else:
        form = RequestForm()
    return render(request, 'blog/request_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Medicine, pk=pk)
    if request.method == "POST":
        form = MedicineForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = MedicineForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def request_edit(request, pk):
    post = get_object_or_404(Request, pk=pk)
    if request.method == "POST":
        form = RequestForm(request.POST, instance=post)
        if form.is_valid():
            list = form.save(commit=False)
            list.published_date = timezone.now()
            list.save()
            return redirect('request_detail', pk=list.pk)
    else:
        form = RequestForm(instance=post)
    return render(request, 'blog/request_edit.html', {'form': form})





# Create your views here.
