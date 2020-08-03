% Dish Data Provenance
dish(text_transform1,"Dish_lower.csv").
dish("expression:value.lower()", text_transform1).
dish("dish.csv",text_transform1).
dish(text_transform2, "Dish_whitespace_cleanup.csv").
dish("expression:value.ltrim()", text_transform2).
dish("expression:value.rtrim()", text_transform2).
dish("Dish_lower.csv", text_transform2).
dish(csv_transform1, "Dish_description_deleted.csv").
dish("drop('description')", csv_transform1).
dish("Dish_whitespace_cleanup.csv", csv_transform1).
dish(csv_transform2, "Dish_clusters.csv").
dish("Dish_description_deleted.csv", csv_transform2).


dish_provenance(X,Y) :- dish(X,Y).
dish_provenance(X,Y) :- dish(X,Z), dish(Z,Y).


ans(X) :- dish_provenance(X, csv_transform2).

#show ans/1.