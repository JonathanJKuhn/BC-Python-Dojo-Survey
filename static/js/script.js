var  otherCheck = document.getElementById("other");

function toggleOtherText() {
    if (otherCheck.checked) {
        document.getElementById("other-text").disabled = false;
    }
    else {
        document.getElementById("other-text").disabled = true;
    }
};

otherCheck.addEventListener('click', toggleOtherText);