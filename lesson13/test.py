from pathlib import Path


p = Path('C:/Users/pc/Desktop/заняття/hw_timoha/lesson13')

print(p.parent)
print(p.name)
print(p.suffix)

print(p.exists()) # повертає правду або брехню в залежності чи існує такий файл чи папка
print(p.is_dir()) # повертає правду якщо p вказує на папку, і брехню, якщо на файл
print(p.is_file()) # протилежний метод

print(p.resolve())

for i in p.iterdir():
    print(i.name)
