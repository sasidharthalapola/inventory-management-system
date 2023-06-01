#Establish a connection to the SQL server
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
import pyodbc

server = 'SASIDHAR\SQLEXPRESS'
database = 'NEW_IMS'
driver = '{SQL Server}'

connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};trusted_connection=yes'

conn = pyodbc.connect(connection_string)

#cn = conn.cursor()

# cn.execute("SELECT * FROM CUSTOMER")
#print(cn.fetchall())
#using the variables the data has been inserted by using print(f"{}{}")
# customer_name = 'chotu'
# customer_address = 'sangareddy'
# customer_email = 'chotu@gmail.com'
#inserting the data into the customer table....
#cn.execute("insert into customer(customer_name.customer_address,customer_email) values ('srikanth','nagaram','srikanth@gmail.com')")
'''
cn.execute(f"insert into customer(customer_name,customer_address,customer_email) values ('{customer_name}','{customer_address}','{customer_email}')")

#to see the changes in the sql server we have to use commit
conn.commit()
'''
#-----'/' for the home page we use forward slash
@app.route('/')   #routing the homepage
def home():
    return render_template('index.html')

@app.route('/show-customers')
def customer_show():
    cn = conn.cursor()
    cn.execute("select * from customer")
    data = []
    for i in cn.fetchall():
        customer = {}
        customer['customer_id']=i[0]
        customer['customer_name']=i[1]
        customer['customer_address']=i[2]
        customer['customer_email']=i[3]
        data.append(customer)

    return render_template('showcustomers.html',data = data)


@app.route('/show-products')
def product_show():
    cn = conn.cursor()
    cn.execute("select * from product")
    data = []
    for i in cn.fetchall():
        product = {}
        product['product_id']=i[0]
        product['product_name']=i[1]
        product['price']=i[2]
        product['stock']=i[3]
        product['supplier_id']=i[4]
        data.append(product)

    return render_template('showproduct.html',data=data)

@app.route('/show-orders')
def orders_show():
    cn = conn.cursor()
    cn.execute("select * from orders")
    data = []
    for i in cn.fetchall():
        orders = {}
        orders['order_id']=i[0]
        orders['product_id']=i[1]
        orders['customer_id']=i[2]
        orders['quantity']=i[3]
        data.append(orders)

        return render_template('showorders.html',data=data)

@app.route('/show-supplier')
def supplier_show():
    cn = conn.cursor()
    cn.execute("select * from supplier")
    data = []
    for i in cn.fetchall():
        supplier = {}
        supplier['supplier_id']=i[0]
        supplier['supplier_name']=i[1]
        supplier['supplier_address']=i[2]
        supplier['supplier_email']=i[3]
        data.append(supplier)

    return render_template('showsupplier.html',data=data)

@app.route('/add-customer',methods=['GET','POST'])
def addcustomer():
    if request.method == 'POST':
         cn = conn.cursor()
         customername=request.form.get('name')
         customeraddress=request.form.get('address')
         customeremail=request.form.get('email')
         cn.execute(f"insert into customer(customer_name,customer_address,customer_email)values('{customername}','{customeraddress}','{customeremail}')")
         conn.commit()
         print('data has been inserted')
         return jsonify({'message':'sucessful'})
    else:
        return render_template('addcustomer.html')
    

@app.route('/add-product',methods=['GET','POST'])
def addproduct():
    if request.method == 'POST':
         cn = conn.cursor()
         productname = request.form.get('name')
         stock=request.form.get('stock')
         price=request.form.get('price')
         supplier_id=request.form.get('supplier_id')
         cn.execute(f"insert into product(product_name,stock,price,supplier_id)values('{productname}','{stock}','{price}','{supplier_id}')")
         conn.commit()
         print('data has been inserted')
         return jsonify({'message':'sucessful'})
    else:
        return render_template('addproduct.html')


@app.route('/add-orders',methods=['GET','POST'])
def addorders():
    if request.method == 'POST':
         cn = conn.cursor()
         productid=request.form.get('productid')
         customerid=request.form.get('customerid')
         quantity=request.form.get('quantity')
         cn.execute(f"insert into orders(product_id,customer_id,quantity)values('{productid}','{customerid}','{quantity}')")
         conn.commit()
         print('data has been inserted')
         return jsonify({'message':'sucessful'})
    else:
        return render_template('addorders.html')
    


@app.route('/add-supplier',methods=['GET','POST'])
def addsuplier():
    if request.method == 'POST':
         cn = conn.cursor()
         suppliername=request.form.get('suppliername')
         supplieraddress=request.form.get('supplieraddress')
         supplieremail=request.form.get('supplieremail')
         cn.execute(f"insert into supplier(supplier_name,supplier_address,supplier_email)values('{suppliername}','{supplieraddress}','{supplieremail}')")
         conn.commit()
         print('data has been inserted')
         return jsonify({'message':'sucessful'})
    else:
        return render_template('addsupplier.html')



@app.route('/update-customer',methods=['GET','POST'])
def updatecustomer():
    if request.method == 'POST':
         cn = conn.cursor()
         customerid=request.form.get("customerid")
         change=request.form.get("change")
         newvalue=request.form.get("newvalue")
         cn.execute(f"update customer set {change}='{newvalue}' where customer_id = '{customerid}'")
         conn.commit()
         print('data has been updated')
         return jsonify({'message':'sucessfull'})
    else:
         return render_template('updatecustomer.html')
    

@app.route('/update-product',methods=['GET','POST'])
def updateproduct():
    if request.method == 'POST':
         cn = conn.cursor()
         productid=request.form.get("productid")
         change=request.form.get("change")
         newvalue=request.form.get("newvalue")
         cn.execute(f"update product set {change}='{newvalue}' where product_id = '{productid}'")
         conn.commit()
         print('data has been updated')
         return jsonify({'message':'sucessfull'})
    else:
         return render_template('updateproduct.html')
    

@app.route('/update-orders',methods=['GET','POST'])
def updateorders():
    if request.method == 'POST':
         cn = conn.cursor()
         orderid=request.form.get("orderid")
         change=request.form.get("change")
         newvalue=request.form.get("newvalue")
         cn.execute(f"update orders set {change}='{newvalue}' where order_id = '{orderid}'")
         conn.commit()
         print('data has been updated')
         return jsonify({'message':'sucessfull'})
    else:
         return render_template('updateorders.html')
    


@app.route('/update-supplier',methods=['GET','POST'])
def updatesupplier():
    if request.method == 'POST':
         cn = conn.cursor()
         supplierid=request.form.get("supplierid")
         change=request.form.get("change")
         newvalue=request.form.get("newvalue")
         cn.execute(f"update supplier set {change}='{newvalue}' where supplier_id = '{supplierid}'")
         conn.commit()
         print('data has been updated')
         return jsonify({'message':'sucessfull'})
    else:
         return render_template('updatesupplier.html')
    





@app.route('/delete-customer', methods=['GET', 'POST'])
def deletecustomer():
    if request.method == 'POST':
        customerid = request.form.get("customerid")
        cn = conn.cursor()
        
        try:
            cn.execute("DELETE FROM ORDERS WHERE CUSTOMER_ID = ?", customerid)
            cn.execute("DELETE FROM CUSTOMER WHERE CUSTOMER_ID = ?", customerid)
            conn.commit()
            return jsonify({'message': 'successful'})
        except Exception as e:
            conn.rollback()
            return jsonify({'message': 'error', 'error_message': str(e)})
        finally:
            cn.close()

    else:
        return render_template('deletecustomer.html')



if __name__ == '__main__':
    app.run()

