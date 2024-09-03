import subprocess

# Откройте файл requirements.txt и прочитайте пакеты
with open('requirements.txt', 'r') as file:
    packages = file.read().splitlines()

# Установите каждый пакет с помощью poetry add
for package in packages:
    subprocess.run(['poetry', 'add', package])
