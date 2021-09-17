from django.shortcuts import render
from django.http import HttpResponse
from .forms import PostForm,SendEmail
from django.views import View
# Create your views here.


class IndexClass(View): # Class Based View
    def get(self, request):
        ketqua = "12345"
        return HttpResponse(ketqua)

# def index(request): # Function Based View
#     return HttpResponse("Test for DemoForm")

# def add_post(request):
#     a = PostForm()
#     return render(request, 'news/add_news.html', {'f': a})

class ClassSaveView(View): # This Class = views/add_post + views/save_new
    def get(self, request):
        a = PostForm()
        return render(request, 'news/add_news.html', {'f': a})

    def post(self, request):
            q = PostForm(request.POST)
            if q.is_valid():
                q.save()
                return HttpResponse("Đã lưu thành công!")
            else:
                return HttpResponse("Lưu thất bại!")

# def save_new(request):
#     if request.method == "POST":
#         q = PostForm(request.POST)
#         if q.is_valid():
#             q.save()
#             return HttpResponse("Đã lưu thành công!")
#         else:
#             return HttpResponse("Lưu thất bại!")
#     else:
#         return HttpResponse("Không phải là Post request!")



def email_view(request):
    b = SendEmail()
    return render(request, 'news/email.html', {'mail': b})

# Function to catch Obj
def process(request):
    if request.method == "POST":
        m = SendEmail(request.POST)
        if m.is_valid(): # m had value
            # tieude = m.cleaned_data['title']
            # noidung = m.cleaned_data['content']
            # email = m.cleaned_data['email']
            # cc = m.cleaned_data['cc']
            # context = {'td': tieude, 'c': cc, 'b': noidung, 'e': email}
            context2 = {'email_data': m}
            return render(request, 'news/print_email.html', context2)
        else:
            return HttpResponse("Error!!!")
    else:
        return HttpResponse("This's not a Post Method")