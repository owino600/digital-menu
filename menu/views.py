from django.shortcuts import render
from django.db.models import Prefetch

from .models import MenuCategory, MenuItem


def public_menu(request):
    available_items = MenuItem.objects.filter(
        is_available=True
    ).order_by('sort_order', 'name')

    categories = MenuCategory.objects.filter(
        is_active=True,
        items__is_available=True
    ).distinct().order_by('sort_order', 'name').prefetch_related(
        Prefetch(
            'items',
            queryset=available_items,
            to_attr='available_items'
        )
    )

    return render(
        request,
        'menu/public_menu.html',
        {'categories': categories}
    )
