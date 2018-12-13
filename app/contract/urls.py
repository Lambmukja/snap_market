from django.urls import path

from contract.views import mixin_contract_view, create_contract_view

urlpatterns = [
    path('<int:pk>/', mixin_contract_view, name='contract_mixin'),
    path('market/<int:market_id>/', create_contract_view, name='contract_create'),
]
