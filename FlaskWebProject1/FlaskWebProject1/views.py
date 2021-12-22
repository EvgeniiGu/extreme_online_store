from datetime import datetime
from flask import render_template, request, url_for, redirect, flash
from FlaskWebProject1 import app
import re
from FlaskWebProject1.Admin import Admin
from FlaskWebProject1.User import User
from FlaskWebProject1.Courier import Courier
from FlaskWebProject1.Storekeeper import Storekeeper
from FlaskWebProject1.Dispatcher import Dispatcher

@app.route('/')
@app.route('/Main.html')
def home():
    return render_template('index.html')

@app.route('/admin.html', methods=['POST', 'GET'])
def admin():
    admin_ = Admin()
    list_employees_ = admin_.get_list_employees()
    print(list_employees_)
    goods_list_ = admin_.get_list_goods()
    #print(goods_list_)
    ffrrr=['a1','a2','a3','a4','a5']
    test = dict(somethingI = ffrrr,somethingJ = [1,2,3,4,5], iter=len(ffrrr))
    if request.method == 'POST':
        text = list()
        #name_index = []
        iter = 0
        print(1 if re.fullmatch(r'[А-Я][а-я]+$', "Залунин") else 0)
        for i in list_employees_["iter_list_employees_"]:
            form_get = request.form.get(str(i))
            if iter == 0 or iter == 1:
                if re.fullmatch(r'[А-Я][а-я]+$', form_get):
                    text.append(form_get)
                else:
                    return render_template('admin.html', error=error)
                iter += 1
            elif iter == 6:
                iter = 1
                if re.fullmatch(r'[А-Я][а-я]+$', form_get):
                    text.append(form_get)
                else:
                    pass
            else:
                text.append(form_get)
                iter += 1
        print(text)
        admin_.save_new_list_employees(text)
        dict_text = {"iter_list_employees_": list_employees_["iter_list_employees_"], "workers": text}
        return render_template('admin.html',**dict_text, **goods_list_)
    return render_template('admin.html', **list_employees_, **goods_list_)

@app.route('/Sign-in.html', methods=['POST', 'GET'])
def sign_in():
    if request.method == 'POST':
        login = request.form.get('text')  # запрос к данным формы
        password = request.form.get('text-1')
        print("login="+login, "password="+password)
        user = User()
        position = user.recognize(login, password)
        print(position)
        if position != -1:
            if position == "Admin":
                return redirect("/admin.html")
            elif position == user.position_[0]:
                return redirect('/Courier_select_set.html')
            elif position == user.position_[1]:
                return redirect('/Dispatcher.html')
            elif position == user.position_[2]:
                return redirect('/Storekeeper.html')
        else:
            return render_template('Sign-in.html')
    else:
        return render_template('Sign-in.html')

@app.route('/About-us.html')
def abotus():
    return render_template('About-us.html')

@app.route('/Contacts.html')
def contacts():
    return render_template('Contacts.html')

@app.route('/Courier_select_set.html', methods=['POST', 'GET'])
def courier_select_set():
    courier = Courier()
    return render_template('Courier_select_set.html')

@app.route('/Courier_order.html', methods=['POST', 'GET'])
def courier_order():
    return render_template('Courier_order.html')

@app.route('/Dispatcher.html', methods=['POST', 'GET'])
def dispatcher():
    dispatcher = Dispatcher()
    return render_template('Dispatcher.html')

@app.route('/Dispatcher_set_create.html', methods=['POST', 'GET'])
def dispatcher_set_create():
    return render_template('Dispatcher_set_create.html')

@app.route('/Storekeeper.html', methods=['POST', 'GET'])
def storekeeper():
    storekeeper = Storekeeper()
    return render_template('Storekeeper.html')
