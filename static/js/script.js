// Timer showing the allert messages
setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 5000);

// Apply datepicker styling for test drive booking form
$('#datepicker').datepicker({
    format: 'dd/mm/yyyy'
});
$('#datepicker').datepicker("setDate", new Date());

// Highlight current day of the week
$(document).ready(function () {
    $('.opening-hours li').eq(new Date().getDay()).addClass('today');
});

// Display current year in the footer
document.querySelector('#current-year').innerText = new Date().getFullYear();