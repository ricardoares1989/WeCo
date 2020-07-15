#DATABASE SETTINGS
config = {
    'user': 'root',
    'password': 'Protection1989',
    'host': '127.0.0.1',
    'database': 'WECO',
}

DB_NAME = 'WECO'

TABLES = {}

TABLES['products'] = (
    "CREATE TABLE IF NOT EXISTS products ("
    "   `product_id` INTEGER PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "   `name` VARCHAR(50) NOT NULL"
    ") ENGINE=InnoDB")

TABLES['registers'] = (
    "CREATE TABLE IF NOT EXISTS registers ("
    "`register_id` BIGINT PRIMARY KEY NOT NULL AUTO_INCREMENT,"
    "`weigth` FLOAT(6,2) NOT NULL,"
    "`product_id` INTEGER NOT NULL,"
    "`created_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"
    "`updated_at` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP"
    "   ON UPDATE CURRENT_TIMESTAMP,"
    "FOREIGN KEY (product_id) REFERENCES products(product_id)"
    ") ENGINE=InnoDB")
