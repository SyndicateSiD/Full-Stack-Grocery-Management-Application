from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("select product.product_id, product.product_name, product.unit_id, product.price_per_unit, unit.unit_type from product inner join unit on product.unit_id=unit.unit_id  order by product.product_name")
    cursor.execute(query)
    response = []
    for (product_id, product_name, unit_id, price_per_unit, unit_type) in cursor:
        response.append({
            'product_id': product_id,
            'product_name': product_name,
            'unit_id': unit_id,
            'price_per_unit': price_per_unit,
            'unit_type': unit_type
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO product"
             "(product_name, unit_id, price_per_unit)"
             "VALUES (%s, %s, %s)")
    data = (product['product_name'], product['unit_id'], product['price_per_unit'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM product where product_id=" + str(product_id))
    cursor.execute(query)
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    
    print(insert_new_product(connection, {
        'product_name': 'capsicum',
        'unit_id': 2,
        'price_per_unit': 40
    }))
  