from os import system, getenv
from dotenv import load_dotenv
from sys import argv
from time import sleep

load_dotenv()

def menu():
    print("1. Start API")
    
def start_api(port):
    try:
        port = input("Insira a porta para a API (default 8000): ") or "8000"
        print("Iniciando API...")
        system(f"python manage.py runserver 0.0.0.0:{port}")
    except KeyboardInterrupt:
        print("\n\tAPI encerrada pelo usuário.")

while True:
    menu()
    choice = input("Selecione uma opção (ou 'sair' para sair): ")
    if choice == '1':
        start_api(argv[0])
    elif choice == '2':
        print(f"="*25)
        print(f'| DB Host..: {getenv("DB_HOST").ljust(11)}|')
        print(f'| DB User..: {getenv("DB_USER").ljust(11)}|')
        print(f'| DB Port..: {getenv("DB_PORT").ljust(11)}|')
        print('='*25)
    elif choice.lower() in ['s', 'sair']:
        break
    else:
        print("Opção inválida. Tente novamente.")
