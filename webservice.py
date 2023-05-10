import os
from flask import *
from werkzeug.utils import secure_filename


from src.dbconnectionnew import *
from src.newcnn import predictld
# from src.read_csv import random_forest

app=Flask(__name__)

@app.route('/farmer_register',methods=['post'])
def farmer_register():
    print(request.form)
    fname = request.form['firstname']
    lname = request.form['lastname']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    print(pin)
    phone = request.form['phone']
    email = request.form['email']
    username = request.form['uname']
    password = request.form['password']

    q = "INSERT INTO `login`  VALUES (null,%s,%s,'pending')"
    val = (username, password)
    res = iud(q, val)

    qry = "INSERT INTO `farmer` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(res), fname, lname, place, post, pin, phone, email)
    iud(qry, val1)
    return jsonify({"task": "success"})

@app.route('/login',methods=['post'])
def login():
    uname = request.form['textfield']
    psw = request.form['textfield2']
    q = "SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val = (uname, psw)
    res = selectone(q,val)
    if res is None:
        return jsonify({"task":"invalid"})
    else:
        id=res['login_id']
        type=res['type']
        return jsonify({"task":"success", "lid":id ,"type":type })


@app.route('/farmer_viewexpert',methods=['post'])
def farmer_viewexpert():
    qry = "SELECT * FROM `expert`"
    res = selectall(qry)
    return jsonify(res)


@app.route('/farmer_provide_condition',methods=['post'])
def farmer_provide_condition():
    return jsonify()

@app.route('/farmer_predict_crop_and_fertilizer',methods=['post'])
def farmer_predict_crop_and_fertilizer():
    return jsonify()

@app.route('/farmer_view_notification',methods=['post'])
def farmer_view_notification():
    qry = "SELECT * FROM `notification`"
    res = selectall(qry)
    return jsonify(res)

@app.route('/farmer_sendcomplaint',methods=['post'])
def farmer_sendcomplaint():
    lid=request.form['lid']
    complaint=request.form['complaint']
    qry = "INSERT INTO `complaint` VALUES(NULL,%s,0,%s,'pending',CURDATE())"
    val = (lid, complaint)
    iud(qry, val)
    return jsonify({"task":"success"})

@app.route('/farmer_viewreply',methods=['post'])
def farmer_viewreply():
    lid = request.form['lid']
    qry = "SELECT * FROM `complaint` where L_id=%s"
    res = selectall2(qry,lid)
    return jsonify(res)

@app.route('/farmer_viewtips',methods=['post'])
def farmer_viewtips():
    eid=request.form['eid']
    qry = "SELECT * FROM `suggestions` WHERE `E_id`=%s"
    res = selectall2(qry,eid)
    return jsonify(res)

@app.route('/farmer_addproducts',methods=['post'])
def farmer_addproducts():
    lid=request.form['lid']
    product=request.form['product']
    rate=request.form['rate']
    details=request.form['details']
    qry = "INSERT INTO `product` VALUE(NULL,%s,%s,%s,%s)"
    val = (lid,product,rate,details)
    iud(qry, val)
    return jsonify({"task":"success"})

@app.route('/farmer_manageproducts',methods=['post'])
def farmer_manageproducts():
    lid = request.form['lid']
    qry = "SELECT * FROM `product` where L_id=%s"
    res = selectall2(qry,lid)
    return jsonify(res)

@app.route('/farmer_viewproduct',methods=['post'])
def farmer_viewproduct():
    qry = "SELECT `product`.`Product`,`Rate`,`Details`,`order details`.`Quantity` FROM `order details` JOIN `product` ON `product`.`Product_id`=`order details`.`Product_id` "
    res = selectall(qry)
    return jsonify(res)

@app.route('/farmer_vieworder',methods=['post'])
def farmer_vieworder():
    print(request.form)
    lid=request.form['lid']
    qry = "SELECT `order`.*,`user`.*,`product`.*,`order details`.* FROM `user` JOIN `order` ON `order`.`U_id`=`user`.`L_id` join `order details` on `order details`.`Order_id`=`order`.`Order_id` join `product` on `product`.`Product_id`=`order details`.`Product_id` where `product`.`L_id`=%s"
    res = selectall2(qry,lid)
    print(res)
    return jsonify(res)

@app.route('/farmer_deleteproducts',methods=['post'])
def farmer_deleteproducts():
    pid = request.form['pid']
    iud("DELETE FROM `product` WHERE `Product_id`=%s",pid)
    return jsonify(task="success")



@app.route('/viewbooked_products',methods=['post'])
def viewbooked_products():
    print(request.form)
    oid = request.form['oid']
    res = selectall2("SELECT * FROM `order details` JOIN `product` ON `order details`.`Product_id`=`product`.`Product_id` AND `order details`.`Order_id`=%s",oid)
    print(res)
    return jsonify(res)


@app.route('/farmer_updatestatus',methods=['post'])
def farmer_updatestatus():
    uid = request.form['uid']
    total = request.form['total']
    qry = "INSERT INTO `order` VALUES(NULL,%s,CURDATE(),%s)"
    val = (uid, total)
    iud(qry, val)
    return jsonify({"task":"success"})

@app.route('/farmer_viewdoubt1',methods=['post'])
def farmer_viewdoubt1():
    print(request.form)
    lid=request.form['lid']
    eid=request.form['eid']
    # qry = "SELECT * FROM `complaint` JOIN `product` ON `complaint`.`prod_id`=`product`.`Product_id` JOIN `user` ON `user`.L_id=`complaint`.`L_id` WHERE `product`.`L_id`=%s"
    res = selectall2("SELECT * FROM `questions` WHERE `L_id`=%s and `E_id`=%s",(lid,eid))
    print(res)
    return jsonify(res)


@app.route('/farmer_viewdoubt',methods=['post'])
def farmer_viewdoubt():
    print(request.form)
    lid=request.form['lid']

    qry = "SELECT * FROM `complaint` JOIN `product` ON `complaint`.`prod_id`=`product`.`Product_id` JOIN `user` ON `user`.L_id=`complaint`.`L_id` WHERE `product`.`L_id`=%s and `complaint`.`Reply`='pending'"
    res = selectall2(qry,(lid))
    print(res)
    return jsonify(res)


@app.route('/sendreplyfarmer',methods=['post'])
def sendreplyfarmer():
    print(request.form)
    reply = request.form['reply']
    cid = request.form['cid']
    iud("UPDATE `complaint` SET `Reply`=%s WHERE `Complaint_id`=%s",(reply,cid))
    return jsonify(task="success")

@app.route('/farmer_senddoubt',methods=['post'])
def farmer_senddoubt():
    eid = request.form['eid']
    lid = request.form['lid']
    doubt = request.form['doubt']
    qry = "INSERT INTO `questions` VALUES (NULL,%s,%s,%s,'pending',CURDATE())"
    val = (eid,lid,doubt)
    iud(qry, val)
    return jsonify({"task":"success"})


@app.route('/farmer_sendreply',methods=['post'])
def farmer_sendreply():
    lid = request.form['lid']
    complaint = request.form['complaint']
    qry = "UPDATE `complaint` SET `Reply`=%s WHERE `Complaint_id`=%s"
    val = (lid, complaint)
    iud(qry, val)
    return jsonify({"task":"success"})

@app.route('/farmer_detectdisease',methods=['post'])
def farmer_detectdisease():
    qry = "SELECT * FROM `disease`"
    res = selectall(qry)
    return jsonify(res)

@app.route('/farmer_payment',methods=['post'])
def farmer_payment():
    return jsonify()



#------------------user--------------------#


@app.route('/user_register',methods=['post'])
def user_register():
    print(request.form)
    fname = request.form['firstname']
    lname = request.form['lastname']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    username = request.form['uname']
    password = request.form['password']

    q = "INSERT INTO `login`  VALUES (null,%s,%s,'pending')"
    val = (username, password)
    res = iud(q, val)

    qry = "INSERT INTO `user` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1 = (str(res), fname, lname, place, post, pin, phone, email)
    iud(qry, val1)
    return jsonify({"task": "success"})

@app.route('/user_login',methods=['post'])
def user_login():
    uname = request.form['textfield']
    psw = request.form['textfield2']
    q = "SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val = (uname, psw)

    res = selectone(q, val)
    if res is None:
        return jsonify({"task":"invalid"})
    else:
        return jsonify({"task":"success"})


@app.route('/user_sendcomplaint',methods=['post'])
def user_sendcomplaint():
    print(request.form)
    lid = request.form['lid']
    pid=request.form['Product']
    complaint = request.form['complaint']
    qry="INSERT INTO `complaint` VALUES(NULL,%s,%s,%s,'pending',CURDATE())"
    val=(lid,pid,complaint)
    iud(qry,val)
    return jsonify({"task":"success"})

@app.route('/user_viewreply',methods=['post'])
def user_viewreply():
    print(request.form)
    lid=request.form['lid']
    qry = "SELECT `complaint`.*,`product`.`Product` FROM `product` JOIN  `complaint` ON `complaint`.`prod_id`=`product`.`Product_id` WHERE `complaint`.`L_id`=%s "
    res = selectall2(qry,lid)
    print(res)
    return jsonify(res)

@app.route('/user_viewnotification',methods=['post'])
def user_viewnotification():
    qry = "SELECT * FROM `notification`"
    res = selectall(qry)
    return jsonify(res)

@app.route('/user_viewfarmer',methods=['post'])
def user_viewfarmer():
    qry = "SELECT * FROM `farmer`"
    res = selectall(qry)
    return jsonify(res)

@app.route('/user_viewproduct',methods=['post'])
def user_viewproduct():
    qry = "SELECT * FROM `product`"
    res = selectall(qry)
    return jsonify(res)

@app.route('/user_orderproduct',methods=['post'])
def user_orderproduct():
    lid=request.form['lid']
    pid=request.form['pid']
    qnty=request.form['qnty']
    res = selectone("SELECT * FROM `order` WHERE `U_id`=%s AND `status`='add_to_cart'")
    if res is None:
        res1 = iud("INSERT INTO `order` (`U_id`,`Date`,`Total`,`status`) VALUES(%s,CURDATE(),%s,%s)",(lid,0,'add_to_cart'))
        iud("INSERT INTO `order details` (`Product_id`,`Order_id`,`Quantity`,`Status`) VALUES(%s,%s,%s,%s)",(pid,res1,qnty,'pending'))
        return jsonify({"task":"success"})
    else:
        iud("INSERT INTO `order details` (`Product_id`,`Order_id`,`Quantity`,`Status`) VALUES(%s,%s,%s,%s)",(pid, res['Order_id'], qnty, 'pending'))
        return jsonify({"task":"success"})


@app.route('/user_orderstatus',methods=['post'])
def user_orderstatus():
    lid = request.form['lid']
    print(lid)
    # qry = "SELECT `order`.*,`order details`.*,`product`.* FROM `order` JOIN `order detals` ON `order`.`Order_id`=`order details`.`Order_id` JOIN `product` ON `order`.`U_id`=`product`.`U_id`"
    qry="SELECT `order details`.*,`order`.*,`product`.* FROM `order` JOIN `order details` ON `order`.`Order_id`=`order details`.`Order_id` JOIN `product` ON `order details`.`Product_id`=`product`.`Product_id` WHERE `order`.`U_id`=%s"
    res = selectall2(qry,lid)
    print(res)
    return jsonify(res)

# @app.route('/user_viewcart',methods=['post'])
# def user_viewcart():
#     lid=request.form['lid']
#     qry = "SELECT SUM(`product`.`Rate`*`order details`.`Quantity`) AS total ,`product`.`Product`,`product`.`Rate`,`order details`.`Quantity`  FROM `order` JOIN `order details` ON `order`.`Order_id`=`order details`.`Order_id` JOIN `product` ON `order details`.`Product_id`=`product`.`Product_id` WHERE `order`.`U_id`=%s AND `order`.`status`='cart' GROUP BY `order details`.`Product_id`"
#     res = selectall2(qry,lid)
#
#     qry1 = "SELECT SUM(`product`.`Rate`*`order details`.`Quantity`) AS total,`order`.`Order_id`  FROM `order` JOIN `order details` ON `order`.`Order_id`=`order details`.`Order_id` JOIN `product` ON `order details`.`Product_id`=`product`.`Product_id` WHERE `order`.`U_id`=%s AND `order`.`status`='cart'"
#     res1 = selectone(qry1,lid)
#     print(res1,"eeeee")
#     return jsonify(data=res,data1=int(res1['total']),oid=res1['Order_id'])

@app.route('/user_viewcart', methods=['POST'])
def user_viewcart():
    lid=request.form['lid']
    q="select `order`.*,`order details`.*,`product`.* from `order` join `order details` on `order`.`Order_id`=`order details`.`Order_id` join `product` on `product`.`Product_id`=`order details`.`Product_id` where `order`.`U_id`=%s and `status`='cart'"
    res=selectall2(q,lid)
    print(res)
    q="select * from `order` where `U_id`=%s and `status`='cart'"
    res1=selectone(q,lid)
    print(res1)
    if res1 is None:
        return jsonify({"task":"empty"})
    else:
        oid=res1['Order_id']
        tt=str(res1['Total'])
        return jsonify(data=res,data1=oid,total=tt)

@app.route('/user_viewproductdetails',methods=['post'])
def user_viewproductdetails():
    lid = request.form['pid']
    qry = "SELECT * FROM `product` WHERE `Product_id`=%s"
    val=(lid)
    res = selectall2(qry,val)
    print(res)
    return jsonify(res)

@app.route('/user_payment',methods=['post'])
def user_payment():
    return jsonify({"task":"success"})

# @app.route('/add_to_cart',methods=['post'])
# def add_to_cart():
#     print(request.form)
#     pid = request.form['pid']
#     lid = request.form['lid']
#     q = request.form['q']
#     qw="select * from `product` where `Product_id`=%s"
#     reess=selectone(qw,pid)
#     pp=reess['Rate']
#     tt=int(pp)*int(q)
#     print("total",tt)
#     try:
#         res = selectone("SELECT * FROM `order` WHERE `U_id`=%s AND `status`='cart'",(lid))
#         print(res)
#         if res is None:
#             res1 = iud("INSERT INTO `order` (`U_id`,`Date`,`Total`,`status`) VALUES(%s,CURDATE(),%s,'cart')", (lid, tt))
#             iud("INSERT INTO `order details` (`Product_id`,`Order_id`,`Quantity`,`Status`) VALUES(%s,%s,%s,'pending')",
#                 (pid, str(res1), q, 'pending'))
#             return jsonify({"task": "success"})
#         else:
#             iud("INSERT INTO `order details` (`Product_id`,`Order_id`,`Quantity`,`Status`) VALUES(%s,%s,%s,'pending')",
#                 (pid, str(res['Order_id']), q))
#             return jsonify({"task": "success"})
#     except:
#         return jsonify({"task": "success"})

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    pro_id=request.form['pid']
    qty=request.form['q']
    lid=request.form['lid']

    qq="select * from `product` where `Product_id`=%s"
    rees=selectone(qq,pro_id)
    tt=int(rees['Rate'])*int(qty)

    q="SELECT * FROM `order` WHERE `U_id`=%s AND `status`='cart'"
    res=selectone(q,lid)

    if res is None:
        qry="INSERT INTO `order` (`U_id`,`Date`,`Total`,`status`) VALUES(%s,CURDATE(),%s,'cart')"
        val=(lid,tt)
        id=iud(qry,val)
        qry1="INSERT INTO `order details` (`Product_id`,`Order_id`,`Quantity`) VALUES(%s,%s,%s)"
        va=(pro_id,str(id),qty)
        iud(qry1,va)
        return jsonify({"task":"success"})
    else:
        total=int(res['Total'])+int(tt)
        qry = "UPDATE `order` SET `Total`=%s WHERE `Order_id`=%s"
        val = (total, str(res['Order_id']))
        id = iud(qry, val)

        qry1="SELECT * FROM `order details` WHERE `Product_id`=%s AND `Order_id`=%s"
        res12=selectone(qry1,(pro_id,str(res['Order_id'])))
        print(res12)
        if res12 is None:
            qry1 = "insert into `order details` values (null,%s,%s,%s)"
            va = ( pro_id,str(res['Order_id']), qty)
            iud(qry1, va)
        else:
            qry1 = "UPDATE `order details` SET `Quantity`=%s WHERE `Order details_id`=%s"
            quty=int(res12['Quantity'])+int(qty)
            va = (quty,str(res12['Order details_id']))
            iud(qry1, va)
        return jsonify({"task": "success"})



@app.route('/image', methods=['post'])
def image():
            print(request.files)
            imag = request.files['file']
            imag.save(r"F:\crop_predictionweb\src\static\1.jpg")
            # imag.save('static/1.jpg')
            image=secure_filename(imag.filename)
            # path1=r"C:\Users\REGIONAL\Downloads\Crop_Disease (1)\Crop_Disease\src\static\qq.jpg"
            imag.save(os.path.join("static\crop",image))
            resp = predictld(r"F:\crop_predictionweb\src\static\1.jpg")
            print(resp)
            if resp==[0]:
                des="Bacterial leaf blight"
            elif resp==[1]:
                des="Brown spot"
            elif resp == [2]:
                des="Leaf smut"
            else:
                des="Normal Leaf"
            return jsonify(task='success',des=des,img=image)

@app.route('/nutri', methods=['post'])
def nutri():
            print(request.files)
            imag = request.files['file']
            imag.save(r"F:\crop_predictionweb\src\static\1.jpg")
            # imag.save('static/1.jpg')
            image=secure_filename(imag.filename)
            # path1=r"C:\Users\REGIONAL\Downloads\Crop_Disease (1)\Crop_Disease\src\static\qq.jpg"
            imag.save(os.path.join("static\crop",image))
            resp = predictld(r"F:\crop_predictionweb\src\static\1.jpg")
            print(resp)
            if resp==[0]:
                des="Nitrogen"
            elif resp==[1]:
                des="Phosphorus"
            else:
                des="Potassium"
            q="SELECT fertilizer FROM `fertilizer_rec` WHERE `reason`=%s"
            res=selectall2(q,des)
            print(res)
            f=[]
            for i in res:
                f.append(i['fertilizer'])
            f=', '.join(f)
            print(f)
            return jsonify(task='success',des=des,img=image,rec=f)

@app.route('/crop_predict1', methods=['POST'])
def crop_predict():
    print(request.form)
    n = request.form['n']
    p = request.form['p']
    k = request.form['k']
    temperature = request.form['temp']
    humidity = request.form['hum']
    ph = request.form['ph']
    rain = request.form['rain']
    res = random_forest(n,p,k,temperature,humidity,ph,rain)
    print("qwer",res)
    return jsonify({"task":"success","result":res[0]})

@app.route('/finalpay', methods=['POST'])
def finalpay():
    print(request.form)
    oid=request.form['oid']
    q="update `order` set `status`='paid' where `Order_id`=%s"
    iud(q,oid)
    return jsonify({"task":"success"})

@app.route('/usr_view_crop', methods=['POST'])
def usr_view_crop():
    q="SELECT * FROM `crop`"
    res=selectall(q)
    print(res)
    return jsonify(res)


app.run(host='0.0.0.0',port='5000')


