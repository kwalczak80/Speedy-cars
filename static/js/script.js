/*jshint esversion: 6 */

// Timer showing the alert messages
setTimeout(function () {
    $("#msg").alert('close');
}, 5000);

// Apply datepicker styling for test drive booking form
$('#datepicker').datepicker({
    format: 'dd/mm/yyyy'
});
$('#datepicker').datepicker("setDate", new Date());

// Highlight the current day of the week
$(document).ready(function () {
    $('.opening-hours li').eq(new Date().getDay()).addClass('today');
});

// Get current year
$('#current-year').html(new Date().getFullYear());