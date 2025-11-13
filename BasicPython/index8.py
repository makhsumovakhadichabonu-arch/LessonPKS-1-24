# Новые темы:
#     Работа с файлами +
#     Тернарный оператор
#     Генератор списков
# №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
# Работа с файлами
# mode = режим:
# r - red - чтение
# w - write - писать - создание нового файла, старый очищает
# a - append
# x - создание нового файла, но если есть такая то вызов


# №№№№№№№№№№№№№№№№№№№№
age = 20
if age >= 18:
    status =" Взрослый"
else:
     status ="несовершеннолетний"
print(status)
################# тернарный
status2= "Взрослый " if age >= 18 else "несовершеннолетний"
print(status2)
##############
n = 5
if n >= 0:
     print("possitive")
else:
     print("negative")
################# тернарный
print("possitive" if n>=0 else "negative")
##################
def bell_to_mark(ball):
     return 'Отлично' if ball>=90 else 'хорошо' if ball >=75 else 'удов' if ball >= 65 else 'неудов'

print(bell_to_mark(76))
######
temperature = -5
print(f"На улице {'тепло' if temperature >0 else 'холодно' }")

#№№№№№№№№№№№№№№№№№№№№№№ Генератор списков
nums =[]
for i in range(100):
     nums.append(i)
     print(nums)
##########
numbers = [i for i in range(100)]
print(numbers)
##########
numbers = [i for i in range (100) if i %2 == 0]
print(numbers)
################

