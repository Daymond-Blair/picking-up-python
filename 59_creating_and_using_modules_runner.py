# 59 creating and using modules runner

''' Program controller Python file '''

import module_one
import module_two
import time

print("3 modules have been imported")

# calling functions direct from a module
module_one.a_function()

# calling a function directly from module 2
module_two.another_function()
time.sleep(1)

# using a class from a module
my_dog = module_one.Dog()  # create 'object' using class 'Dog' located in 'module_one'
my_dog.bark()
my_dog.dog_spawn_window()
