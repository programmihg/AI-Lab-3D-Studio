/**
 * AI Lab & 3D Studio - Финален Скрипт
 * Този код управлява брояча горе, флашкартите и Пътната карта.
 */

function initApp() {
    console.log("🚀 Скриптовете се зареждат...");

    // --- 1. СЪЗДАВАНЕ НА БРОЯЧА В ГОРНАТА ЛЕНТА ---
    const header = document.querySelector('.md-header__inner');
    if (header && !document.getElementById('study-controls')) {
        const controls = document.createElement('div');
        controls.id = 'study-controls';
        controls.innerHTML = `
            <div id="study-counter">
                <span style="color: #00ff88;">✓ <span id="val-success">0</span></span>
                <span style="color: #ff5555; margin-left:15px;">✗ <span id="val-fail">0</span></span>
            </div>
            <button id="reset-progress">НУЛИРАЙ</button>
        `;
        header.appendChild(controls);
    }

    let correctCount = 0;
    let wrongCount = 0;

    // --- 2. ДОБАВЯНЕ НА БУТОНИ ВЪВ ВСЯКА ФЛАШКАРТА ---
    document.querySelectorAll('.flashcard').forEach(card => {
        const answer = card.querySelector('.answer');
        if (answer && !card.querySelector('.card-controls')) {
            const btnWrap = document.createElement('div');
            btnWrap.className = 'card-controls';
            btnWrap.innerHTML = `
                <button class="btn-status btn-correct">Знам го</button>
                <button class="btn-status btn-wrong">Забравих</button>
                <button class="btn-status btn-details">Подробно</button>
            `;
            answer.appendChild(btnWrap);
        }
    });

    // --- 3. УНИВЕРСАЛЕН МЕНИДЖЪР НА КЛИКОВЕТЕ ---
    // Този блок слуша за кликове по цялата страница
    document.body.onclick = function(e) {
        const target = e.target;
        
        // Намираме дали сме кликнали вътре във флашкарта или roadmap запис
        const card = target.closest('.flashcard');
        const entry = target.closest('.roadmap-entry');

        // А) Обръщане на карта (ако кликнеш някъде по нея, но не на бутон)
        if (card && !target.classList.contains('btn-status')) {
            card.classList.toggle('flipped');
        }

        // Б) Бутони Знам / Забравих
        if (target.classList.contains('btn-correct') && card) {
            e.stopPropagation();
            if (!card.classList.contains('correct')) {
                if (card.classList.contains('wrong')) {
                    wrongCount--; 
                    card.classList.remove('wrong');
                }
                card.classList.add('correct');
                correctCount++;
                updateDisplay();
            }
        }

        if (target.classList.contains('btn-wrong') && card) {
            e.stopPropagation();
            if (!card.classList.contains('wrong')) {
                if (card.classList.contains('correct')) {
                    correctCount--; 
                    card.classList.remove('correct');
                }
                card.classList.add('wrong');
                wrongCount++;
                updateDisplay();
            }
        }

        // В) Бутон ПОДРОБНО (За всички страници!)
        if (target.classList.contains('btn-details') || target.classList.contains('roadmap-details-btn')) {
            e.stopPropagation();
            // Търсим детайлите първо вътре в елемента, после като следващ елемент
            const details = (card || entry) ? (card || entry).querySelector('.details') : target.nextElementSibling;
            
            if (details) {
                details.classList.toggle('show');
                target.textContent = details.classList.contains('show') ? 'Скрий детайли' : 'Подробно';
            }
        }

        // Г) Ресет
        if (target.id === 'reset-progress') location.reload();
    };

    function updateDisplay() {
        document.getElementById('val-success').innerText = correctCount;
        document.getElementById('val-fail').innerText = wrongCount;
    }
}

// Изпълни скрипта при зареждане на страницата
document.addEventListener("DOMContentLoaded", initApp);

// Специално за MkDocs Material (Navigation Tabs поддръжка)
if (typeof app !== "undefined" && app.document$) {
    app.document$.subscribe(function() {
        initApp();
    });
}