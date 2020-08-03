
e(text_transform1,Dish_lower.csv).
e(expression:value.lower(), text_transform1).
e(dish.csv,text_transform1).
e(text_transform2, Dish_whitespace_cleanup.csv).
e(expression:value.ltrim(), text_transform2).
e(expression:value.rtrim(), text_transform2).
e(Dish_lower.csv, text_transform2).
e(csv_transform1, Dish_description_deleted.csv).
e(drop('description'), csv_transform1).
e(Dish_whitespace_cleanup.csv, csv_transform1).
e(csv_transform2, Dish_clusters.csv).
e(Dish_description_deleted.csv, csv_transform2).


tc(X,Y) :- e(X,Y).
tc(X,Y) :- e(X,Z), e(Z,Y).
