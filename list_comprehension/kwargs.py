def func(names, **kwargs):
    if kwargs.get('reverse_str')== True:
        return [i[::-1].title() for i in names]
    else:
        return [i.title() for i in names]
    
    
name = ['akshi','arhit'] 
print(func(name)) 
print(func(name, reverse_str = True))