var reminderButton = document.getElementById("reminder-button");
reminderButton.addEventListener("click", reminderInputShow);

reminderButton.innerHTML = "Test";

var reminderInputContainer = document.getElementById("reminder-input-container");
reminderInputContainer.style.display = "none";
reminderInputContainer.style.opacity = 0;
var OPACITY1 = 0;

function reminderInputShow() {
    if (reminderInputContainer.style.display == "none") {
        reminderInputContainer.style.display = "block";
        var Timer1 = setInterval(reminderPopupShowAnimation, 40);
        function reminderPopupShowAnimation() {
            reminderInputContainer.style.opacity = OPACITY1;
            OPACITY1 += 0.05;
            if (OPACITY1 > 1.05) {
                clearInterval(Timer1);
                OPACITY1 = 0;
            }
        }
    }
}

var reminderInputContainerExit = document.getElementById("reminder-input-container-exit");
reminderInputContainerExit.addEventListener("click", reminderInputHide);
var OPACITY2 = 1;

function reminderInputHide() {
    if (reminderInputContainer.style.display == "block") {
        var Timer2 = setInterval(reminderPopupHideAnimation, 40);
        function reminderPopupHideAnimation() {
            reminderInputContainer.style.opacity = OPACITY2;
            OPACITY2 -= 0.05;
            if (OPACITY2 < -0.05) {
                clearInterval(Timer2);
                OPACITY2 = 1;
                reminderInputContainer.style.display = "none";
            }
        }
    }
}