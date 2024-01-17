function validateForm() {
  // Get form inputs
  var age = document.getElementById('age').value;
  var sex = document.getElementById('sex').value;
  var chestPain = document.getElementById('chestPain').value;
  var restingBPS = document.getElementById('restingBPS').value;
  var cholesterol = document.getElementById('cholesterol').value;
  var fastingBloodSugar = document.getElementById('fastingBloodSugar').value;
  var restingECG = document.getElementById('restingECG').value;
  var maxHeartRate = document.getElementById('maxHeartRate').value;
  var exerciseAngina = document.getElementById('exerciseAngina').value;
  var oldPeak = document.getElementById('oldPeak').value;
  var STSlope = document.getElementById('STSlope').value;

  // Simple validation example (you can customize this based on your requirements)
  if (!isNumeric(age) || age <= 0) {
      alert('Please enter a valid age.');
      return false;
  }

  if (!isNumeric(sex) || (sex !== '1.0' && sex !== '0.0')) {
      alert('Please enter a valid value for sex (1.0 for Male, 0.0 for Female).');
      return false;
  }

  if (!isNumeric(chestPain) || chestPain < 0) {
      alert('Please enter a valid chest pain type.');
      return false;
  }

  if (!isNumeric(restingBPS) || restingBPS <= 0) {
      alert('Please enter a valid resting blood pressure.');
      return false;
  }

  if (!isNumeric(cholesterol) || cholesterol <= 0) {
      alert('Please enter a valid cholesterol level.');
      return false;
  }

  if (!isNumeric(fastingBloodSugar) || (fastingBloodSugar !== '0.0' && fastingBloodSugar !== '1.0')) {
      alert('Please enter a valid value for fasting blood sugar (0.0 for No, 1.0 for Yes).');
      return false;
  }

  if (!isNumeric(restingECG) || restingECG < 0) {
      alert('Please enter a valid resting ECG.');
      return false;
  }

  if (!isNumeric(maxHeartRate) || maxHeartRate <= 0) {
      alert('Please enter a valid max heart rate.');
      return false;
  }

  if (!isNumeric(exerciseAngina) || (exerciseAngina !== '0' && exerciseAngina !== '1')) {
      alert('Please enter a valid value for exercise angina (0 for No, 1 for Yes).');
      return false;
  }

  if (!isNumeric(oldPeak) || oldPeak < 0) {
      alert('Please enter a valid old peak.');
      return false;
  }

  if (!isNumeric(STSlope) || STSlope < 0) {
      alert('Please enter a valid ST slope.');
      return false;
  }

  // If all validations pass, the form will be submitted
  return true;
}

function isNumeric(value) {
  return !isNaN(parseFloat(value)) && isFinite(value);
}

  