from django.contrib.humanize.templatetags.humanize import intcomma
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseNotFound, JsonResponse, FileResponse
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.conf import settings

from random import choice

from .forms import *
from .models import *
from .utils import *


# Create your views here.
def home(request):

	projects = Ready_project.objects.all()
	if len(projects) > 4:
		projects = projects[:4]


	class Projs:
		def __init__(self, project):
			self.project = project
			self.photo = ''
			for ph in Project_photo.objects.filter(project=project):
				if ph.photo:
					self.photo = ph.photo.url
					break

	projects = [Projs(x) for x in projects]

	return render(request, 'new_ui/home.html', {
		'projects': projects
	})




@csrf_exempt
def catalog(request):

	class Pinfo:
		def __init__(self, prod):
			self.name = prod.name
			self.id = prod.id
			self.price = prod.price
			self.photo = ''
			if prod.photo:
				self.photo = prod.photo.url

			if request.user.is_authenticated:
				self.in_trash = len(UserTrash.objects.filter(user=request.user, product=prod)) > 0

				if self.in_trash:
					self.in_trash_count = UserTrash.objects.filter(user=request.user, product=prod).first().pcount

			else:
				self.in_trash = False

	all_cats = Category.objects.all()

	if request.method == 'GET':

		products = Product.objects.all()
		products = [Pinfo(x) for x in products]

		return render(request, 'new_ui/catalog.html', {
			'cats': all_cats,
			'products': products,
			'cat_id' : -1,
			'code_ch' : 'False',
			'n_ch' : 'False',
			'a_s_ch' : 'False',
			'a_e_ch' : 'False',
			'h_s_ch' : 'False',
			'h_e_ch' : 'False',
			'w_s_ch' : 'False',
			'w_e_ch' : 'False',
			'l_s_ch' : 'False',
			'l_e_ch' : 'False',
			'price_s_ch' : 'False',
			'price_e_ch' : 'False'
		})

	elif request.method == 'POST':

		products = Product.objects.all()
		producttags = ProductTag.objects.all()

		cat_id = -1
		code_ch = 'False'
		n_ch = 'False'
		a_s_ch = 'False'
		a_e_ch = 'False'
		h_s_ch = 'False'
		h_e_ch = 'False'
		w_s_ch = 'False'
		w_e_ch = 'False'
		l_s_ch = 'False'
		l_e_ch = 'False'
		price_s_ch = 'False'
		price_e_ch = 'False'



		if request.POST['cat']:
			cat_id = request.POST['cat']
		if request.POST['code_ch']:
			code_ch = request.POST['code_ch']
		if request.POST['n_ch']:
			n_ch = request.POST['n_ch']
		if request.POST['a_s_ch']:
			a_s_ch = request.POST['a_s_ch']
		if request.POST['a_e_ch']:
			a_e_ch = request.POST['a_e_ch']
		if request.POST['h_s_ch']:
			h_s_ch = request.POST['h_s_ch']
		if request.POST['h_e_ch']:
			h_e_ch = request.POST['h_e_ch']
		if request.POST['w_s_ch']:
			w_s_ch = request.POST['w_s_ch']
		if request.POST['w_e_ch']:
			w_e_ch = request.POST['w_e_ch']
		if request.POST['l_s_ch']:
			l_s_ch = request.POST['l_s_ch']
		if request.POST['l_e_ch']:
			l_e_ch = request.POST['l_e_ch']
		if request.POST['price_s_ch']:
			price_s_ch = request.POST['price_s_ch']
		if request.POST['price_e_ch']:
			price_e_ch = request.POST['price_e_ch']

		if cat_id:

			if cat_id.isdigit():
				cat_id = int(cat_id)
				if cat_id != -1:
					products = [x.product for x in ProductCategory.objects.filter(category=Category.objects.get(id=cat_id))]


		if code_ch != 'False':
			products = [x for x in products if code_ch.lower() in x.product_code.lower()]


		if n_ch != 'False':
			pre_products = []
			for product in products:
				if n_ch.lower() in product.name.lower():
					pre_products.append(product)
				else:
					for pt in producttags.filter(product=product):
						if pt.tag.name.lower().startswith(n_ch.lower()):
							pre_products.append(product)
							break

			products = pre_products

		if a_s_ch != 'False':
			if a_s_ch.isdigit():
				products = [x for x in products if x.age_start and x.age_start >= int(a_s_ch)]


		if a_e_ch != 'False':
			if a_e_ch.isdigit():
				products = [x for x in products if x.age_start and x.age_start <= int(a_e_ch)]


		if h_s_ch != 'False':
			if h_s_ch.isdigit():
				products = [x for x in products if x.height and x.height >= int(h_s_ch)]


		if h_e_ch != 'False':
			if h_e_ch.isdigit():
				products = [x for x in products if x.height and x.height <= int(h_e_ch)]


		if w_s_ch != 'False':
			if w_s_ch.isdigit():
				products = [x for x in products if x.width and x.width >= int(w_s_ch)]


		if w_e_ch != 'False':
			if w_e_ch.isdigit():
				products = [x for x in products if x.width and x.width <= int(w_e_ch)]


		if l_s_ch != 'False':
			if l_s_ch.isdigit():
				products = [x for x in products if x.length and x.length >= int(l_s_ch)]


		if l_e_ch != 'False':
			if l_e_ch.isdigit():
				products = [x for x in products if x.length and x.length <= int(l_e_ch)]


		if price_s_ch != 'False':
			if price_s_ch.isdigit():
				products = [x for x in products if x.price >= int(price_s_ch)]


		if price_e_ch != 'False':
			if price_e_ch.isdigit():
				products = [x for x in products if x.price <= int(price_e_ch)]


		products = [Pinfo(x) for x in products]

		return render(request, 'new_ui/catalog.html', {
			'cats': all_cats,
			'products': products,
			'cat_id': int(cat_id),
			'code_ch': code_ch,
			'n_ch': n_ch,
			'a_s_ch': a_s_ch,
			'a_e_ch': a_e_ch,
			'h_e_ch': h_e_ch,
			'h_s_ch': h_s_ch,
			'w_s_ch': w_s_ch,
			'w_e_ch': w_e_ch,
			'l_s_ch': l_s_ch,
			'l_e_ch': l_e_ch,
			'price_s_ch': price_s_ch,
			'price_e_ch': price_e_ch
		})


@csrf_exempt
def up_uitp_count(request):
	if request.method == 'POST':

		uid = int(request.POST['uid'])
		pid = int(request.POST['pid'])

		trash = UserTrash.objects.get(user__id=uid, product__id=pid)
		trash.pcount += 1
		trash.save()

		sm = intcomma(str(sum([x.product.price * x.pcount for x in UserTrash.objects.filter(user__id=uid)]))).replace(
			',', ' ')

		return JsonResponse({
			'sm': sm,
			'in_trash': True,
			'count': trash.pcount
		}, status=200)


@csrf_exempt
def down_uitp_count(request):
	if request.method == 'POST':

		uid = int(request.POST['uid'])
		pid = int(request.POST['pid'])

		trash = UserTrash.objects.get(user__id=uid, product__id=pid)
		tp = trash.id
		in_trash = True

		if trash.pcount == 1:
			in_trash = False
			trash.delete()
		elif trash.pcount > 1:
			trash.pcount -= 1
			trash.save()

		sm = intcomma(str(sum([x.product.price * x.pcount for x in UserTrash.objects.filter(user__id=uid)]))).replace(',', ' ')

		if in_trash:
			return JsonResponse({
				'sm': sm,
				'in_trash': in_trash,
				'count': trash.pcount,
				'tp': tp
			}, status=200)
		return JsonResponse({
			'sm': sm,
			'in_trash': in_trash,
			'tp': tp
		}, status=200)


@login_required
@csrf_exempt
def remove_product_from_trash(request):
	if request.method == 'POST':

		pid = int(request.POST.get('pid'))

		trash = UserTrash.objects.filter(id=pid)

		trash.delete()

		sm = intcomma(str(sum([x.product.price * x.pcount for x in UserTrash.objects.filter(id=pid)]))).replace(
			',', ' ')

		return JsonResponse({
			'sm': sm
		}, status=200)



@csrf_exempt
def add_product_to_trash(request):
	if request.method == 'POST':

		try:
			prod = Product.objects.get(id=int(request.POST['pid']))

			UserTrash.objects.create(
				user=request.user,
				product=prod,
				pcount=1
			)

			return JsonResponse({}, status=200)

		except:
			return JsonResponse({}, status=500)


def about(request):
	return render(request, 'new_ui/about.html')


def trash(request):
	products = UserTrash.objects.filter(user=request.user)
	total_sum = sum([x.product.price * x.pcount for x in products])

	user_contacts = False
	if request.user.is_authenticated:
		if request.user.email:
			user_contacts = True
		if request.user.phone_number:
			user_contacts = True

	return render(request, 'new_ui/trash.html', {
		'user_contacts': user_contacts,
		'products': products,
		'pcount': len(products),
		'total_sum': total_sum
	})


@login_required
@csrf_exempt
def add_order(request):
	if request.method == 'POST':

		uid = int(request.POST['uid'])

		if uid == request.user.id:

			contacts = ''

			if request.user.email:
				contacts += f'email: {request.user.email} '
			if request.user.phone_number:
				contacts += f'Номер телефона: {request.user.phone_number} '

			is_good = True

			try:
				order = Order.objects.create(
					user=request.user,
					contacts=contacts,
					total_price=sum([x.product.price * x.pcount for x in UserTrash.objects.filter(user=request.user)])
				)

				for prod in UserTrash.objects.filter(user=request.user):
					OrderElement.objects.create(
						order=order,
						product=prod.product,
						pcount=prod.pcount,
						total_price=prod.product.price * prod.pcount,
					)
			except Exception as e:
				is_good = False
				return JsonResponse({}, status=500)

			if is_good:
				UserTrash.objects.filter(user=request.user).delete()
				return JsonResponse({}, status=200)

			return JsonResponse({}, status=500)

		else:
			return JsonResponse({}, status=500)


@login_required
def profile(request):

	orders = Order.objects.filter(user=request.user).order_by('-status', '-create_at')

	return render(request, 'new_ui/profile.html', {
		'orders': orders
	})


@login_required
@csrf_exempt
def update_contacts(request):
	if request.method == 'POST':

		try:
			email = request.POST['email']
			phone = int(request.POST['phone_number'])

			request.user.phone_number = phone
			request.user.email = email

			request.user.save()

			return JsonResponse({}, status=200)
		except:
			return JsonResponse({}, status=500)


@login_required
def detail_order(request, oid):
	order = Order.objects.get(id=oid)

	if order.user == request.user:

		items = OrderElement.objects.filter(order=order)
		ts = sum([x.total_price for x in items])
		tpcount = sum([x.pcount for x in items])

		return render(request, 'new_ui/order_detail.html', {
			'order': order,
			'items': items,
			'ts': ts,
			'tpcount': tpcount
		})

	else:
		return HttpResponse(status=404)


def login(request):
	if request.method == 'GET':
		return render(request, 'new_ui/login_page.html')
	elif request.method == 'POST':
		username = request.POST["username"]
		password = request.POST["password"]
		usr = authenticate(request, username=username, password=password)
		if usr is not None:
			user_login(request, usr)
			return HttpResponseRedirect('/')
		else:
			return render(request, 'new_ui/login_page.html')


def logout(request):
	user_logout(request)
	return HttpResponseRedirect('/')


def registration(request):
	if request.method == 'GET':
		return render(request, 'new_ui/reg.html', {
			'form': RegForm()
		})
	elif request.method == 'POST':
		form = RegForm(request.POST)
		if form.is_valid():

			username = form.cleaned_data['username']
			email = form.cleaned_data['email']
			psw1 = form.cleaned_data['password']
			psw2 = form.cleaned_data['password2']

			if psw1 == psw2:

				user = CustomUser.objects.create_user(username=username, email=email, password=psw1)
				user.set_password(psw1)
				user.save()

				user_login(request, user)
				return HttpResponseRedirect('/')

			else:
				return render(request, 'new_ui/reg.html', {
					'form': form
				})

		else:
			return render(request, 'new_ui/reg.html', {
				'form': form
			})


def product_detail(request, pid):

	class Pinfo:
		def __init__(self, prod):
			self.product = prod

			if request.user.is_authenticated:
				self.in_trash = len(UserTrash.objects.filter(user=request.user, product=self.product)) > 0

				if self.in_trash:
					self.in_trash_count = UserTrash.objects.filter(user=request.user, product=self.product).first().pcount

			else:
				self.in_trash = False

	product = Pinfo(get_object_or_404(Product, id=pid))
	return render(request, 'new_ui/product_detail.html', {'product': product})


def ready_project_detail(request, pid):

	class Proj:
		def __init__(self, project):
			self.project = project
			self.photos = []
			self.video = ''

			if self.project.video:
				if os.path.exists(self.project.video.path):
					self.video = self.project.video.url

			for ph in Project_photo.objects.filter(project=project):
				if ph.photo:
					self.photos.append(ph.photo.url)

	return render(request, 'new_ui/ready_project_detail.html', {'project': Proj(get_object_or_404(Ready_project, id=pid))})


@csrf_exempt
def get_file(request):
	if request.GET:
		try:
			url = request.GET.get('url')

			file = open(os.path.join(settings.BASE_DIR, url.replace('/', '', 1)), 'rb')

			return FileResponse(file, as_attachment=True, filename=url.replace('/media/projects_files/', '', 1))
		except:
			return HttpResponseNotFound(request)


def projects(request):
	class RProject:
		def __init__(self, project):
			self.id = project.id
			self.price = project.price
			self.name = project.name
			for ph in Project_photo.objects.filter(project=project):
				if ph.photo:
					self.photo = ph.photo.url
	class CProject:
		def __init__(self, project):
			self.id = project.id
			self.price = project.price
			self.name = project.name
			for ph in Calculated_project_photo.objects.filter(project=project):
				if ph.photo:
					self.photo = ph.photo.url
	return render(request, 'new_ui/projects.html', {
		'ready_projects': [RProject(x) for x in Ready_project.objects.all()],
		'calculated_projects': [CProject(x) for x in Calculated_project.objects.all()]
	})


def calculated_project_details(request, id):
	project = get_object_or_404(Calculated_project, id=id)
	photos = []
	file = ''
	if project.file:
		if os.path.exists(project.file.path):
			file = project.file.url


	for ph in Calculated_project_photo.objects.filter(project=project):
		if ph.photo:
			photos.append(ph.photo.url)
	return render(request, 'new_ui/calculated_project_detail.html', {'project': project, 'photos': photos, 'file': file})
