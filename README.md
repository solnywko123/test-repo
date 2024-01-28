#Без линтинга
## Установка

1. Клонируйте репозиторий:

```bash
git clone https://github.com/solnywko123/test-repi

2. Создайте виртуальное окружение

python -m venv .venv

активируете
source .venv/bin/activate

Установите зависимости

проведите миграции


Запустите сервер:


1. add_product_to_recipe
Endpoint: /add_product_to_recipe/

GET-параметры:

recipe_id: Идентификатор рецепта.
product_id: Идентификатор продукта.
weight: Вес продукта в граммах.
Пример использования:

bash
Copy code
curl "http://localhost:8000/add_product_to_recipe/?recipe_id=1&product_id=2&weight=150"
2. cook_recipe
Endpoint: /cook_recipe/

GET-параметры:

recipe_id: Идентификатор рецепта.
Пример использования:

bash
Copy code
curl "http://localhost:8000/cook_recipe/?recipe_id=1"
3. show_recipes_without_product
Endpoint: /show_recipes_without_product/

GET-параметры:

product_id: Идентификатор продукта.
Пример использования:

bash
Copy code
curl "http://localhost:8000/show_recipes_without_product/?product_id=2"

