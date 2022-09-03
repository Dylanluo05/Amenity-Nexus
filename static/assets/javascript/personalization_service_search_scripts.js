var reminderButton = document.getElementById("reminder-button");
reminderButton.addEventListener("click", reminderInputShow);

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

var phonebookButton = document.getElementById("phonebook-button");
phonebookButton.addEventListener("click", phonebookLobbyShow);

var phonebookLobbyContainer = document.getElementById("phonebook-lobby-container");
phonebookLobbyContainer.style.display = "none";
phonebookLobbyContainer.style.opacity = 0;
var OPACITY3 = 0;

function phonebookLobbyShow() {
    if (phonebookLobbyContainer.style.display == "none") {
        phonebookLobbyContainer.style.display = "block";
        var Timer3 = setInterval(phonebookPopupShowAnimation, 40);
        function phonebookPopupShowAnimation() {
            phonebookLobbyContainer.style.opacity = OPACITY3;
            OPACITY3 += 0.05;
            if (OPACITY3 > 1.05) {
                clearInterval(Timer3);
                OPACITY3 = 0;
            }
        }
    }
}

var phonebookLobbyContainerExit = document.getElementById("phonebook-lobby-container-exit");
phonebookLobbyContainerExit.addEventListener("click", phonebookLobbyHide);

var OPACITY4 = 1;

function phonebookLobbyHide() {
    if (phonebookLobbyContainer.style.display == "block") {
        var Timer4 = setInterval(phonebookPopupHideAnimation, 40);
        function phonebookPopupHideAnimation() {
            phonebookLobbyContainer.style.opacity = OPACITY4;
            OPACITY4 -= 0.05;
            if (OPACITY4 < -0.05) {
                clearInterval(Timer4);
                phonebookLobbyContainer.style.display = "none";
                OPACITY4 = 1;
            }
        }
    }
}

var reminderForm = document.getElementById("reminder-form");

function addReminderExternal() {
    event.preventDefault();
    var reminderFormData = $("#reminder-form").serializeArray();
    reminderForm.reset();
    var reminderFormObject = {
        title: reminderFormData[0].value,
        date: reminderFormData[1].value,
        time: reminderFormData[2].value
    };

    if (localStorage.getItem("myServiceRemindsKey")) {
        var serviceRemindsList2 = JSON.parse(localStorage.getItem("myServiceRemindsKey"));
        var serviceRemindObject2 = {
            title: reminderFormData[0].value,
            date: reminderFormData[1].value,
            time: reminderFormData[2].value
        };
        serviceRemindsList2.push(serviceRemindObject2);
        localStorage.setItem("myServiceRemindsKey", JSON.stringify(serviceRemindsList2));
    }
    else {
        var serviceRemindObject1 = {
            title: reminderFormData[0].value,
            date: reminderFormData[1].value,
            time: reminderFormData[2].value
        };
        var serviceRemindsList1 = [serviceRemindObject1];
        localStorage.setItem("myServiceRemindsKey", JSON.stringify(serviceRemindsList1));
    }
}