import csv
import os
import pytest
from helpers import read_csv
@pytest.fixture(scope="module")
def stock_file():
    with open('stock_data.csv', 'w', newline='') as stock_file:
        fieldnames = ['product_id', 'manufacturer_name', 'quantity_in_stock', 'supplier_contact',
                      'last_stock_update', 'price_per_unit', 'category', 'location_in_warehouse', 'reorder_threshold']
        stock_writer = csv.DictWriter(stock_file, fieldnames=fieldnames)
        stock_writer.writeheader()
        stock_writer.writerow({'product_id' : '123', 'manufacturer_name' : 'TestCompany','quantity_in_stock' : "10",
                               'supplier_contact' : '123-456-7891', 'last_stock_update' : '01/01/2000',
                               'price_per_unit': '100.00', 'category' : 'Test', 'location_in_warehouse' : 'A1', 
                               'reorder_threshold': '1'})
    yield
    os.remove('stock_data.csv')
    def test_read_csv(stock_file):
    # Arrange - set up input and expected output
    filepath = 'stock_data.csv'
    expected_length = 1
    expected_id = 123
    expected_quantity = 10
    # Act
    stock_data = read_csv(filepath)
    # Assert
    assert len(stock_data) == expected_length
    assert stock_data['product_id'][0] == expected_id
    assert stock_data['quantity_in_stock'][0] == expected_quantity
    