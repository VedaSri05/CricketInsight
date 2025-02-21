function predictRuns() {
    let data = {
        total_matches: parseInt(document.getElementById('matches').value),
        innings: parseInt(document.getElementById('innings').value),
        average_score: parseFloat(document.getElementById('average').value),
        strike_rate: parseFloat(document.getElementById('strike').value),
        highest_score: parseInt(document.getElementById('highest').value),
        fours: parseInt(document.getElementById('fours').value),
        sixes: parseInt(document.getElementById('sixes').value),
        fifties: parseInt(document.getElementById('fifties').value),
        hundreds: parseInt(document.getElementById('hundreds').value)
    };

    fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        document.getElementById('result').innerText = "Predicted Runs: " + result.predicted_total_runs;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('result').innerText = "Error predicting runs.";
    });
}
