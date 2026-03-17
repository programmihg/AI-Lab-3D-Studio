import os
import re

def collect_roadmaps():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    docs_dir = os.path.join(base_dir, 'docs')
    index_file = os.path.join(docs_dir, 'index.md')

    active_entries = []
    archived_entries = []
    
    icons = {
        "python": "🐍",
        "github": "🐙",
        "3d": "📦",
        "ai": "🤖",
        "модел": "🧠",
        "интеграция": "🔗",
        "флашкарт": "🃏"
    }

    if not os.path.exists(docs_dir): return

    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file == 'roadmap.md' and "index.md" not in root:
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    entries = re.findall(r'<div class="roadmap-entry">.*?</div>\s*</div>', content, re.DOTALL)
                    if not entries:
                        entries = re.findall(r'<div class="roadmap-entry">.*?</div>', content, re.DOTALL)

                    for entry in entries:
                        clean_entry = entry.strip()
                        
                        # Добавяне на икона
                        for key, icon in icons.items():
                            if key in clean_entry.lower():
                                clean_entry = clean_entry.replace('class="milestone">', f'class="milestone">{icon} ')
                                break
                        
                        # Групиране: Активни срещу Архив
                        if "архив" in clean_entry.lower() or "completed" in clean_entry.lower():
                            archived_entries.append(clean_entry)
                        else:
                            active_entries.append(clean_entry)

    # Статистика
    total = len(active_entries) + len(archived_entries)
    percent = int((len(archived_entries) / total) * 100) if total > 0 else 0

    active_entries.sort(reverse=True)
    archived_entries.sort(reverse=True)

    with open(index_file, 'w', encoding='utf-8') as f:
        f.write("# 🏠 AI Lab & 3D Studio Dashboard\n\n")
        
        # Лента със статистика
        f.write(f'<div style="background: #252538; padding: 15px; border-radius: 10px; border: 1px solid #444; margin-bottom: 20px; display: flex; justify-content: space-around; align-items: center;">')
        f.write(f'<span>📊 <b>Общо задачи:</b> {total}</span>')
        f.write(f'<span>✅ <b>Завършени:</b> {len(archived_entries)}</span>')
        f.write(f'<span>📈 <b>Прогрес:</b> {percent}%</span>')
        f.write(f'</div>\n\n')

        f.write('<input type="text" id="roadmap-search" placeholder="🔍 Търси в историята..." style="width:100%; padding:12px; border-radius:10px; border:1px solid #444; background:#252538; color:white; margin-bottom:20px;">\n\n')
        
        f.write("## 🚀 Активни Цели\n\n")
        f.write('<div id="active-container">\n\n')
        for entry in active_entries:
            f.write(entry + "\n\n")
        f.write('</div>\n\n')

        if archived_entries:
            f.write("---\n## 📚 Архив (Завършени)\n\n")
            f.write('<div id="archive-container" style="opacity: 0.7;">\n\n')
            for entry in archived_entries:
                f.write(entry + "\n\n")
            f.write('</div>\n\n')
        
        # JS за търсачката
        f.write("""
<script>
const searchInput = document.getElementById('roadmap-search');
const entries = document.querySelectorAll('.roadmap-entry');

searchInput.addEventListener('input', function() {
    const term = this.value.toLowerCase();
    entries.forEach(entry => {
        const text = entry.innerText.toLowerCase();
        entry.style.display = text.includes(term) ? 'block' : 'none';
    });
});

entries.forEach(entry => {
    const text = entry.innerText.toLowerCase();
    if (text.includes('python')) entry.style.borderLeft = '5px solid #3776ab';
    else if (text.includes('github') || text.includes('git')) entry.style.borderLeft = '5px solid #6e5494';
    else if (text.includes('3d')) entry.style.borderLeft = '5px solid #ff9900';
});
</script>
""")

if __name__ == "__main__":
    collect_roadmaps()