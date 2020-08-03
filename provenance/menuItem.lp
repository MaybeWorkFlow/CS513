% Menu Item Data Provenance
menuItem(contraint_transformation, "MenuItem.csv").
menuItem("id:UNIQUE", contraint_transformation).
menuItem("menu_page_id:FOREIGN_KEY(menu_page_id)_REFERENCES_MenuPage(id)", contraint_transformation).
menuItem("(price|high_price):price>high_price", contraint_transformation).
menuItem("(created_at|updated_at):created_at_>_updated_at", contraint_transformation).
menuItem("high_price:high_price_>_0", contraint_transformation).
menuItem("price:price_>_0", contraint_transformation).
menuItem("MenuItem.csv", contraint_transformation).

menuItem_provenance(X,Y) :- menuItem(X,Y).
menuItem_provenance(X,Y) :- menuItem(X,Z), menuItem(Z,Y).

ans(X) :- menuItem_provenance(X, contraint_transformation).

#show ans/1.
