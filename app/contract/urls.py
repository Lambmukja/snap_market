from django.urls import path

from contract.views import contract_page_view, create_contract_view

urlpatterns = [
    path('<int:pk>/', contract_page_view, name='contract_page'),
    path('market/<int:market_id>/', create_contract_view, name='contract_create'),
]
