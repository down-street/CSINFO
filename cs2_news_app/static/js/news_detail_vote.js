document.addEventListener("DOMContentLoaded", function() {
    const upvoteButtons = document.querySelectorAll('.upvote-button');
    const downvoteButtons = document.querySelectorAll('.downvote-button');

    upvoteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const newsId = this.getAttribute('data-id');
            fetch(`/news/${newsId}/upvote/`, { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    if(data.success) {
                        this.nextElementSibling.innerText = parseInt(this.nextElementSibling.innerText) + 1;
                        this.classList.add('bounce');
                        setTimeout(() => this.classList.remove('bounce'), 300);
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });

    downvoteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const newsId = this.getAttribute('data-id');
            fetch(`/news/${newsId}/downvote/`, { method: 'POST' })
                .then(response => response.json())
                .then(data => {
                    if(data.success) {
                        this.nextElementSibling.innerText = parseInt(this.nextElementSibling.innerText) + 1;
                        this.classList.add('bounce');
                        setTimeout(() => this.classList.remove('bounce'), 300);
                    }
                })
                .catch(error => console.error('Error:', error));
        });
    });
});
