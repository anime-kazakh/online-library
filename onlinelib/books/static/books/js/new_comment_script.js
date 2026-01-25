document.getElementById('comment-form').addEventListener('submit', function(e) {
    e.preventDefault()
    const config = document.getElementById('app-config');
    if (!config) { alert('Config error!') }
    const formData = {
        book: config.dataset.book,
        comment:document.getElementById('id_comment').value,
        csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value
    };
    fetch(config.dataset.postUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': formData.csrfmiddlewaretoken
        },
        body: JSON.stringify({
            book: formData.book,
            comment: formData.comment
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            const commentsList = document.getElementById('comments-list');
            const newComment = document.createElement('div');
            newComment.className = 'comment'
            newComment.innerHTML = `
                <div class="comment-info">
                    <span>
                        ${data.BookComment.user}
                    </span>
                    <span>
                        ${data.BookComment.post_time}
                    </span>
                </div>
                <div class="comment-text">
                    ${data.BookComment.comment}
                </div>
            `;
            commentsList.prepend(newComment);
            document.getElementById('id_comment').value = '';
            location.reload()
        } else {
            alert('Ошибка' + data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});