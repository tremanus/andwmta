document.getElementById("QrtsBett").addEventListener("change", function () {
    document.getElementById("option1-fields").style.display = this.value === "1" ? "block" : "none";
    document.getElementById("option2-fields").style.display = this.value === "2" ? "block" : "none";
    document.getElementById("option3-fields").style.display = this.value === "3" ? "block" : "none";
});

const form = document.getElementById('form');
        form.addEventListener('submit', async function (event) {
            event.preventDefault();

            const formData = new FormData(form);
            const response = await fetch('/process', {
                method: 'POST',
                body: formData
            });

            const result = await response.text();
            document.getElementById('results').innerHTML = result;
        });

document.addEventListener('DOMContentLoaded', () => {
    // Option 1 logic
    const prefixCheckbox = document.getElementById('prefix-only');
    const suffixCheckbox = document.getElementById('suffix-only');
    const mirchaInput = document.getElementById('mircha-value');

    function updateMirchaValue() {
        if (prefixCheckbox.checked && suffixCheckbox.checked) {
            mirchaInput.value = '4'; // Both checked
        } else if (prefixCheckbox.checked) {
            mirchaInput.value = '2'; // Prefix only
        } else if (suffixCheckbox.checked) {
            mirchaInput.value = '3'; // Suffix only
        } else {
            mirchaInput.value = '1'; // Neither checked
        }
    }

    prefixCheckbox.addEventListener('change', updateMirchaValue);
    suffixCheckbox.addEventListener('change', updateMirchaValue);

    // Option 2 logic
    const prefixCheckbox2 = document.getElementById('prefix-only-2');
    const suffixCheckbox2 = document.getElementById('suffix-only-2');
    const mirchaInput2 = document.getElementById('mircha2-value');

    function updateMircha2Value() {
        if (prefixCheckbox2.checked && suffixCheckbox2.checked) {
            mirchaInput2.value = '4'; // Both checked
        } else if (prefixCheckbox2.checked) {
            mirchaInput2.value = '2'; // Prefix only
        } else if (suffixCheckbox2.checked) {
            mirchaInput2.value = '3'; // Suffix only
        } else {
            mirchaInput2.value = '1'; // Neither checked
        }
    }

    prefixCheckbox2.addEventListener('change', updateMircha2Value);
    suffixCheckbox2.addEventListener('change', updateMircha2Value);
});

