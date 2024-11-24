# Human class imported from human.py file
from human import Human

language = 'Python'

# slicing
print(language[0:3])

pto = language[0:6:2]
print(pto)

native = 'Bangladesh'

# 0 menas starting index of the string
# 10 means total number of char in the string
# 3 means select char after first 3 characters in the string
bgdh = native[0:10:3]
print(bgdh)

# string methods
challenge = 'thirty days of python'
print(challenge.capitalize())


tom = Human("tom cruise", "actor")
tom.do_work()
tom.speaks()


maria = Human("maria sharapova", 'tennis player')
maria.do_work()
maria.speaks()
