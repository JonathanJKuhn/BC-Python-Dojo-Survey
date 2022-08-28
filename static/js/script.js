var  otherCheck = document.getElementById("other");
var otherText = document.getElementById("other-text");

var reasonGroup = document.getElementsByName("reasonInput");

function validateOtherText() {
    if (otherCheck.checked) {
        otherText.disabled = false;
        otherText.required = true;
    }
    else {
        otherText.disabled = true;
        otherText.required = false;
    };
};

function toggleGroupRequired(group, bool) {
    group.forEach((x) => {
        x.required = bool;
    });
};

function validateReasonRequired () {
    var anyChecked = false;
    reasonGroup.forEach((reason) => {
        if (reason.checked) {
            anyChecked = true;
            toggleGroupRequired(reasonGroup, false);
        };       
    });

    if (!anyChecked) {
        toggleGroupRequired(reasonGroup, true);
    };
};

otherCheck.addEventListener('click', validateOtherText);

reasonGroup.forEach( x => {
    x.addEventListener('click', validateReasonRequired);
});