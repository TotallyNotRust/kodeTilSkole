

function getMessage() {
    alert("Under opsætning.");
}

function mkNav() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'Skriv til mig.html', true);
    xhr.onreadystatechange = function () {
        if (this.readyState !== 4) return;
        if (this.status !== 200) return;
        document.getElementById('skrivTilMig').innerHTML = this.responseText;
    };
    xhr.send();
}
window.onload(mkNav());