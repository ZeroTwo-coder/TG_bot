from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = '5113496906:AAHQYTufMOXgtGhLLQafVq5ZE7rdliQjnPU'  # Забираем значение типа str
ADMINS = '111'  # Тут у нас будет список из админов
IP = '111'  # Тоже str, но для айпи адреса хоста
is_admin = [754851433]
