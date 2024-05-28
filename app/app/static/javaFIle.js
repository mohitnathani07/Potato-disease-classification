// Get the image input and action button elements
const imageInput = document.getElementById('imageInput');
const actionButton = document.getElementById('actionButton');
const selectedImage = document.getElementById('selectedImage');

// Event listener for the image input
imageInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (file) {
        const reader = new FileReader();
        reader.onload = function(e) {
            selectedImage.src = e.target.result;
            selectedImage.style.display = 'block';
        }
        reader.readAsDataURL(file);
    }
});

// Event listener for the action button
actionButton.addEventListener('click', function() {
    if (selectedImage.src) {
        alert('Action performed on the selected image!');
    } else {
        alert('Please select an image first.');
    }
});