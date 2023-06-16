// Start by getting making a youtube link to bytestring converter

const submitBttn = document.getElementById("submitBttn");
const textForm = document.getElementById("linkData");
submitBttn.addEventListener('click', songSearch);
function songSearch(event) {
    let link = textForm.value;
    // console.log(link);
    fetch(`/getMP3?link=${link}`)
        .then(function (response) {
            return response.text();
        }).then(function (text) {
            console.log('GET response text:');
            console.log(text); // Print the greeting as text
        });
    event.preventDefault();
}