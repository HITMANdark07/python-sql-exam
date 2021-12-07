import mysql.connector

def createDatabase():
  mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
  )
  mycursor = mydb.cursor()
  mycursor.execute("CREATE DATABASE gift_db");

def main():
    print("Creating database and connect")
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="gift_db"
    )
    mycursor=mydb.cursor()

    createProductsTable = """CREATE TABLE Products
                    ( product_id VARCHAR(255),
                      product_name VARCHAR(255),
                      product_price double
                    );"""

    insertProducts = """INSERT INTO Products
                    ( product_id ,product_name,product_price) VALUES (%s,%s,%s)"""

    productValues=[];
    while(True):
        want = input("Do you want to exit : ")
        if not want=="yes":
            id = input("Enter Product Id: ")
            name = input("Enter Product name: ")
            price = input("Enter Product Price: ")
            productValues.append((id,name,price));
        else:
            break;
    mycursor.execute(createProductsTable)

    mycursor.executemany(insertProducts,productValues)

    mydb.commit()
    getQuery ="SELECT * FROM Products WHERE product_price < 50"
    mycursor.execute(getQuery)
    records = mycursor.fetchall()
    for record in records:
        print("Product_ID: {} Product_Name: {} Product_Price: {}".format(record[0],record[1],record[2]))

if __name__ == "__main__":
    createDatabase()
    main()