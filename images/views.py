from django.shortcuts import render
from utils import save_to_db

# Create your views here.
def upload_images(request):
    return render(request, 'upload_images.html')

def process_images(request):
    urls_array = request.POST.get('urls_list')
    urls_list=urls_array.split('<br/>')
    del urls_list[-1]
    print("########")
    print(urls_list)
    print("########")
    save_to_db(urls_list)
    return render(request, 'home.html')
