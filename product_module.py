import json
import sqlite3
import sys
import jinja2


class Product:
    def __init__(self,product_id_number):
        """Function that initiates a class Product.  Function connects to a sql database, and populates attributes for the object
            Argument: product id number
        """
        self.id = product_id_number
        conn = sqlite3.connect(r'product.db')
        c = conn.cursor()
        sql_result = c.execute("SELECT brand, list_price, product_description, product_name, sale_price from product where product_id = ?", (product_id_number,))
        for item in sql_result:
            self.brand = item[0]
            self.list_price = item[1]
            self.description = item[2]
            self.name = item[3]
            self.sale_price = item[4]
    def __str__(self):
        """Function that returns a string when the print function is called against an object type Product

        """
        return(f'Product(id={self.id}, brand={self.brand}, sale_price={self.sale_price})')
    
    def get_savings_pct(self):
        """Function that calculates a savings percentage based on sale price and list price
            Return values: float value reprsenting the percentage of savings
        """
        savings_pct = ( 1 - (float(self.sale_price) / float(self.list_price) ) ) * 100
        return round(savings_pct, 2)

def get_all_products():
    """Function that queries the product database and returns a list of product IDs.  Function connects to a sql database, and populates attributes for the object
        Argument: none
        Return value: list of product objects
    """
    product_id_list = []
    product_list = []
    conn = sqlite3.connect(r'product.db')
    c = conn.cursor()
    sql_result = c.execute("SELECT product_id from product")
    for item in sql_result:
        product_id_list.append(item[0])
    for item in product_id_list:
        product_list.append(Product(item))
    return product_list

if __name__ == '__main__':
    prod_id = sys.argv[1]
    this_product = Product(prod_id)

    template_dir = 'templates'
    env = jinja2.Environment()
    env.loader = jinja2.FileSystemLoader(template_dir)

    template = env.get_template('product.html')
    completed_page = template.render(product=this_product)

    wfh = open(prod_id + '.html', 'w')
    wfh.write(completed_page)
    wfh.close()