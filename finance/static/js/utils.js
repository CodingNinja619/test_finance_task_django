export function loadOptions(url, selectElement, placeholder = "-----", selectedId = null) {
  fetch(url)
    .then(response => response.json())
    .then(data => {
      selectElement.innerHTML = `<option value="">${placeholder}</option>`;

      data.forEach(item => {
        const option = document.createElement("option");
        option.value = item.id;
        option.textContent = item.name;

        if (selectedId && String(item.id) === String(selectedId)) {
          option.selected = true;
        }

        selectElement.appendChild(option);
      });
    });
}