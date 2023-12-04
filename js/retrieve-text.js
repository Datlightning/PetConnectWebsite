var all_data = {"some data":"more"};
var text = "123123";
export function makeAPICall() {
    // Replace 'YOUR_SCRIPT_URL' with the actual URL of your deployed Google Apps Script web app
    var url = 'https://script.google.com/macros/s/AKfycbxr7dgaK_ahsSlJNdrMe-APn5VJT4_4-s3574ubTfvgEdj86_UqeiaVdvuI1DDe1XwWcQ/exec?key=very-secret-api-key-that-nobody-knows&action=get_product_data';

    // Make an AJAX call to Google Script
    $.getJSON(url, function(result) {
        console.log(result)
        all_data = result
});

    // log the returned data
    // saveDataToFile(e)
}
