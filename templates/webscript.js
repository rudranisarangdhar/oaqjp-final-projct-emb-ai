function RunSentimentAnalysis() {
    let text = document.getElementById("textToAnalyze").value;

    if (text === "") {
        document.getElementById("system_response").innerHTML = "Invalid text! Please try again.";
        return;
    }

    fetch(`/emotionDetector?textToAnalyze=${text}`)
        .then(response => response.text())
        .then(data => {
            document.getElementById("system_response").innerHTML = data;
        })
        .catch(error => {
            document.getElementById("system_response").innerHTML = "Error occurred!";
        });
}
