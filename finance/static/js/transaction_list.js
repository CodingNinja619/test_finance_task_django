document.addEventListener("DOMContentLoaded", function () {

            const typeSelect = document.querySelector("#type-select");
            const categorySelect = document.querySelector("#category-select");
            const subcategorySelect = document.querySelector("#subcategory-select");

            const selectedType = typeSelect.value;
            const selectedCategory = categorySelect.value;
            const selectedSubcategory = subcategorySelect.value;

            function loadCategories(typeId, selectedCategoryId = null) {

                categorySelect.innerHTML = `<option value="">Все</option>`;

                if (!typeId) {
                    categorySelect.disabled = true;
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
                        }
                    });
            }

            function loadSubcategories(categoryId, selectedSubId = null) {

                subcategorySelect.innerHTML = `<option value="">Все</option>`;

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

            // events
            typeSelect.addEventListener("change", function () {
                loadCategories(this.value);
                subcategorySelect.innerHTML = `<option value="">Все</option>`;
                subcategorySelect.disabled = true;
            });

            categorySelect.addEventListener("change", function () {
                loadSubcategories(this.value);
            });

            // восстановление состояния после reload
            if (selectedType) {
                loadCategories(selectedType, selectedCategory);
            } else {
                categorySelect.disabled = true;
                subcategorySelect.disabled = true;
            }

        });
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