document.getElementById('score-container__rate-button').addEventListener('click', function (e) {
    e.preventDefault();
    const score_form = document.getElementById('score-form');
    if (score_form.style['display'] !== '') {

        score_form.style = ''
    } else {
        score_form.style = 'display: none;'
    }
});
document.getElementById('score-form').addEventListener('submit', function (e) {
    e.preventDefault();
    const config = document.getElementById('app-config');
    if (!config) { alert('Config error!') }
    const formData = {
        book: config.dataset.book,
        score: document.getElementById('score').value,
        csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value
    };
    fetch(config.dataset.bookRateUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': formData.csrfmiddlewaretoken
        },
        body: JSON.stringify({
            book: formData.book,
            score: formData.score
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const avgScoreContainer = document.getElementById('score_avg');
            avgScoreContainer.textContent = `${data.avg_score} / 10`;
            const scoreFormButton = document.getElementById('score-form__button');
            scoreFormButton.textContent = 'Изменить оценку'
        } else {
            alert('Ошибка' + data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});