function getMessage() {
    var senderInformation = {
        "navn": document.getElementById('senderNavn').value,
        "email": document.getElementById('senderEmail').value,
        "besked": document.getElementById('senderBesked').value,
    }
    var json = JSON.stringify(senderInformation);
    fs.writeFile('beskeder.json', json, (err) => {
        if (err) {
            throw err;
        }
        Console.log("Besked sendt")
    });
}