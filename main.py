from flask import Flask, render_template, request
import pymysql

db = pymysql.connect("localhost","root","12345678","shoppinglist")
app = Flask(__name__)


def VerifyNew(InsertID):
    cursor4 = db.cursor()
    sql = "select ProductID from product"
    cursor4.execute(sql)
    IDs = cursor4.fetchall()
    IDsList = []
    for i in IDs:
        IDsList.append(i[0])
    if InsertID in IDsList:
        return 0
    else:
        return 1

#the index


#View a product only
@app.route("/ViewAProduct", methods = ["GET","POST"])
def ViewAProduct():
    cursor1 = db.cursor()
    cursor2 = db.cursor()
    if request.method == "POST":
        ID = request.form.get("ID")
    else:
        ID = request.args.get("ID")
    cursor2.execute("select count(*) from product")
    num = cursor2.fetchall()
    if ID != None:
        if int(ID) <= int(num[0][0]):
            sql = "select * from product where ProductID = '%s'" %(ID)
            cursor1.execute(sql)
            item = list(cursor1.fetchall())
            cursor1.close()
            return render_template("ViewAProduct.html", item = item)
        else:
            return render_template("ViewAProduct.html",item = [("None","None","None")])
    else:
        return render_template("ViewAProduct.html",item = [("None","None","None")])

#show the product list
@app.route("/ProductList")
def ProductList(): 
    cursor3 = db.cursor()
    sql = "select * from product"
    cursor3.execute(sql)
    items = list(cursor3.fetchall())
    cursor3.close()
    return render_template("product.html", items = items)

#add a product
@app.route("/AddProduct", methods = ["GET","POST"])
def AddProduct():
    if request.method == "POST":
        ID = request.form.get("ID")
        Name = request.form.get("Name")
        Price = request.form.get("Price")
    else:
        ID = request.args.get("ID")
        Name = request.args.get("Name")
        Price = request.args.get("Price")
    if ID != None:
        if VerifyNew(int(ID)) == 1:
            cursor5 = db.cursor()
            sql = "insert into product(ProductID,ProductName,ProductUnitPrice) values('%s','%s','%s')" %(ID,Name,Price)
            cursor5.execute(sql)
            cursor5.close()
            db.commit()
            status = "Successfully add the product！"
            return render_template("AddProduct.html", status = status)
        else:
            status = "Fail to add, because the product is already in the product table!"
            return render_template("AddProduct.html", status = status)
    else:
        return render_template("AddProduct.html", status = "Add Status")

if __name__ == "__main__":
    app.debug == False
    app.run(host="localhost",port=5000)
    