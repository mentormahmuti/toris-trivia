document.addEventListener("DOMContentLoaded", function() {
    const quizForm = document.querySelector("form");
    const questionContainer = document.querySelector("body");

    quizForm.addEventListener("submit", function(event) {
        event.preventDefault();
        const formData = new FormData(quizForm);
        fetch(quizForm.action, {
            method: "POST",
            body: formData
        })
        .then(response => response.text())
        .then(html => {
            questionContainer.classList.add("fade-out");
            setTimeout(() => {
                questionContainer.innerHTML = html;
                questionContainer.classList.remove("fade-out");
                questionContainer.classList.add("fade-in");
            }, 500);
        })
        .catch(error => console.error('Error:', error));
    });
});