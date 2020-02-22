# import module_name

import formatted_name_function

person = formatted_name_function.get_formatted_name('jimi', 'hendrix')
print(person)

person = formatted_name_function.get_formatted_name('john', 'hooker', 'lee')
print(person)

# # from module_name import function name

from formatted_name_function import get_formatted_name

person = get_formatted_name('justin', 'williams', 'morgan')
print(person)

# # from module_name import function_name as fn

from formatted_name_function import get_formatted_name as gfn

person = gfn('ross', 'williams', 'david')
print(person)

# import module_name as mn

import formatted_name_function as fnf

person = fnf.get_formatted_name('allen', 'williams', 'david')
print(person)

# from module_name import *

from formatted_name_function import *

person = get_formatted_name('beth', 'williams', 'vendryes')
print(person)

