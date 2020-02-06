from django.contrib import admin
from django.urls import path
from item import views
from item import api
from item.api import filter_view


urlpatterns = [

    path('/', views.items),
    path('/<int:pk>', views.item),
    path('/<int:pk>/status', api.views.status_update),

    path('/delete/<int:pk>', api.views.item_delete),
    path('/filter', filter_view.ItemList.as_view()),
    path('/new_filter', filter_view.query_success),
    path('/custom-filter', api.views.query_status_update),
    path('/date-filter', api.views.get_query_by_date),
    path('/search', api.views.search_item),

    path('/insert', api.views.bulk_insert),
    path('/bulk-loop', api.views.post_post)


]
