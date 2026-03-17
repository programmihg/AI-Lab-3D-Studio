import subprocess
import sys

def run_script(script_name):
    print(f"--- Изпълнявам {script_name} ---")
    try:
        # Използваме sys.executable, за да сме сигурни, че ползваме същия .venv
        result = subprocess.run([sys.executable, script_name], capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(f"Грешка в {script_name}: {result.stderr}")
    except Exception as e:
        print(f"Неуспешно стартиране на {script_name}: {e}")

if __name__ == "__main__":
    # 1. Обновява флашкартите за преговор
    run_script("collect_cards.py")
    
    # 2. Обновява пътната карта в index.md
    run_script("collect_roadmap.py")
    
    print("✨ Всичко е обновено! Можеш да видиш промените в сайта.")