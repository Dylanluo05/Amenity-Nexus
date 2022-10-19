var reminderButton1 = document.getElementById("reminder-button-1");
reminderButton1.addEventListener("click", reminderInputShow);

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

/*
var reminderForm = document.getElementById("reminder-form");
var myServiceReminds = document.getElementById("my-service-reminds");

if (localStorage.getItem("myServiceRemindsKey")) {
    for (var i = 0; i < JSON.parse(localStorage.getItem("myServiceRemindsKey")).length; i++) {
        var remindTitle = document.createElement("li");
        remindTitle.innerHTML = JSON.parse(localStorage.getItem("myServiceRemindsKey"))[i].title;
        remindTitle.setAttribute("class", "reminder-item-title");

        var remindDate = document.createElement("p");
        remindDate.innerHTML = JSON.parse(localStorage.getItem("myServiceRemindsKey"))[i].date;
        remindDate.setAttribute("class", "reminder-item-date");

        var remindTime = document.createElement("p");
        remindTime.innerHTML = JSON.parse(localStorage.getItem("myServiceRemindsKey"))[i].time;
        remindTime.setAttribute("class", "reminder-item-time");

        var remindCheck = document.createElement("p");
        remindCheck.innerHTML = "&#x2716;";
        remindCheck.setAttribute("class", "reminder-item-check");
        remindCheck.addEventListener("click", removeReminder);

        var remindContainer = document.createElement("div");
        remindContainer.setAttribute("class", "reminder-item-container");
        remindContainer.appendChild(remindTitle);
        remindContainer.appendChild(remindDate);
        remindContainer.appendChild(remindTime);
        remindContainer.appendChild(remindCheck);

        myServiceReminds.appendChild(remindContainer);
    }
}

function addReminder() {
    event.preventDefault();
    var reminderFormData = $("#reminder-form").serializeArray();
    reminderForm.reset();
    var reminderFormObject = {
        title: reminderFormData[0].value,
        date: reminderFormData[1].value,
        time: reminderFormData[2].value
    };

    var newRemindTitle = document.createElement("li");
    newRemindTitle.innerHTML = reminderFormObject.title;
    newRemindTitle.setAttribute("class", "reminder-item-title");

    var newRemindDate = document.createElement("p");
    newRemindDate.innerHTML = reminderFormObject.date;
    newRemindDate.setAttribute("class", "reminder-item-date")

    var newRemindTime = document.createElement("p");
    newRemindTime.innerHTML = reminderFormObject.time;
    newRemindTime.setAttribute("class", "reminder-item-time");

    var newRemindCheck = document.createElement("p");
    newRemindCheck.innerHTML = "&#x2716;";
    newRemindCheck.setAttribute("class", "reminder-item-check");
    newRemindCheck.addEventListener("click", removeReminder);

    var newRemindContainer = document.createElement("div");
    newRemindContainer.setAttribute("class", "reminder-item-container");
    newRemindContainer.appendChild(newRemindTitle);
    newRemindContainer.appendChild(newRemindDate);
    newRemindContainer.appendChild(newRemindTime);
    newRemindContainer.appendChild(newRemindCheck);

    myServiceReminds.appendChild(newRemindContainer);

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

function removeReminder() {
    var reminderIndex = $(this).parent().index();
    $(this).parent().remove();
    var serviceRemindsList3 = JSON.parse(localStorage.getItem("myServiceRemindsKey"));
    serviceRemindsList3.splice(reminderIndex, 1);
    localStorage.setItem("myServiceRemindsKey", JSON.stringify(serviceRemindsList3));
}
*/

var phonebookButton1 = document.getElementById("phonebook-button-1");
phonebookButton1.addEventListener("click", phonebookLobbyShow);

var phonebookLobbyContainer = document.getElementById("service-phonebook-lobby-container");
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

var phonebookLobbyContainerExit = document.getElementById("service-phonebook-lobby-container-exit");
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

$(".reveal-1").hide();
$(".button-1").on("click", addContact);

if (localStorage.servicePhonebookKey) {
    var addedDataArrayRetrieve2 = JSON.parse(localStorage.servicePhonebookKey);
    for (var i = 0; i < addedDataArrayRetrieve2.length; i++) {
        var indexRetrieve = addedDataArrayRetrieve2[i].index;
        $(".button-1").eq(indexRetrieve).hide();
        $(".reveal-1").eq(indexRetrieve).show();
    }
}

function addContact() {
    var index = $(this).parent().parent().index();
    var indexNew = index - 4;
    var title = $(this).parent().children(".title").html();
    var titleLength = title.length;
    var titleNew = title.slice(0, titleLength - 1);
    var phoneNumber = $(this).parent().children(".phone-number").html();
    $(this).hide();
    $(".reveal-1").eq(indexNew).show();
    if (localStorage.servicePhonebookKey) {
        var addedDataArrayRetrieve1 = JSON.parse(localStorage.servicePhonebookKey);
        var addedData2 = {
            index: indexNew,
            title: titleNew,
            phoneNumber: phoneNumber
        };
        addedDataArrayRetrieve1.push(addedData2);
        localStorage.servicePhonebookKey = JSON.stringify(addedDataArrayRetrieve1);
    } else {
        var addedData1 = {
            index: indexNew,
            title: titleNew,
            phoneNumber: phoneNumber
        };
        var addedDataArray = [addedData1];
        localStorage.servicePhonebookKey = JSON.stringify(addedDataArray);
    }
}

var slideNumber = 0;

if (localStorage.servicePhonebookKey) {
    var addedDataArrayRetrieve3 = JSON.parse(localStorage.servicePhonebookKey);
    /*var indexList = [];
    for (var a = 0; a < addedDataArrayRetrieve3.length; a++) {
        indexList.push(addedDataArrayRetrieve3[a].index);
    }
    var indexListSort = indexList.sort(function(a, b){return a - b});
    for (var w = 0; w < indexListSort.length; w++) {
        if (indexListSort[0] == addedDataArrayRetrieve3[w].index) {
            $("#service-phonebook-name").html(addedDataArrayRetrieve3[w].title);
            $("#service-phonebook-phone-number").html(addedDataArrayRetrieve3[w].phoneNumber);
        }
    }*/
    $("#service-phonebook-name").html(addedDataArrayRetrieve3[0].title);
    $("#service-phonebook-phone-number").html(addedDataArrayRetrieve3[0].phoneNumber);
}

var prevButton = document.getElementById("prev");
prevButton.addEventListener("click", previous);

var nextButton = document.getElementById("next");
nextButton.addEventListener("click", next);

function previous() {
    var addedDataArrayRetrieve4 = JSON.parse(localStorage.servicePhonebookKey);
    if (slideNumber > 0) {
        slideNumber -= 1;
    } else {
        slideNumber = addedDataArrayRetrieve4.length - 1;
    }
    /*var indexListSortItem1 = indexListSort[slideNumber];
    for (var y = 0; y < addedDataArrayRetrieve4.length; y++) {
        if (indexListSortItem1 == addedDataArrayRetrieve4[y].index) {
            $("#service-phonebook-name").html(addedDataArrayRetrieve4[y].title);
            $("#service-phonebook-phone-number").html(addedDataArrayRetrieve4[y].phoneNumber);
        }
    }*/
    $("#service-phonebook-name").html(addedDataArrayRetrieve4[slideNumber].title);
    $("#service-phonebook-phone-number").html(addedDataArrayRetrieve4[slideNumber].phoneNumber);

}

function next() {
    var addedDataArrayRetrieve5 = JSON.parse(localStorage.servicePhonebookKey);
    if (slideNumber < addedDataArrayRetrieve5.length - 1) {
        slideNumber += 1;
    } else {
        slideNumber = 0;
    }
    /*var indexListSortItem2 = indexListSort[slideNumber];
    for (var y = 0; y < addedDataArrayRetrieve5.length; y++) {
        if (indexListSortItem2 == addedDataArrayRetrieve5[y].index) {
            $("#service-phonebook-name").html(addedDataArrayRetrieve5[y].title);
            $("#service-phonebook-phone-number").html(addedDataArrayRetrieve5[y].phoneNumber);
        }
    }*/
    $("#service-phonebook-name").html(addedDataArrayRetrieve5[slideNumber].title);
    $("#service-phonebook-phone-number").html(addedDataArrayRetrieve5[slideNumber].phoneNumber);
}

var removeButton = document.getElementById("button-2");
removeButton.addEventListener("click", removeContact);

function removeContact() {
    var addedDataArrayRetrieveFinal = JSON.parse(localStorage.servicePhonebookKey)
    var slideNumberTemp = slideNumber
    if (slideNumber == addedDataArrayRetrieveFinal.length - 1) {
        slideNumber = 0;
    } else {
        slideNumber += 1;
    }
    /*var indexListSortItem3 = indexListSort[slideNumber];
    for (var b = 0; b < addedDataArrayRetrieveFinal.length; b++) {
        if (indexListSortItem3 == addedDataArrayRetrieveFinal[b].index) {
            $("#service-phonebook-name").html(addedDataArrayRetrieveFinal[b].title);
            $("#service-phonebook-phone-number").html(addedDataArrayRetrieveFinal[b].phoneNumber);
        }
    }*/
    $("#service-phonebook-name").html(addedDataArrayRetrieveFinal[slideNumber].title);
    $("#service-phonebook-phone-number").html(addedDataArrayRetrieveFinal[slideNumber].phoneNumber);
    /*indexListSort.splice(slideNumberTemp, 1);
    for (var i = 0; i < addedDataArrayRetrieveFinal.length; i++) {
       if (indexListSort[slideNumberTemp] == addedDataArrayRetrieveFinal[i].index) {
           addedDataArrayRetrieveFinal.splice(i, 1);
           localStorage.servicePhonebookKey = JSON.stringify(addedDataArrayRetrieveFinal);
       }
    }*/
    addedDataArrayRetrieveFinal.splice(slideNumberTemp, 1);
    localStorage.servicePhonebookKey = JSON.stringify(addedDataArrayRetrieveFinal);
}