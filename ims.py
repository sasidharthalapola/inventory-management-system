#Establish a connection to the SQL server
from flask import Flask, jsonify, request, render_template
app = Flask(__name__)
import sqlite3

conn = sqlite3.connect('sql.db')
app = Flask(__name__)

def idgenerator(tab):
    conn = sqlite3.connect('sql.db')
    cn = conn.cursor()
    idval = ''
    if tab=='CUSTOMER':
        idval = 'CUSTOMER_ID'
    if tab=='PRODUCT':
        idval = 'PRODUCT_ID'
    if tab=='ORDERS':
        idval = 'ORDER_ID'
    if tab=='SUPPLIER':
        idval = 'SUPPLIER_ID'
    print(tab,idval)
    cn.execute(f"SELECT {idval} FROM {tab}")
    new = cn.fetchall()
    cud = str(new[len(new)-1][0])
    for i in range(len(str(cud))):
        if cud[i].isnumeric():
            f = i
            break
    myint = cud[f:]
    myint = int(myint)+1
    return idval[0:3]+str(myint)

@app.route('/')   
def home():
    return render_template('index.html')

@app.route('/show-customers')
def customer_show():
    conn = sqlite3.connect('sql.db')
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
    conn = sqlite3.connect('sql.db')
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
    conn = sqlite3.connect('sql.db')
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
    conn = sqlite3.connect('sql.db')
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
         conn = sqlite3.connect('sql.db')
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
         conn = sqlite3.connect('sql.db')
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
         conn = sqlite3.connect('sql.db')
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
         conn = sqlite3.connect('sql.db') 
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
         conn = sqlite3.connect('sql.db')
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
         conn = sqlite3.connect('sql.db')
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
         conn = sqlite3.connect('sql.db')
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
         conn = sqlite3.connect('sql.db')
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
        conn = sqlite3.connect('sql.db')
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
    

@app.route('/delete-product', methods=['GET', 'POST'])
def product_delete():
    if request.method == 'POST':
        product_id = request.form.get("product_id")
        conn = sqlite3.connect('sql.db')
        cn = conn.cursor()

        try:
            cn.execute("DELETE FROM ORDERS WHERE product_id = ?", product_id)
            cn.execute("DELETE FROM product WHERE product_id = ?", product_id)  # Updated column name
            conn.commit()
            return jsonify({'message': 'successful'})
        except Exception as e:
            conn.rollback()
            return jsonify({'message': 'error', 'error_message': str(e)})
        finally:
            cn.close()
    else:
        return render_template('deleteproduct.html')
        
@app.route('/delete-orders', methods=['GET', 'POST'])
def orders_delete():
    if request.method == 'POST':
        order_id = request.form.get("order_id")
        conn = sqlite3.connect('sql.db')
        cn = conn.cursor()

        try:
            cn.execute("DELETE FROM ORDERS WHERE order_ID = ?", order_id)
            conn.commit()
            return jsonify({'message': 'successful'})
        except Exception as e:
            conn.rollback()
            return jsonify({'message': 'error', 'error_message': str(e)})
        finally:
            cn.close()
    else:
        return render_template('deleteorders.html')
    
@app.route('/delete-supplier', methods=['GET', 'POST'])
def supplier_delete():
    if request.method == 'POST':
        supplier_id = request.form.get("supplier_id")
        conn = sqlite3.connect('ims.db')
        cn = conn.cursor()

        try:
            # Delete related records in PRODUCT table first
            cn.execute("DELETE FROM PRODUCT WHERE supplier_id = ?", supplier_id)
            conn.commit()

            # Delete the supplier
            cn.execute("DELETE FROM supplier WHERE supplier_id = ?", supplier_id)
            conn.commit()

            return jsonify({'message': 'successful'})
        except Exception as e:
            conn.rollback()
            return jsonify({'message': 'error', 'error_message': str(e)})
        finally:
            cn.close()

    else:
        return render_template('deletesupplier.html')


if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 5000, debug = False)

