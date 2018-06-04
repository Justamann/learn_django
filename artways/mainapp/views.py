from django.shortcuts import render


def main(request):
    title = 'Art Ways'
    return render(request, 'mainapp/index.html',
                  dict(art_title=title, sub='All for your creativity'))


def products(request):
    product_list = ['Pencil', 'Brash', 'Ball', 'Fire-staff', 'Guitar', 'Flute']
    # product_list = []
    return render(request, 'mainapp/products.html', {'products': product_list})


def contact(request):
    return render(request, 'mainapp/contact.html')