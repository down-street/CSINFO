function toggleDetails(element) {
    const players = element.querySelector('.players');
    if (players.style.display === 'flex') {
        players.style.display = 'none';
    } else {
        players.style.display = 'flex';
    }
}