from django.urls import path
from .admin_panel_views import *
from .views import *



admin_panel_urlpatterns = [
	path('admin_panel', admin_panel),
	path('admin_panel/roles', admin_panel_roles),
	path('admin_panel/categories', admin_panel_product_categories),
	path('admin_panel/categories/delete', admin_panel_delete_category),
	path('admin_panel/tags', admin_panel_tags),
	path('admin_panel/tags/delete', admin_panel_delete_tag),
	path('admin_panel/tags/add', admin_panel_add_tag),
	path('admin_panel/products', admin_panel_products),
	path('admin_panel/products/add', admin_panel_products_add),
	path('admin_panel/products/edit/<int:pid>', admin_panel_edit_product),
	path('admin_panel/remove_tag', admin_panel_remove_product_tag),
	path('admin_panel/add_tag', admin_panel_add_product_tag),
	path('admin_panel/categories/add', admin_panel_add_category),
	path('admin_panel/remove_cat', admin_panel_remove_product_cat),
	path('admin_panel/add_cat', admin_panel_add_product_cat),
	path('admin_panel/delete_product', delete_product),
	path('admin_panel/orders', admin_panel_orders),
	path('admin_panel/delete_order', delete_order),
	path('admin_panel/order/<int:oid>', admin_panel_order),
	path('admin_panel/delete_role/<int:rid>', admin_delete_role),
	path('admin_panel/edit_role/<int:rid>', admin_edit_role),
	path('admin_panel/roles/add', admin_add_role),
	path('admin_panel/orders/edit/<int:id>', admin_edit_order),
	path('admin_panel/upcount', order_upcount),
	path('admin_panel/downcount', order_downcount),
	path('admin_panel/products/add_price', add_price),
	path('admin_panel/ready_projects', admin_ready_projects),
	path('admin_panel/ready_projects/edit/<int:pid>', admin_ready_projects_edit),
	path('admin_panel/delete_project', admin_delete_project),
	path('admin_panel/ready_projects/add', admin_project_add),
	path('admin_panel/delete_ph_proj/<int:phid>', admin_del_ph_proj),
	path('admin_panel/calculated_projects', admin_calculated_projects),
	path('admin_panel/calculated_projects/add', admin_add_calc_project),
	path('admin_panel/calculated_projects/edit/<int:pid>', admin_edit_calc_project),
	path('admin_panel/do_tos', admin_do_tos),
	path('admin_panel/undo_tos', admin_undo_tos)
]

urlpatterns = [
	path('', home),
	path('catalog', catalog),
	path('up_uitp_count', up_uitp_count),
	path('down_uitp_count', down_uitp_count),
	path('add_product_to_trash', add_product_to_trash),
	path('remove_product_from_trash', remove_product_from_trash),
	path('add_order', add_order),
	path('profile', profile),
	path('update_contacts', update_contacts),
	path('orders/<int:oid>', detail_order),
	path('about', about),
	path('trash', trash),
	path('login', login),
	path('logout', logout),
	path('reg', registration),
	path('product/<int:pid>', product_detail),
	path('ready_project/<int:pid>', ready_project_detail),
	path('get_file', get_file),
	path('projects', projects),
	path('calculated_project/<int:id>', calculated_project_details),
	path('tos_projects', tos_projects)
] + admin_panel_urlpatterns
