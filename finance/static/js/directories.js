// import { loadOptions } from "./utils";
const tabs = document.querySelectorAll('.tab');

tabs.forEach(tab => {
  tab.addEventListener('click', () => {
    // убрать active у всех
    tabs.forEach(t => t.classList.remove('active'));

    // добавить active текущему
    tab.classList.add('active');
  });
});
console.log("TOP layer");
document.addEventListener("DOMContentLoaded", () => {
  const forms = document.querySelectorAll(
    "#type-form, #status-form, #category-form, #subcategory-form"
  );

  document.querySelectorAll(".open-form-btn").forEach(button => {
    button.addEventListener("click", () => {

      // скрыть все формы
      forms.forEach(form => form.classList.add("d-none"));

      // показать нужную
      document
        .getElementById(button.dataset.target)
        .classList.remove("d-none");
    });
  });

  document.querySelectorAll(".close-form-btn").forEach(button => {
    button.addEventListener("click", () => {
      button.closest("div").classList.add("d-none");
    });
  });

});

console.log(document.querySelectorAll(".edit-type"));
console.log(document.querySelector("#type-form"));
console.log(document.querySelector("#id_name"));


// Почему-то вылетело из DomCOntentLoaded
console.log("Inside DOMContentLoaded");

const typeSelect = document.querySelector("#type-select");
const categorySelect = document.querySelector("#category-select");

const categoriesList = document.querySelector("#categories-list");
const subcategoriesList = document.querySelector("#subcategories-list");

fetch("/ajax/categories/")
  .then(response => response.json())
  .then(categories => {
    categorySelect.innerHTML = "<option value=''>-----</option>";
    categories.forEach(category => {
      let option = document.createElement("option");
      option.value = category.id;
      option.textContent = category.name;
      categorySelect.appendChild(option);
    })
  })

console.log(categoriesList);

// if (!typeSelect || !categorySelect) {
//   return;
// }
console.log(typeSelect);


typeSelect.addEventListener("change", function () {
  const typeId = this.value;
  console.log("CHANGE FIRED", this.value);

  if (!typeId) {
    categoriesList.innerHTML = "";
    subcategoriesList.innerHTML = "";
    return;
  }

  loadCategories(typeId);
});

categorySelect.addEventListener("change", function () {
  const categoryId = this.value;

  if (!categoryId) {
    subcategoriesList.innerHTML = "";
    return;
  }

  loadSubcategories(categoryId);

});

document.querySelectorAll(".edit-type").forEach(btn => {
  btn.addEventListener("click", () => {
    console.log("Clicked");
    document.querySelector("#type-form").classList.remove("d-none");

    document.querySelector("#type-form #id_name").value = btn.dataset.name;
    document.querySelector("#type-form form").action =
      `/directories/type/${btn.dataset.id}/edit/`;
  });
});

document.querySelectorAll(".edit-status").forEach(btn => {
  btn.addEventListener("click", () => {
    document.querySelector("#status-form").classList.remove("d-none");

    document.querySelector("#status-form #id_name").value = btn.dataset.name;
    document.querySelector("#status-form form").action =
      `/directories/status/${btn.dataset.id}/edit/`;
  });
});

function loadCategories(typeId) {
  fetch(`/ajax/categories?type_id=${typeId}`)
    .then(res => res.json())
    .then(categories => {

      categoriesList.innerHTML = "";

      categories.forEach(category => {
        categoriesList.insertAdjacentHTML(
          "beforeend",
          `
            <li class="list-group-item d-flex justify-content-between align-items-center mt-3">
                <span>${category.name}</span>

                <div>
                    <button
                        class="btn btn-outline-primary btn-sm me-2 edit-category"
                        data-id="${category.id}"
                        data-name="${category.name}"
                        data-type="${category.type_id}"
                    >
                        Изменить
                    </button>

                    <button class="btn btn-outline-danger btn-sm">
                        Удалить
                    </button>
                </div>
            </li>
          `
        );
      });

      attachCategoryEditHandlers(); // важно
    });
}

function attachCategoryEditHandlers() {
  document.querySelectorAll(".edit-category").forEach(btn => {
    btn.addEventListener("click", () => {
      console.log("Edit category clicked");

      // показать форму
      document.querySelector("#category-form").classList.remove("d-none");

      // заполнить поля формы
      document.querySelector("#category-form #id_name").value = btn.dataset.name;
      document.querySelector("#category-form #id_type").value = btn.dataset.type;

      // поменять action формы
      document.querySelector("#category-form form").action =
        `/directories/category/${btn.dataset.id}/edit/`;
    });
  });
}

// function loadCategories(typeId) {
//   fetch(`/ajax/categories?type_id=${typeId}`)
//     .then(res => res.json())
//     .then(categories => {

//       categoriesList.innerHTML = "";

//       categories.forEach(category => {
//         categoriesList.insertAdjacentHTML(
//           "beforeend",
//           `
//                         <li class="list-group-item d-flex justify-content-between align-items-center mt-3">
//                             <span>${category.name}</span>

//                             <div>
//                                 <button class="btn btn-outline-primary btn-sm me-2">
//                                     Изменить
//                                 </button>

//                                 <button class="btn btn-outline-danger btn-sm">
//                                     Удалить
//                                 </button>
//                             </div>
//                         </li>
//                         `
//         );
//       });
//     });
// }



function attachSubcategoryEditHandlers() {
  document.querySelectorAll(".edit-subcategory").forEach(btn => {
    btn.addEventListener("click", () => {

      const form = document.querySelector("#subcategory-form");

      form.classList.remove("d-none");

      // ВАЖНО: ограничиваемся формой (без конфликтов id)
      form.querySelector("#subcategory-form #id_name").value = btn.dataset.name;
      form.querySelector("#subcategory-form #id_category").value = btn.dataset.category;

      form.querySelector("form").action =
        `/directories/subcategory/${btn.dataset.id}/edit/`;
    });
  });
}

function loadSubcategories(categoryId) {
  fetch(`/ajax/subcategories?category_id=${categoryId}`)
    .then(res => res.json())
    .then(subcategories => {

      subcategoriesList.innerHTML = "";

      subcategories.forEach(subcategory => {
        subcategoriesList.insertAdjacentHTML(
          "beforeend",
          `
      <li class="list-group-item d-flex justify-content-between align-items-center mt-2">
          <span>${subcategory.name}</span>

          <div>
              <button
                  class="btn btn-outline-primary btn-sm me-2 edit-subcategory"
                  data-id="${subcategory.id}"
                  data-name="${subcategory.name}"
                  data-category="${subcategory.category_id}"
              >
                  Изменить
              </button>

              <button class="btn btn-outline-danger btn-sm">
                  Удалить
              </button>
          </div>
      </li>
    `
        );
      });
      attachSubcategoryEditHandlers();
    });

  
}