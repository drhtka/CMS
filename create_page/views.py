from django.shortcuts import render
from create_page.models import ChangePage, CreateTwo, CreatedChildPage, TypePages
# Create your views here.

def create_page(request):

    changepage = ChangePage.objects.all()
    catetwo = CreateTwo.objects.all()
    catechilfrenage = CreatedChildPage.objects.all()
    typechildre = TypePages.objects.all()

    # changepage = ChangePage.objects.filter().values('id', 'name')
    # catetwo = CreateTwo.objects.filter().values('id', 'name')
    # catechilfrenage = CreatedChildPage.objects.filter().values('id', 'name')
    # typechildre = TypePages.objects.filter().values('id', 'name')


    for itemsch in ChangePage, CreateTwo, CreatedChildPage, TypePages:
       print(itemsch)

    return render(request, "create_page/create_page.html", {
        'changepage': changepage,
        'catetwo': catetwo,
        'catechilfrenage': catechilfrenage,
        'typechildre': typechildre,
                                                            })