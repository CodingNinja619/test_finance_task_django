document.addEventListener("DOMContentLoaded", function () {
            const typeSelect = document.querySelector("#type-select");
            const categorySelect = document.querySelector("#category-select");
            const subcategorySelect = document.querySelector("#subcategory-select");

            if (!typeSelect || !categorySelect || !subcategorySelect) {
                return;
            }

            const selectedType = typeSelect.value;
            const selectedCategory = categorySelect.value;
            const selectedSubcategory = subcategorySelect.value;

            function loadCategories(typeId, selectedCategoryId = null) {
                categorySelect.innerHTML = "<option value=''>-----</option>";

                if (!typeId) {
                    categorySelect.disabled = true;
                    subcategorySelect.innerHTML = "";
                    subcategorySelect.disabled = true;
                    return;
                }

                categorySelect.disabled = false;

                fetch(`/ajax/categories/?type_id=${typeId}`)
                    .then(res => res.json())
                    .then(data => {
                        data.forEach(cat => {
                            const option = document.createElement("option");
                            option.value = cat.id;
                            option.textContent = cat.name;

                            if (selectedCategoryId && String(cat.id) === String(selectedCategoryId)) {
                                option.selected = true;
                            }

                            categorySelect.appendChild(option);
                        });

                        if (selectedCategoryId) {
                            loadSubcategories(selectedCategoryId, selectedSubcategory);
                        } else {
                            subcategorySelect.innerHTML = "";
                            subcategorySelect.disabled = true;
                        }
                    });
            }

            function loadSubcategories(categoryId, selectedSubId = null) {
                subcategorySelect.innerHTML = "<option value=''>-----</option>";


                if (!categoryId) {
                    subcategorySelect.disabled = true;
                    return;
                }

                subcategorySelect.disabled = false;

                fetch(`/ajax/subcategories/?category_id=${categoryId}`)
                    .then(res => res.json())
                    .then(data => {
                        data.forEach(sub => {
                            const option = document.createElement("option");
                            option.value = sub.id;
                            option.textContent = sub.name;

                            if (selectedSubId && String(sub.id) === String(selectedSubId)) {
                                option.selected = true;
                            }

                            subcategorySelect.appendChild(option);
                        });
                    });
            }
            console.log(typeSelect);

            typeSelect.addEventListener("change", function () {
                console.log("type change");
                loadCategories(this.value);
            });
            console.log(categorySelect);
            categorySelect.addEventListener("change", function () {
                console.log("category change");
                console.log(this.value);
                loadSubcategories(this.value);
            });

            console.log("Listener attached");

            if (selectedType) {
                loadCategories(selectedType, selectedCategory);
            } else {
                categorySelect.disabled = true;
                subcategorySelect.disabled = true;
            }

            const form = document.querySelector("form[method='post']");
            form.addEventListener("submit", function () {
                categorySelect.disabled = false;
                subcategorySelect.disabled = false;
            });
        });