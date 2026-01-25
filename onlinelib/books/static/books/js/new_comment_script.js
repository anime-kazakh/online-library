document.getElementById('comment-form').addEventListener('submit', function(e) {
    e.preventDefault()
    const config = document.getElementById('app-config');
    if (!config) { alert('Config error!') }
    const formData = {
        book: config.dataset.book,
        comment:document.getElementById('id_comment').value,
        csrfmiddlewaretoken: document.querySelector('[name=csrfmiddlewaretoken]').value
    };
    fetch(config.dataset.addCommentUrl, {
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
                    <span class="comment-info__username">
                        ${data.BookComment.user}
                    </span>
                    <span class="comment-info__post-time">
                        ${data.BookComment.post_time}
                    </span>
                    <span class="comment-info__delete-comment">
                        <form id="delete-comment-form">
                            <input type="hidden" name="csrfmiddlewaretoken" value="${config.dataset.csrfToken}">
                            <input type="hidden" name="comment-id" value="${data.BookComment.comment_id}">
                            <button type="submit">
                                <svg><use href="#delete-2"></use></svg>
                            </button>
                        </form>
                    </span>
                </div>
                <div class="comment-text">
                    ${data.BookComment.comment}
                </div>
            `;
            commentsList.prepend(newComment);
            document.getElementById('id_comment').value = '';
            // location.reload()
        } else {
            alert('Ошибка' + data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});