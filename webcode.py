import os
from flask import *
from werkzeug.utils import secure_filename
from src.dbconnectionnew import *
app=Flask(__name__)
app.secret_key="ghjk"


import functools


def login_required(func):
	@functools.wraps(func)
	def secure_function():
		if "lid" not in session:
			return render_template('loginindex.html')
		return func()
	return secure_function




@app.route('/logout')
@login_required
def logout():
	session.clear()
	return redirect('/')


@app.route('/')
def login():
    return render_template('loginindex.html')

@app.route('/login_post',methods=['post'])
def login_post():
    uname=request.form['username']
    psw=request.form['pass']
    q="SELECT * FROM `login` WHERE `username`=%s AND `password`=%s"
    val=(uname,psw)
    res=selectone(q,val)
    if res is None:
        return '''<script>alert("Invalid username or password");window.location='/'</script>'''
    elif res['type']=='admin':
        session['lid'] = res['login_id']
        return'''<script>alert("Admin home");window.location='/adminhome'</script>'''
    elif res['type']=='expert':
        session['lid']=res['login_id']
        return'''<script>alert("expert");window.location='/expert_home'</script>'''
    else:
        return '''<script>alert("Invalid user");window.location='/'</script>'''


#=================================================ADMIN===================================================

@app.route('/adminhome')
@login_required
def adminhome():
    return render_template('admin/index.html')

@app.route('/add_and_manage',methods=['post','get'])
@login_required
def add_and_manage():
    qry="SELECT * FROM `notification`"
    res=selectall(qry)
    return render_template('admin/add & manage notification.html',val=res)





@app.route('/add_crop',methods=['post','get'])
@login_required
def add_crop():
    return render_template('admin/add crop.html')
@app.route('/add_crop1',methods=['post','get'])
@login_required
def add_crop1():
   crop=request.form['textfield']
   description=request.form['textfield2']
   image=request.files['textfield3']
   fname=secure_filename(image.filename)
   image.save(os.path.join('static/crop',fname))

   q = "INSERT INTO `crop` VALUES (NULL,%s,%s,%s)"
   val = (crop,description,fname)
   res = iud(q,val)
   return '''<script>alert("added succesfully");window.location='/manage_crop'</script>'''

@app.route('/edit_crop',methods=['post','get'])
@login_required
def edit_crop():
    id=request.args.get('id')
    session['EC_id']=id
    qry="select * from crop where  `Crop_id`=%s"
    res=selectone(qry,id)
    return render_template('admin/edit crop.html',val=res)

@app.route('/edit_crop1',methods=['post','get'])
@login_required
def edit_crop1():
    try:
       crop=request.form['textfield']
       description=request.form['textfield2']
       image=request.files['textfield3']
       fname=secure_filename(image.filename)
       image.save(os.path.join('static/crop',fname))

       q = "UPDATE `crop` SET `Crop_name`=%s,`Description`=%s,`Image`=%s  WHERE `Crop_id`=%s "
       val = (crop,description,fname,session['EC_id'])
       res = iud(q,val)
       return '''<script>alert("Edited succesfully");window.location='/manage_crop'</script>'''
    except:
        crop = request.form['textfield']
        description = request.form['textfield2']

        q = "UPDATE `crop` SET `Crop_name`=%s,`Description`=%s  WHERE `Crop_id`=%s "
        val = (crop, description, session['EC_id'])
        res = iud(q, val)
        return '''<script>alert("Edited succesfully");window.location='/manage_crop'</script>'''


@app.route('/add_expert',methods=['post','get'])
@login_required
def add_expert():
    return render_template('admin/add expert.html')
@app.route('/add_expert1',methods=['post','get'])
@login_required
def add_expert1():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    email=request.form['textfield6']
    phone=request.form['textfield7']
    username=request.form['textfield8']
    password=request.form['textfield9']

    q="INSERT INTO `login` VALUES (NULL,%s,%s,'expert')"
    val=(username,password)
    res=iud(q,val)

    qry="INSERT INTO `expert` VALUES (NULL,%s,%s,%s,%s,%s,%s,%s,%s)"
    val1=(str(res),fname,lname,place,post,pin,email,phone,)
    iud(qry,val1)
    return '''<script>alert("registered succesfull");window.location='/manage_expert'</script>'''


@app.route('/edit_expert',methods=['post','get'])
@login_required
def edit_expert():
    id=request.args.get('id')
    session['EE_id']=id
    qry="select * from expert where  `E_id`=%s"
    res=selectone(qry,id)
    return render_template('admin/edit expert.html',val=res)


@app.route('/edit_expert1',methods=['post','get'])
@login_required
def edit_expert1():
    fname=request.form['textfield']
    lname=request.form['textfield2']
    place=request.form['textfield3']
    post=request.form['textfield4']
    pin=request.form['textfield5']
    email=request.form['textfield6']
    phone=request.form['textfield7']


    qry="UPDATE `expert` SET `First_name`=%s,`Last_name`=%s,`place`=%s,`post`=%s,`pin`=%s,`email`=%s,`phone`=%s   WHERE `E_id`=%s"
    val1=(fname,lname,place,post,pin,email,phone,session['EE_id'])
    iud(qry,val1)
    return '''<script>alert("registered succesfull");window.location='/manage_expert'</script>'''



@app.route('/delete_expert')
@login_required
def delete_expert():
    id = request.args.get('id')
    qry = "DELETE FROM `expert` WHERE `E_id`=%s"
    iud(qry,id)
    return '''<script>alert("deleted succesfully");window.location='/manage_expert'</script>'''





@app.route('/add_notification',methods=['post','get'])
@login_required
def add_notification():
    return render_template('admin/add notification.html')

@app.route('/delete_notification')
@login_required
def delete_notification():
    id = request.args.get('id')
    qry = "DELETE FROM `notification` WHERE `N_id`=%s"
    iud(qry,id)
    return '''<script>alert("deleted succesfully");window.location='/add_and_manage'</script>'''


@app.route('/add_notification1',methods=['post','get'])
@login_required
def add_notification1():

    notification=request.form['textfield']
    qry="INSERT INTO `notification` VALUES(NULL,%s,CURDATE())"
    val=(notification)
    iud(qry,val)
    return '''<script>alert("Added succesfull");window.location='/add_and_manage'</script>'''




@app.route('/manage_crop')
@login_required
def manage_crop():
    qry="SELECT * FROM `crop`"
    res=selectall(qry)
    return render_template('admin/manage crop.html',val=res)

@app.route('/delete_crop')
@login_required
def delete_crop():
    id = request.args.get('id')
    qry = "DELETE FROM `crop` WHERE `Crop_id`=%s"
    iud(qry,id)
    return '''<script>alert("deleted succesfully");window.location='/manage_crop'</script>'''



@app.route('/manage_expert')
@login_required
def manage_expert():
    qry="SELECT * FROM `expert`"
    res=selectall(qry)
    return render_template('admin/manage expert.html',val=res)



@app.route('/admin_send_reply')
@login_required
def admin_send_reply():
    id = request.args.get('id')
    session['ER_id'] = id

    return render_template('admin/send reply.html')
@app.route('/admin_send_reply1',methods=['post'])
@login_required
def admin_send_reply1():
    reply=request.form['textfield']
    q="UPDATE `complaint` SET `Reply`=%s WHERE `Complaint_id`=%s"
    val=(reply,session['ER_id'])
    iud(q,val)
    return '''<script>alert("reply updated");window.location='/admin_send_reply'</script>'''


@app.route('/verify_farmer')
@login_required
def verify_farmer():
    qry="SELECT `farmer`.* FROM `farmer` JOIN `login` ON `farmer`.`L_id`=`login`.`login_id` WHERE `login`.`type`='pending'"
    res=selectall(qry)
    return render_template('admin/verify farmer.html',val=res)

@app.route('/accept_farmer')
@login_required
def accept_farmer():
    id = request.args.get('id')
    qry = "UPDATE `login` SET `type`='farmer' WHERE `login_id`=%s"
    iud(qry,id)
    return '''<script>alert("accepted succesfully");window.location='/verify_farmer'</script>'''

@app.route('/reject_farmer')
@login_required
def reject_farmer():
    id = request.args.get('id')
    qry = "UPDATE `login` SET `type`='reject' WHERE `login_id`=%s"
    iud(qry,id)
    return '''<script>alert("rejected succesfully");window.location='/verify_farmer'</script>'''

@app.route('/view_complaint_and_send_reply')
@login_required
def view_complaint_and_send_reply():
    qry="select `complaint`.*,`farmer`.* from `complaint` join `farmer` on `complaint`.`L_id`=`farmer`.`L_id` where `complaint`.`Reply`='pending'"
    res=selectall(qry)
    print(res)
    return render_template('admin/view complaint and send reply.html',val=res)

@app.route('/view_registered_user_and_verify')
@login_required
def view_registered_user_and_verify():
    qry="SELECT `user`.* FROM `user` JOIN `login` ON `user`.`L_id`=`login`.`login_id` WHERE `login`.`type`='pending'"
    res=selectall(qry)
    return render_template('admin/view registered user and verify.html',val=res)

@app.route('/accept_user')
@login_required
def accept_user():
    id = request.args.get('id')
    qry = "UPDATE `login` SET `type`='user' WHERE `login_id`=%s"
    iud(qry,id)
    return '''<script>alert("accepted succesfully");window.location='/view_registered_user_and_verify'</script>'''

@app.route('/reject_user')
@login_required
def reject_user():
    id = request.args.get('id')
    qry = "UPDATE `login` SET `type`='reject' WHERE `login_id`=%s"
    iud(qry,id)
    return '''<script>alert("rejected succesfully");window.location='/view_registered_user_and_verify'</script>'''












#================================================EXPERT========================================================

@app.route('/add_fertilizer')
@login_required
def add_fertilizer():
    return render_template('expert/add fertilizer.html')

@app.route('/add_tip')
@login_required
def add_tip():
    return render_template('expert/add tip.html')


@app.route('/expert_home')
@login_required
def expert_home():
    return render_template('expert/expert home.html')

@app.route('/manage_fertilizer')
@login_required
def manage_fertilizer():
    qry = "SELECT * FROM `fertilizer` WHERE `E_id`=%s"
    res = selectall2(qry, session['lid'])
    return render_template('expert/manage fertilizer.html',val=res)

@app.route('/delete_fertilizer')
@login_required
def delete_fertilizer():
    id = request.args.get('id')
    qry = "DELETE FROM `fertilizer` WHERE `Fertilizer_id`=%s"
    iud(qry,id)
    return '''<script>alert("deleted succesfully");window.location='/manage_fertilizer'</script>'''

@app.route('/add_fertilizer1',methods=['post','get'])
@login_required
def add_fertilizer1():

    Fertilizer=request.form['textfield']
    Description=request.form['textfield2']
    Price=request.form['textfield3']
    qry="INSERT INTO `fertilizer` VALUES(NULL,%s,%s,%s,%s)"
    val=(session['lid'],Fertilizer,Description,Price)
    iud(qry,val)
    return '''<script>alert("Added succesfull");window.location='/manage_fertilizer'</script>'''

@app.route('/edit_fertilizer',methods=['post','get'])
@login_required
def edit_fertilizer():
    id=request.args.get('id')
    session['fid']=id
    qry="SELECT * FROM fertilizer WHERE `Fertilizer_id`=%s"
    res=selectone(qry,id)
    return render_template('expert/edit fertilizer.html',val=res)

@app.route('/edit_fertilizer1',methods=['post','get'])
@login_required
def edit_fertilizer1():

    Fertilizer=request.form['textfield']
    Description=request.form['textfield2']
    Price=request.form['textfield3']
    qry="UPDATE `fertilizer` SET `Fertilizer`=%s,`Description`=%s,`Price`=%s WHERE `Fertilizer_id`=%s"
    vall=(Fertilizer,Description,Price,session['fid'])
    iud(qry,vall)
    return '''<script>alert("Updated succesfull");window.location='/manage_fertilizer'</script>'''

@app.route('/manage_tip')
@login_required
def manage_tip():
    qry = "SELECT * FROM `suggestions` WHERE `E_id`=%s"
    res = selectall2(qry,session['lid'])
    return render_template('expert/Manage tip.html',val=res)

@app.route('/delete_tip')
@login_required
def delete_tip():
    id = request.args.get('id')
    qry = "DELETE FROM `suggestions` WHERE `Tip_id`=%s"
    iud(qry,id)
    return '''<script>alert("deleted succesfully");window.location='/manage_tip'</script>'''



@app.route('/add_tip1',methods=['post','get'])
@login_required
def add_tip1():

    tip=request.form['textfield']
    qry="INSERT INTO `suggestions` VALUES(NULL,%s,CURDATE(),%s)"
    val=(tip,session['lid'])
    iud(qry,val)
    return '''<script>alert("Added succesfull");window.location='/manage_tip'</script>'''


@app.route('/expert_send_reply')
@login_required
def expert_send_reply():
    id = request.args.get('id')
    session['lid'] = id

    return render_template('expert/send reply.html')

@app.route('/expert_send_reply1', methods=['post'])
@login_required
def expert_send_reply1():
    reply = request.form['textfield']
    qry = "UPDATE `questions` SET `Reply`=%s WHERE `Doubt_id`=%s"
    val = (reply, session['lid'])
    iud(qry, val)
    return '''<script>alert("reply updated");window.location='/expert_send_reply'</script>'''


@app.route('/view_doubt_and_send_reply')
@login_required
def view_doubt_and_send_reply():
    qry = "SELECT `questions`.*,`farmer`.`First_name`,`Last_name` FROM `questions` JOIN `farmer` ON `farmer`.`L_id`=`questions`.`L_id` WHERE `Reply`='pending' AND `E_id`=%s"
    res = selectall2(qry,session['lid'])
    return render_template('expert/view doubt and send reply.html',val=res)

@app.route('/view_notification')
@login_required
def view_notification():
    qry = "SELECT * FROM `notification`"
    res = selectall(qry)
    return render_template('expert/view notification.html',val=res)







app.run(debug=True,port=5001)


