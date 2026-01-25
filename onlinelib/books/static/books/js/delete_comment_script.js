document.getElementById('delete-comment-form').addEventListener('submit', function (e) {
    e.preventDefault()
    const config = document.getElementById('app-config');
    if (!config) { alert('Config error!') }
    const formData = {
        comment_id: document.querySelector('[name=comment-id]').value,
        csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value
    };
    fetch(config.dataset.deleteCommentUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': formData.csrfmiddlewaretoken
        },
        body: JSON.stringify({
            comment_id: formData.comment_id
        })
    })
    .then(response => response.json())
    .then(data => {
        if(data.success) {
            location.reload();
        } else {
            alert('Ошибка' + data.error);
        }
    })
    .catch(error => console.error('Error', error))
});