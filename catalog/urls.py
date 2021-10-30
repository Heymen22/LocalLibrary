from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = []
urlpatterns += [ url(r'^$', views.index, name='index') ]
urlpatterns += [ url(r'^books/$', views.BookListView.as_view(), name='books') ]
urlpatterns += [ url(r'^books/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail') ]	
urlpatterns += [ url(r'^authors/$', views.AuthorListView.as_view(), name='authors') ]
urlpatterns += [ url(r'^authors/(?P<pk>\d+)$', views.AuthorDetailView.as_view(), name='author-detail') ]	
urlpatterns += [
    url(r'^book/(?P<pk>[-\w]+)/renew/$', views.renew_book_librarian, name='renew-book-librarian'),
]
urlpatterns += [
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
urlpatterns += [ url(r'^catalog/borrowed/$', views.AllLoanedBooksListView.as_view(), name='all-borrowed') ]
urlpatterns += [
    url(r'^author/create/$', views.AuthorCreate.as_view(), name='author_create'),
    url(r'^author/(?P<pk>\d+)/update/$', views.AuthorUpdate.as_view(), name='author_update'),
    url(r'^author/(?P<pk>\d+)/delete/$', views.AuthorDelete.as_view(), name='author_delete'),
]
urlpatterns += [
    url(r'^book/create/$', views.BookCreate.as_view(), name='book_create'),
    url(r'^book/(?P<pk>\d+)/update/$', views.BookUpdate.as_view(), name='book_update'),
    url(r'^book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book_delete'),
]