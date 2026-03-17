import os
import re

def collect_roadmaps():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(base_dir, 'docs')
    index_file = os.path.join(docs_dir, 'index.md')

    all_entries = []
    
    print(f"🔍 Търсене в: {docs_dir}")

    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file == 'roadmap.md':
                full_path = os.path.join(root, file)
                # Пропускаме главния index.md
                if "index.md" in full_path: continue
                
                print(f"📂 Обработка на: {full_path}")
                
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Намираме всички блокове roadmap-entry
                    entries = re.findall(r'<div class="roadmap-entry">.*?</div>\s*</div>', content, re.DOTALL)
                    if not entries:
                        entries = re.findall(r'<div class="roadmap-entry">.*?</div>', content, re.DOTALL)

                    for entry in entries:
                        clean_entry = entry.strip()
                        # АВТОМАТИЧЕН ФИКС ЗА ЗАТВАРЯЩИ ТАГОВЕ
                        open_divs = clean_entry.count('<div')
                        close_divs = clean_entry.count('</div')
                        while open_divs > close_divs:
                            clean_entry += '\n</div>'
                            close_divs += 1
                        
                        all_entries.append(clean_entry)

    # Сортираме записите (най-новите най-отгоре)
    all_entries.sort(reverse=True)

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write("# 🏠 Добре дошли в AI Lab & 3D Studio\n\n")
        f.write("## 🗺️ Последна активност (Глобална Пътна Карта)\n\n")
        
        if not all_entries:
            f.write("*Все още няма намерени записи в локалните roadmap.md файлове.*\n")
        else:
            for entry in all_entries:
                f.write(entry + "\n\n")
            
    print(f"✅ Готово! Индексирани записи: {len(all_entries)}")

if __name__ == "__main__":
    collect_roadmaps()