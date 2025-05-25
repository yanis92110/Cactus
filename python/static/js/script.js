document.addEventListener('DOMContentLoaded', function () {
    const fetchDataButton = document.getElementById('fetchDataButton');
    const dataOutput = document.getElementById('dataOutput');

    fetchDataButton.addEventListener('click', function () {
        // Faire une requête GET à l'API Flask
        fetch('/api/data')
            .then(response => response.json())
            .then(data => {
                dataOutput.textContent = data.message;
            })
            .catch(error => console.error('Erreur:', error));
    });
});
