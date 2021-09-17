from django.shortcuts import render, HttpResponse
from django.views import View
from django.contrib.auth import authenticate, login, decorators
from django.contrib.auth.mixins import LoginRequiredMixin # Mixins connect Object together
# Create your views here.


class Indexclass(View):
    def get(self, request):
        return HttpResponse("<h2>Dữ liệu trả lại thành công</h2>")

    def post(self, request):
        pass


class LoginClass(View):
    def get(self, request):
        return render(request, 'login/Login.html')

    def post(self, reqest):
        user_name = reqest.POST.get("username") # take valueable form input name = "username"
        pass_word = reqest.POST.get("password")
        my_user = authenticate(username=user_name, password=pass_word)
        if my_user is None:
            return HttpResponse("Tài khoản đăng nhập ko tồn tại")

        login(reqest, my_user)
        return render(reqest, 'login/success.html')

class ViewUser(LoginRequiredMixin, View): #Authorization for User
    login_url = '/'
    def get(self, request):
            return HttpResponse("<h1>Đây là ViewUser</h1>")


@decorators.login_required(login_url='/') # Use for something need to more faster
def view_product(request):
    return HttpResponse("<h1>Xem Product</h1>")

