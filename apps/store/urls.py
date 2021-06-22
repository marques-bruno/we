from django.urls import path, include
from .views import (
    ajax_set_product_info,
    product_list_view,
    product_detail_view,
    order_summary_view,
    ajax_add_to_cart,
    ajax_remove_item_from_cart,
    ajax_increase_item_from_cart,
    ajax_decrease_item_from_cart,
    ajax_get_product_info,
)

from rest_framework import routers
from .views import (
    OrderView, 
    OrderStatusView, 
    OrderItemView, 
    ProductView, 
    ProductAllergenView, 
    ProductLabelView, 
    ProductTypeView, 
    ProductUnitView, 
    PickupPointView
)

app_name = "store"

router = routers.DefaultRouter()
router.register(r'orders', OrderView, 'order')
router.register(r'order-items', OrderItemView, 'order_item')
router.register(r'order-statuses', OrderStatusView, 'order_status')
router.register(r'products', ProductView, 'product')
router.register(r'product-allergens', ProductAllergenView, 'product_allergen')
router.register(r'product-labels', ProductLabelView, 'product_label')
router.register(r'product-types', ProductTypeView, 'product_type')
router.register(r'product-units', ProductUnitView, 'product_unit')
router.register(r'pickup-points', PickupPointView, 'pickup_point')

urlpatterns = [
    path('products/', product_list_view, name="product_list"),
    path('product/<slug>/', product_detail_view, name="product"),
    path('ajax/add_to_cart/', ajax_add_to_cart, name="add_to_cart"),
    path('ajax/remove-item/', ajax_remove_item_from_cart, name="remove_item"),
    path('ajax/increase-item/', ajax_increase_item_from_cart, name="increase_item"),
    path('ajax/decrease-item/', ajax_decrease_item_from_cart, name="decrease_item"),
    
    path('order-summary/', order_summary_view, name="order_summary"),
    path('api/store/', include(router.urls)),

    path('get/ajax/get-product-info/', ajax_get_product_info, name="get_product_info"),
    path('post/ajax/set-product-info/', ajax_set_product_info, name="set_product_info"),
]
