# 🚨 Не меняйте код вне зеленой зоны!
guests = []

def invite_friends(list_):
	list_.append(f'Всего гостей приглашено: {len(list_)}')
	print(*list_, sep=' приглашен!\n')

# 🟢 (НАЧАЛО) Напишите ваш код здесь 👇

# 🟢 (КОНЕЦ)

invite_friends(guests)
