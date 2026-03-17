import os
import re
import random

def collect_flashcards():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    source_dir = base_dir if os.path.basename(base_dir) == 'docs' else os.path.join(base_dir, 'docs')
    output_dir = os.path.join(source_dir, 'review')

    vault = {'web': [], 'programming': [], 'networking': [], '3d-design': []}
    
    q_pattern = re.compile(r'<div class="question">(.*?)</div>', re.DOTALL)
    a_pattern = re.compile(r'<div class="answer">(.*?)</div>', re.DOTALL)
    d_pattern = re.compile(r'<div class="details">(.*?)</div>', re.DOTALL)

    for root, dirs, files in os.walk(source_dir):
        if 'review' in root: continue
        for file in files:
            if file.endswith('.md'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    raw_cards = content.split('<div class="flashcard">')
                    category = os.path.basename(root)
                    if category in vault:
                        for block in raw_cards[1:]:
                            q_match = q_pattern.search(block)
                            a_match = a_pattern.search(block)
                            d_match = d_pattern.search(block)
                            
                            if q_match and a_match:
                                question = q_match.group(1).strip()
                                answer = a_match.group(1).strip()
                                details = f'<div class="details">{d_match.group(1).strip()}</div>' if d_match else ""
                                
                                clean_card = f'<div class="flashcard"><div class="question">{question}</div><div class="answer">{answer}</div>{details}</div>'
                                vault[category].append(clean_card)

    if not os.path.exists(output_dir): os.makedirs(output_dir)

    for category, cards in vault.items():
        if not cards: continue
        random.shuffle(cards)
        output_file = os.path.join(output_dir, f'{category}.md')
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("---\nhide:\n  - navigation\n---\n\n# 🧠 Преговор: " + category.upper() + "\n\n")
            for card in cards:
                f.write(card + "\n\n")
            
    print("✅ Файловете са прегенерирани с поддръжка на детайли!")

if __name__ == "__main__":
    collect_flashcards()