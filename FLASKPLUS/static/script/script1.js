function previewImage() {
    var input = document.getElementById('inputImage');
    var preview = document.getElementById('preview');
    var file = input.files[0];

    var reader = new FileReader();

    reader.onloadend = function () {
        preview.src = reader.result;
    };

    if (file) {
        reader.readAsDataURL(file);
    } else {
        preview.src = "";
    }
}

function predict() {
    var input = document.getElementById('inputImage');
    var resultText = document.getElementById('result');

    if (!input.files || input.files.length === 0) {
        resultText.innerText = "Please select an image.";
        return;
    }

    var file = input.files[0];
    var formData = new FormData();
    formData.append('file', file);

    $.ajax({
        url: 'predict',  // Replace with the correct endpoint where you deploy the prediction server
        type: 'POST',
        data: formData,
        contentType: false,
        processData: false,
        success: function (data) {
            resultText.innerText = "Probability of being COVID-19: " + data.probability.toFixed(4) +
                                   "\nPredicted class: " + data.class;
        },
        error: function () {
            resultText.innerText = "Error predicting the image.";
        }
    });
}
