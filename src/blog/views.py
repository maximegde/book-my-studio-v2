from django.shortcuts import render

def index(request):
    return render(request, "blog/index.html")


def article(request, numero_article):
    print(numero_article)
    return render(request, f"blog/article_{numero_article}.html")
