#1: Интерактивна система за обучение (MkDocs + Flashcards)
Раздел за документация на самия инструмент, който създадохме.

Примерни флашкарти за този раздел:

HTML
<div class="flashcard">
    <div class="question">Каква е ролята на скрипта <code>collect_cards.py</code>?</div>
    <div class="answer">Автоматизация на преговора.</div>
    <div class="details">
        Скриптът обхожда всички папки в <code>docs/</code>, намира блоковете с клас <code>flashcard</code>, разбърква ги и генерира нови <code>.md</code> файлове в папка <code>review/</code> за всяка категория.
    </div>
</div>

<div class="flashcard">
    <div class="question">Как се дефинира структурата на една флашкарта в Markdown файла?</div>
    <div class="answer">Чрез три основни <code>div</code> елемента.</div>
    <div class="details">
        Използва се контейнер с клас <code>flashcard</code>, вътре в който има:<br>
        1. <code>div class="question"</code> (Въпрос)<br>
        2. <code>div class="answer"</code> (Кратък отговор)<br>
        3. <code>div class="details"</code> (Подробно обяснение - опционално)
    </div>
</div>