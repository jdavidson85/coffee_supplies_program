import sqlite3


def main():
    coffee_db = None
    try:
        coffee_db = sqlite3.connect('coffee.db')
        coffee_cursor = coffee_db.cursor()
        coffee_cursor.execute("""Select Category From Coffee""")
        category_list = coffee_cursor.fetchall()

        unique_categories = []
        for category in category_list:
            if category[0] not in unique_categories:
                unique_categories.append(category[0])


        print("Category       Product      Supplier")
        print("==========   ===========   ==========")


        unique_categories.sort()
        for category in unique_categories:
            print(category)
            coffee_cursor.execute("""Select  *   From Cofeee where category ==  ?""")
            product_list = coffee_cursor.fetchall()
            for product in product_list:
                print(f"        {product[1]:20}  {product[3]}")

    except sqlite3.Error:
        print("SQL error encountered")
    finally:
        if coffee_db is not None:
            coffee_db.close()


main()