# 🏠 AI Lab & 3D Studio Dashboard

<input type="text" id="roadmap-search" placeholder="🔍 Търси в историята (напр. python, 3d, git)..." style="width:100%; padding:12px; border-radius:10px; border:1px solid #444; background:#252538; color:white; margin-bottom:20px;">

## 🗺️ Пътна Карта

<div id="roadmap-container">

<div class="roadmap-entry">
    <span class="date">2026-03-17</span>
    <span class="milestone">🤖 Покорен връх: Поддръжка на детайлни отговори</span>
    <button class="roadmap-details-btn">Подробно</button>
    <div class="details">
        Внедрена е функционалност за "Подробно" разгъване на информацията при флашкартите. Първото приложение е за командата <code>netstat -tlnp</code> с детайлно описание на флаговете.
    </div>
</div>

<div class="roadmap-entry">
    <span class="date">2026-03-17</span>
    <span class="milestone">🤖 Покорен връх: Интерактивна документация за флашкарти</span>
    <button class="roadmap-details-btn">Подробно</button>
    <div class="details">
        Създаден е наръчник за работа със системата (Flashcards Guide), включващ HTML структурата и ролята на автоматизиращите скриптове.
    </div>
</div>

<div class="roadmap-entry">
    <span class="date">2026-03-17</span>
    <span class="milestone">🤖 Покорен връх: Интеграция на тежки LLM модели</span>
    <button class="roadmap-details-btn">Подробно</button>
    <div class="details">
        Успешно конфигуриране на <b>Llama-3.3-70b-instruct</b> и <b>Command-R 32B</b> в LM Studio. Моделите са тествани за работа в локална среда с оптимизирана квантизация.
    </div>
</div>

<div class="roadmap-entry">
    <span class="date">2026-03-17</span>
    <span class="milestone">🤖 Заглавие на задачата</span>
    <button class="roadmap-details-btn">Подробно</button>
    <div class="details">
        Тук са скритите детайли, които ще се появят при клик.
    </div>
</div>

<div class="roadmap-entry">
    <span class="date">2026-03-17</span>
    <span class="milestone">🗂️ Покорен връх: Решаване на Merge Conflicts</span>
    <button class="roadmap-details-btn">Подробно</button>
    <div class="details" style="display: none;">
        Конфликтите възникват, когато двама души променят един и същ ред. 
        Оправят се чрез: <br>
        1. Избор на версия (Accept Incoming/Current) <br>
        2. <code>git add .</code> <br>
        3. <code>git commit</code>
    </div>
</div>

<div class="roadmap-entry">
    <span class="date">2026-03-17</span>
    <span class="milestone">🗂️ Покорен връх: Организация на Git хранилище</span>
    <button class="roadmap-details-btn">Подробно</button>
    <div class="details" style="display: none;">
        Успешно структуриране на локалните файлове и подготовка за първи Push към отдалечен сървър.
    </div>
</div>

<div class="roadmap-entry">
    <span class="date">2026-03-17</span>
    <span class="milestone">🐙 Покорен връх: Начало на GitHub секцията</span>
    <button class="roadmap-details-btn">Подробно</button>
    <div class="details">
        Създаден нов раздел за проследяване на Git команди и управление на версиите.
    </div>
</div>

<div class="roadmap-entry">
    <span class="date">2026-03-17</span>
    <span class="milestone">🐍 Покорен връх: AI-Assisted Coding с Cursor</span>
    <button class="roadmap-details-btn">Подробно</button>
    <div class="details">
        Настроена е среда за разработка Cursor с активиран модел <b>Llama-3.3-70b</b> за подпомагане на писането на Python скриптове.
    </div>
</div>

<div class="roadmap-entry">
    <span class="date">2026-03-16</span>
    <span class="milestone">🤖 Покорен връх: Автоматизирано подреждане на карти</span>
    <button class="roadmap-details-btn">Подробно</button>
    <div class="details">
        Отстранен е проблемът с вгнездяването ("матрьошките") на таговете. Картите вече се генерират чисто и се подреждат правилно една под друга в секцията за преговор.
    </div>
</div>

</div>


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

// Динамично оцветяване
entries.forEach(entry => {
    const text = entry.innerText.toLowerCase();
    if (text.includes('python')) entry.style.borderLeft = '5px solid #3776ab';
    else if (text.includes('github') || text.includes('git')) entry.style.borderLeft = '5px solid #6e5494';
    else if (text.includes('3d')) entry.style.borderLeft = '5px solid #ff9900';
});
</script>
