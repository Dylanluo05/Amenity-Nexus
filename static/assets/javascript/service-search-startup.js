if (localStorage.getItem("maintenanceAutomaticScroll")) {
    if (localStorage.getItem("maintenanceAutomaticScroll") == "On") {
        document.getElementById('category-dropdown-container-1').scrollIntoView({behavior: "smooth", block: "start"});
        localStorage.setItem("maintenanceAutomaticScroll", "Off");
    }
}
if (localStorage.getItem("amenityAutomaticScroll")) {
    if (localStorage.getItem("amenityAutomaticScroll") == "On") {
        document.getElementById('category-dropdown-container-2').scrollIntoView({behavior: "smooth", block: "start"});
        localStorage.setItem("amenityAutomaticScroll", "Off");
    }
}
if (localStorage.getItem("medicalAutomaticScroll")) {
    if (localStorage.getItem("medicalAutomaticScroll") == "On") {
        document.getElementById('category-dropdown-container-3').scrollIntoView({behavior: "smooth", block: "start"});
        localStorage.setItem("medicalAutomaticScroll", "Off");
    }
}
if (localStorage.getItem("educationAutomaticScroll")) {
    if (localStorage.getItem("educationAutomaticScroll") == "On") {
        document.getElementById('category-dropdown-container-4').scrollIntoView({behavior: "smooth", block: "start"});
        localStorage.setItem("educationAutomaticScroll", "Off");
    }
}

if (localStorage.getItem("maintenanceDropdownStatus")) {
    if (localStorage.getItem("maintenanceDropdownStatus") == "Hidden") {
        $(".category-dropdown-content").eq(0).css("display", "none");
    } else if (localStorage.getItem("maintenanceDropdownStatus") == "Shown") {
        $(".category-dropdown-content").eq(0).css("display", "block");
        $(".category-dropdown-content").eq(0).animate({height: "250px"}, 1000);
    }
}

if (localStorage.getItem("amenityDropdownStatus")) {
    if (localStorage.getItem("amenityDropdownStatus") == "Hidden") {
        $(".category-dropdown-content").eq(1).css("display", "none");
    } else if (localStorage.getItem("amenityDropdownStatus") == "Shown") {
        $(".category-dropdown-content").eq(1).css("display", "block");
        $(".category-dropdown-content").eq(1).animate({height: "250px"}, 1000);
    }
}

if (localStorage.getItem("medicalDropdownStatus")) {
   if (localStorage.getItem("medicalDropdownStatus") == "Hidden") {
        $(".category-dropdown-content").eq(2).css("display", "none");
   } else if (localStorage.getItem("medicalDropdownStatus") == "Shown") {
       $(".category-dropdown-content").eq(2).css("display", "block");
       $(".category-dropdown-content").eq(2).animate({height: "250px"}, 1000);
   }
}

if (localStorage.getItem("educationDropdownStatus")) {
    if (localStorage.getItem("educationDropdownStatus") == "Hidden") {
        $(".category-dropdown-content").eq(3).css("display", "none");
    }
    else if (localStorage.getItem("educationDropdownStatus") == "Shown") {
        $(".category-dropdown-content").eq(3).css("display", "block");
        $(".category-dropdown-content").eq(3).animate({height: "250px"}, 1000);
    }
}
