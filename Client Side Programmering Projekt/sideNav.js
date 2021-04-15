
function openNav() {
    document.getElementById("mySidenav").style.width = "13pc";
}

function closeNav() {
    document.getElementById("mySidenav").style.width = "0";
}

// Loader menu fra html fil og insætter den når siden loades
function mkNav() {
    var xhr = new XMLHttpRequest();
    xhr.open('GET', 'sideNav.html', true);
    xhr.onreadystatechange = function () {
        if (this.readyState !== 4) return;
        if (this.status !== 200) return; 
        document.getElementById('sideNav').innerHTML = this.responseText;
    };
    xhr.send();
}
window.onload(mkNav());