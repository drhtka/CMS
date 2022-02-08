# -*- coding: utf-8 -*-
from django import forms
from shop.models import Category, Promo, Brands, Item, Dishwasher, Notebook, VacuumCleaner, TV, Clothes


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category


class NotebookForms(forms.ModelForm):

    class Meta:
        model = Notebook

