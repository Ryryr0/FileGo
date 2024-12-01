const fileDropZone = document.getElementById('fileDropZone');
const fileInput = document.getElementById('fileInput');
const addFileBtn = document.getElementById('addFileBtn');
const fileNameDisplay = document.getElementById('fileName');

document.addEventListener('DOMContentLoaded', () => {
    // Handle drag-and-drop functionality
    fileDropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        fileDropZone.classList.add('dragover');
    });

    fileDropZone.addEventListener('dragleave', () => {
        fileDropZone.classList.remove('dragover');
    });

    fileDropZone.addEventListener('drop', (e) => {
        e.preventDefault();
        fileDropZone.classList.remove('dragover');
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            fileInput.files = files;
            fileNameDisplay.textContent = `Selected file: ${files[0].name}`;
        }
    });

    // Handle file selection via button
    addFileBtn.addEventListener('click', () => {
        fileInput.click();
    });

    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = `Selected file: ${fileInput.files[0].name}`;
        }
    });
});
