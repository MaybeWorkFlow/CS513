"""
@begin MenuItem_Contraint  @desc Workflow for cleaning New York Public Library Menus - Menu Item DataSet
"""



"""
@begin contraint_transformation @desc adding sql integrity constraints
@in id:UNIQUE
@in menu_page_id:FOREIGN_KEY(menu_page_id)_REFERENCES_MenuPage(id)
@in (price|high_price):price>high_price
@in (created_at|updated_at):created_at_>_updated_at
@in high_price:high_price_>_0
@in price:price_>_0
@in MenuItem.csv  @uri http://menus.nypl.org/data
"""

"""
@out MenuItem.csv
@end contraint_transformation
"""



"""
@end MenuItem_Contraint
"""