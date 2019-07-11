from django.http import Http404 
from django.shortcuts import render, get_object_or_404, redirect
from products.models import Product
from products.forms import ProductForm, RawProductForm

# Create your views here.
def product_detail(request, id):
	# try:
	# 	prod = Product.objects.get(id=id)
	# except Product.DoesNotExist:
	# 	raise Http404
	prod = get_object_or_404(Product, id=id)
	prods = Product.objects.all()

	context = {
		"product": prod,
		"products": prods,
	}
	return render(request, 'product/detail.html', context)

def product_create(request, *args, **kwargs):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = ProductForm()

	context = {
		"form": form
	}
	return render(request, 'product/create.html', context)	

# def product_create(request)	:
# 	form = RawProductForm()
# 	if request.method == "POST": 
# 		form = RawProductForm(request.POST)
# 		if form.is_valid():
# 			print(form.cleaned_data)
# 			Product.objects.create(**form.cleaned_data)
# 		else:
# 			print(form.errors)	
# 		form = RawProductForm()	
# 	context = {
# 		"form":form
# 	}
# 	return render(request, 'product/create.html', context)	

def product_edit(request, *args, **kwargs):
	# Initial data is used when you want a form input to have a default value
	#
	# initial_data = {
	# 	"price": 10
	# }	
	# form = ProductForm(request.POST or None,initial=initial_data)

	product = Product.objects.get(id=1)
	form = ProductForm(request.POST or None,instance=product)
	if form.is_valid():
		form.save()
	
	context = {
		"form": form
	}	
	return render(request, 'product/edit.html', context)	

def product_delete(request, id):
	product = get_object_or_404(Product, id=id)

	if request.method == "POST":
		product.delete()
		return redirect("../../")

	context = {
		"product": product
	}
	return render(request, "product/delete.html", context)	
			