seconds = int(input("Введите время в секундах: "))
minutes = seconds // 60
seconds = seconds % 60
hours = minutes // 60
minutes = minutes % 60
print(f"{hours}:{minutes}:{seconds}")
