function openNav() {
    const navbar = document.getElementById("SideNav");

    if (navbar.style.width === "0%") {
        navbar.style.width = "100%";
    } else {
        navbar.style.width = "0%";
    }
}
  
function closeNav() {
    document.getElementById("SideNav").style.width = "0";
}

function openmodal() {
    document.getElementById("myModal").style.display= "block"
    var amount = document.getElementById("amountField").value;
    var address = document.getElementById("walletField").value;

    var amountLabel = document.getElementById("amountLabel");
    var addressLabel = document.getElementById("walletLabel");

    amountLabel.innerText = amount;
    addressLabel.innerText = address;
}

function closemodal() {
    document.getElementById("myModal").style.display = "none";
}

function copyToClipboard() {
    var textToCopy = document.getElementById("addr").innerText;

    var tempTextArea = document.createElement("textarea");
    tempTextArea.value = textToCopy;
    tempTextArea.style.position = "fixed";  // To ensure the textarea is not visible
    document.body.appendChild(tempTextArea);

    tempTextArea.select();
    tempTextArea.setSelectionRange(0, 99999); // For mobile devices

    try {
        var successful = document.execCommand("copy");
        var message = successful ? "Address copied to clipboard!" : "Unable to copy text.";
        alert(message);
    } catch (error) {
        console.error("Unable to copy text. Error: ", error);
    }

    document.body.removeChild(tempTextArea);
}
  				
function proceed_withdrawal(){
    document.getElementById("Withdraw_proceeded").style.display = "block";
}		


