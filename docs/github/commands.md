<div class="flashcard">
    <div class="question">Как да клонирам хранилище от GitHub на локалния си компютър?</div>
    <div class="answer"><code>git clone [URL]</code></div>
    <div class="details">
        Използва се за създаване на копие на проект. URL адресът може да бъде HTTPS или SSH.
    </div>
</div>

<div class="flashcard">
    <div class="question">Коя е стандартната последователност за качване на промени?</div>
    <div class="answer">Add -> Commit -> Push</div>
    <div class="details">
        1. <code>git add .</code> (подготвя файловете)<br>
        2. <code>git commit -m "описание"</code> (запазва промените локално)<br>
        3. <code>git push origin main</code> (изпраща ги към GitHub)
    </div>
</div>

<div class="flashcard">
    <div class="question">Как да реша Merge Conflict стъпка по стъпка?</div>
    <div class="answer">Identify -> Fix -> Add -> Commit</div>
    <div class="details">
        1. <b>Identify:</b> Git маркира конфликтите във файла с <code><<<<<<<</code> и <code>>>>>>>></code>.<br>
        2. <b>Fix:</b> Изтрий маркерите и остави кода, който искаш.<br>
        3. <b>Add:</b> Маркирай файла като готов с <code>git add [име-на-файл]</code>.<br>
        4. <b>Commit:</b> Завърши процеса с <code>git commit -m "Resolved conflict"</code>.
    </div>
</div>

<div class="flashcard">
    <div class="question">Кои са трите маркера при Merge Conflict?</div>
    <div class="answer"><<<<<<<, =======, >>>>>>></div>
    <div class="details">
        - <code><<<<<<< HEAD</code>: Твоите локални промени.<br>
        - <code>=======</code>: Разделителната линия.<br>
        - <code>>>>>>>> branch_name</code>: Промените, които идват отвън и се опитваш да влееш.
    </div>
</div>

<div class="flashcard">
    <div class="question">За какво служи <code>git status</code>?</div>
    <div class="answer">Показва състоянието на работната директория.</div>
    <div class="details">
        Позволява ти да видиш кои файлове са променени, кои са подготвени за commit (staged) и кои не се проследят от Git.
    </div>
</div>

<div class="flashcard">
    <div class="question">Какво означават символите при конфликт (<<<<<<< HEAD)?</div>
    <div class="answer"> HEAD е твоята текуща версия.</div>
    <div class="details">
        - <code><<<<<<< HEAD</code>: Твоите промени.<br>
        - <code>=======</code>: Границата.<br>
        - <code>>>>>>>> [branch]</code>: Промените, които идват от другото място.
    </div>
</div>

<div class="flashcard">
    <div class="question">Как да добавя отдалечено (remote) хранилище?</div>
    <div class="answer">git remote add origin [URL]</div>
    <div class="details">
        Тази команда казва на Git: "Искам да изпращам кода си на този адрес в GitHub и да го наричам 'origin'".
    </div>
</div>

<div class="flashcard">
    <div class="question">Каква е разликата между git commit и git push?</div>
    <div class="answer">Локално vs Отдалечено запазване</div>
    <div class="details">
        - <b>Commit:</b> Прави "снимка" на промените на твоя компютър.<br>
        - <b>Push:</b> Изпраща тези снимки в сървъра на GitHub.
    </div>
</div>