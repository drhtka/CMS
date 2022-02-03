from django.test import TestCase

# Create your tests here.
fruits = ["Apple", "Pear", "Peach", "Banana"]
fruit_dictionary = {fruit : "In stock" for fruit in fruits}
# print(fruit_dictionary)


tmp_classes =  'TV', 'Clothes'

for classes in tmp_classes:
    aaaa = {'verb_class': classes}
    print(aaaa)

# class_name_append = {classes: 'verb_class' for classes in tmp_classes}