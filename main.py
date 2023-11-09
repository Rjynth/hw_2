def read_cookbook(filename):
  cook_book = {}
  with open("cookbook.txt") as file:
      while True:
          dish_name = file.readline().strip()
          if not dish_name:
              break

          ingredient_count = int(file.readline().strip())

          ingredients = []
          for _ in range(ingredient_count):
              ingredient_info = file.readline().strip().split(' | ')
              ingredient_name = ingredient_info[0]
              quantity = int(ingredient_info[1])
              measure = ingredient_info[2]
              ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})

          cook_book[dish_name] = ingredients
          file.readline()

  return cook_book


def get_shop_list_by_dishes(dishes, person_count, cook_book):
  shop_list = {}
  for dish in dishes:
      ingredients = cook_book.get(dish)
      if not ingredients:
          continue

      for ingredient in ingredients:
          ingredient_name = ingredient['ingredient_name']
          quantity = ingredient['quantity'] * person_count
          measure = ingredient['measure']

          if ingredient_name in shop_list:
              shop_list[ingredient_name]['quantity'] += quantity
          else:
              shop_list[ingredient_name] = {'measure': measure, 'quantity': quantity}

  return shop_list


cook_book = read_cookbook('files/cookbook.txt')
dishes = ['Запеченный картофель', 'Омлет']
person_count = 2

shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)
print(shop_list)
