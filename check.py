import requests
import time
import sys
from bs4 import BeautifulSoup
from colorama import init, Fore, Style

init(autoreset=True)

# --- ТВОИ ОРИГИНАЛЬНЫЕ ФУНКЦИИ (БЕЗ ИЗМЕНЕНИЙ) ---

def print_logo():
    print("\033[H\033[J") 
    print(f"""
{Fore.CYAN}  _____  ______  _____          _____ 
{Fore.CYAN} |  __ \|  ____|/ ____|   /\    / ____|
{Fore.CYAN} | |__) | |__  | |       /  \  | (___       
{Fore.CYAN} |  _  /|  __| | |      / /\ \  \___ \ 
{Fore.CYAN} | | \ \| |____| |____ / ____ \ ____) |
{Fore.CYAN} |_|  \_\______| \____/_/    \_\_____/ 
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣾⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀
    ⢻⣆⠀⠀⠀⠀⠀⠀⠀⢸⣿⡿⠛⠿⣿⡿⠟⠿⡟⣿⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟
    ⠈⢻⣷⣄⠀⠀⠀⠀⠀⠈⢻⣇⢀⣠⡟⢧⣀⣀⣿⡏⠀⠀⠀⠀⠀⠀⣠⣾⡟⠁
    ⠀⠀⠹⣿⣷⣄⠀⠀⠀⠀⠙⣏⢹⣿⣤⣼⣿⢏⡝⠁⠀⠀⠀⠀⣠⣾⣿⠏⠀⠀
    ⠀⠀⠀⠈⠻⣿⣷⣤⡀⠀⠀⢸⡆⠿⠿⠏⠇⣾⠁⠀⠀⢀⣤⣾⣿⠗⠁⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⠛⢷⣿⣶⣄⡈⠻⣿⣿⣿⡿⠋⢀⣠⣶⣿⡿⠛⠁⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢀⣀⠀⠉⠛⠿⣯⣷⣦⣤⣠⣶⣺⣽⠿⠛⠁⠀⣀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⢿⡿⣷⣄⣠⣤⡾⣟⣻⡿⣭⣟⣷⢦⣤⣀⣠⡾⢿⠇⠀⠀⠀⠀⠀
    ⠀⠀⣶⣶⢶⣾⣶⣾⣿⡶⠾⠛⠋⠉⠀⠀⠉⠛⠻⠷⠖⣿⣷⣶⣷⡖⣶⡆⠀⠀
    ⠀⠀⠉⠋⠀⠀⠀⠀⢹⣦⣦⠀⠀⠀⠀⠀⠀⠀⠀⣦⣴⠇⠀⠀⠀⠈⠛⠁⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀
{Fore.YELLOW}          PHONE PARSER v1.6 [RECAS]
    """)

def print_end():
    print(f"""{Fore.BLUE}
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⣿⣿⣿⣧⣤⣤⣄
⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⠏
⠀⠀⣰⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀
⠀⠀⢿⣇⢀⣀⣤⣤⣤⣤⣤⣤⣤⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀
⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀[Результаты найдены]⠀⠀
⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⡕⠀⠈⠛⠛⠿⠿⠿⠿⠿⠿⠿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣼⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣿⢿⣷⠀⠀⠀⠀⠀⠀⠀⠀
⢿⡿⠁⠸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡘⣿⣄⠀⠀⠀⠀⠀⠀⠀
⢸⣇⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣇⡀⠀⠀⠀⠀⠀⠀⠀⠀
        ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀
    [Probix-Recas]
    """)

def loading_animation(duration=1.0, text="Обработка"):
    chars = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    for _ in range(int(duration * 10)):
        for char in chars:
            sys.stdout.write(f'\r{Fore.MAGENTA} {text} {char} ')
            sys.stdout.flush()
            time.sleep(0.01)
    sys.stdout.write('\r' + ' ' * 40 + '\r')

def check_number():
    print_logo()
    print(f"{Fore.WHITE}Введите номер (7xxxxxxxxxx):")
    phone = input(f"{Fore.CYAN}>>> {Fore.YELLOW}").strip().replace("+", "").replace(" ", "")
    if not phone.isdigit():
        print(f"{Fore.RED} Ошибка: Нужны только цифры!")
        return
    url = f"https://кто-звонил7.рф/{phone}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    loading_animation(text="Анализ номера")
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.encoding = 'utf-8'
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            print(f"{Fore.GREEN}[SUCCESS]{Fore.WHITE} Информация по номеру: {Style.BRIGHT}{phone}")
            print(f"{Fore.CYAN}{'━'*50}")
            print(f"{Fore.YELLOW}{'Страна':<12} {Fore.WHITE}│ {Fore.GREEN}Россия")
            items = soup.find_all('div', class_='info-item')
            for item in items:
                l_div = item.find('div', class_='info-label')
                v_div = item.find('div', class_='info-value')
                if l_div and v_div:
                    print(f"{Fore.YELLOW}{l_div.get_text(strip=True):<12} {Fore.WHITE}│ {Fore.GREEN}{v_div.get_text(strip=True)}")
            print_end()
    except Exception as e:
        print(f"{Fore.RED}Ошибка: {e}")

# --- ФУНКЦИЯ ПАРСИНГА ФШР ---

def check_fshr():
    print(f"\n{Fore.WHITE}Введите ID ФШР:")
    fshr_id = input(f"{Fore.CYAN}>>> {Fore.YELLOW}").strip()
    
    url = f"https://ratings.ruchess.ru/people/{fshr_id}"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    loading_animation(text="Парсинг ФШР")

    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            player_name = soup.find('h1').get_text(strip=True) if soup.find('h1') else "Неизвестно"
            
            print(f"{Fore.GREEN}[FSHR SUCCESS]{Fore.WHITE} Игрок: {player_name}")
            print(f"{Fore.CYAN}{'━'*50}")

            items = soup.find_all('li', class_='list-group-item')
            for item in items:
                text = item.get_text(" ", strip=True)
                if "ФШР ID" in text:
                    print(f"{Fore.YELLOW}{'ФШР ID':<12} {Fore.WHITE}│ {Fore.CYAN}{text.split(':')[-1].strip()}")
                elif "Пол" in text:
                    print(f"{Fore.YELLOW}{'Пол':<12} {Fore.WHITE}│ {Fore.WHITE}{text.split(':')[-1].strip()}")
                elif "Регион" in text:
                    reg = text.split(':')[-1].replace('\n', ' ').strip()
                    print(f"{Fore.YELLOW}{'Регион':<12} {Fore.WHITE}│ {Fore.WHITE}{reg}")
                elif "Год рождения" in text:
                    print(f"{Fore.YELLOW}{'Год рожд.':<12} {Fore.WHITE}│ {Fore.WHITE}{text.split(':')[-1].strip()}")
        else:
            print(f"{Fore.RED}[!] Ошибка: ID не найден.")
    except Exception as e:
        print(f"{Fore.RED}[!] Ошибка соединения: {e}")

# --- ГЛАВНОЕ МЕНЮ (ОБНОВЛЕНО) ---

if __name__ == "__main__":
    while True:
        print_logo()
        print(f"{Fore.WHITE}1. Пробить ТЕЛЕФОН")
        print(f"{Fore.WHITE}2. Пробить ФШР ID (Шахматисты)")
        print(f"{Fore.WHITE}3. Пробить ВСЁ СРАЗУ (Тел + ФШР)")
        
        choice = input(f"\n{Fore.CYAN}Выбор (1-3): {Fore.YELLOW}").strip()

        if choice == '1':
            check_number()
        elif choice == '2':
            check_fshr()
        elif choice == '3':
            check_number()
            check_fshr()
        else:
            print(f"{Fore.RED}Неверный выбор.")

        print(f"\n{Fore.CYAN}{'━'*50}")
        if input(f"{Fore.WHITE}Вернуться в меню? (y/n): ").lower() != 'y':
            print(f"{Fore.MAGENTA}До встречи!")
            break
