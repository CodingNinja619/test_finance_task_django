document.addEventListener("DOMContentLoaded", function () {

  const typeSelect = document.querySelector("#id_type");
  const categorySelect = document.querySelector("#id_category");
  const subcategorySelect = document.querySelector("#id_subcategory");

  const selectedType = typeSelect.value;
  const selectedCategory = categorySelect.value;

  categorySelect.disabled = true;
  subcategorySelect.disabled = true;

  if (selectedType) {
    categorySelect.disabled = false;

    loadOptions(
      `/ajax/categories?type_id=${selectedType}`,
      categorySelect,
      "Выберите категорию",
      selectedCategory
    );
  } else {
    categorySelect.innerHTML = "<option>Сначала выберите тип</option>";
  }
  

  if (selectedCategory) {
    subcategorySelect.disabled = false;

    loadOptions(
      `/ajax/subcategories?category_id=${selectedCategory}`,
      subcategorySelect,
      "Выберите категорию",
      selectedSubcategory
    );
  } else {
    subcategorySelect.innerHTML = "<option>Сначала выберите категорию</option>";
  }

  // categorySelect.innerHTML = "<option>Сначала выберите тип</option>";
  // subcategorySelect.innerHTML = "<option>Сначала выберите категорию</option>";

  typeSelect.addEventListener("change", function () {
    let typeId = this.value;
    if (typeId) {
      categorySelect.disabled = false;
      loadOptions(`/ajax/categories?type_id=${typeId}`, categorySelect);
    }
    else {
      categorySelect.innerHTML = "<option>Сначала выберите тип</option>";
      categorySelect.disabled = true;
    }
  });

  categorySelect.addEventListener("change", function () {
    let categoryId = this.value;
    console.log(categoryId);
    if (categoryId) {
      subcategorySelect.disabled = false;
      loadOptions(`/ajax/subcategories?category_id=${categoryId}`, subcategorySelect);
    }
    else {
      subcategorySelect.innerHTML = "<option>Сначала выберите категорию</option>";
      subcategorySelect.disabled = true;
    }
  })
})

function loadOptions(url, selectElement, placeholder = "-----", selectedId = null) {
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

// function loadOptions(url, selectElement, placeholder="-----") {
//   fetch(url)
//     .then(response => response.json())
//     .then(data => {
//       selectElement.innerHTML = `<option value=''>${placeholder}</option>`;
//       data.forEach(item => {
//         let option = document.createElement("option");
//         option.value = item.id;
//         option.textContent = item.name;
//         selectElement.appendChild(option);
//       })
//     });
// }

// function loadCategories(typeId, categorySelect) {
//   console.log("f");
//   fetch("/ajax/categories/?type_id=" + typeId)
//     .then(response => response.json())
//     .then(categories => {
//       categorySelect.innerHTML = "<option value=''>------</option>";
//       categories.forEach(category => {
//         let option = document.createElement("option");
//         option.value = category.id;
//         option.textContent = category.name;
//         categorySelect.appendChild(option);
//       })
//     })
//   }

