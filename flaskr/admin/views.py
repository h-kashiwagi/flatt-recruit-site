from flask import Blueprint, request, render_template, redirect, url_for, jsonify
from flask_login import login_user, login_required, logout_user
from flaskr.admin.forms import LoginForm, RegisterForm
from flaskr.models.user import User
from flaskr.models.company import Company
from sqlalchemy.orm import sessionmaker
from sqlalchemy.dialects import sqlite # クエリをコンパイル
import logging
import json


 # SQLAlchemy のログを INFO レベルで出力する
logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)

# DEBUG レベル以上のログを出力する
#logging.basicConfig(level=logging.DEBUG)

# userや会社ごとやマスタごとにBlueprintを使い分ける必要がある？登録するときに「admin/userやadmin/company」のように
# adminフォルダ(一つのアプリ)の中にcompanyやuser、industryなどの個別のviewを作ってbrueprintを分けるー全く機能のちがうアプリならadminともちがうフォルダーにする
# 第一引数はBlueprintの名前
# bp = Blueprint('admin', __name__, template_folder='templates', static_url_path='/static', static_folder='static', url_prefix='/admin')
admin = Blueprint('admin', __name__, template_folder='templates', static_folder='static')

@admin.route('/')
def home():
    return render_template('admin/home.html')


@admin.route('/logout')
@login_required
def logout():
    # セッション削除
    logout_user()
    return redirect(url_for('admin.home'))

@admin.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    # GETメソッドのときはLoginFormだけテンプレートと一緒に返す
    if request.method == 'POST' and form.validate():
        user = User.select_by_email(form.email.data)
        # userが存在し、emailから取得したUserのパスワードとクライアントが入力したパスワードが一致するか
        if user and user.validate_password(form.password.data):
            # セッション開始
            login_user(user, remember=True)
            #　次のURL
            next = request.args.get('next')
            if not next:
                # トッページを表示
                next = url_for('admin.top')
            return redirect(next)
    return render_template('admin/login.html', form=form)


@admin.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm(request.form)
    # validate_email()を実行
    if request.method == 'POST' and form.validate():
        user = User(
            email = form.email.data,
            username = form.username.data,
            password = form.password.data
        )
        # インサート
        user.add_user()
        return redirect(url_for('admin.login'))
    return render_template('admin/register.html', form=form)

@admin.route('/user')
@login_required
def user():
    return render_template('admin/user.html')

    
# ログイン後の画面
@admin.route('/company', methods=['GET'])
@login_required
def top():
    search_text = request.args.get('search')
    print(search_text)
    if search_text is None or len(search_text) == 0:
        companydata = Company.getAll()
    else:
        companydata = Company.getSearchData(search_text)    
    res = []
    for item in companydata:
        res.append(item.toDict())
    return render_template('admin/company.html', data=res)

# 登録
@admin.route('/create', methods=['POST'])
@login_required
def create():
    name = request.form.get('name')
    industry_id = request.form.get('industry_id', type=int) # 親をプルダウン
    occupation_id = request.form.get('occupation_id', type=int) # 親をプルダウン
    work_location = request.form.get('work_location')
    job_role = request.form.get('job_role')
    ideal = request.form.get('ideal')
    anuual_income = request.form.get('anuual_income', type=int, default=0) # 検討
    monthly_income = request.form.get('monthly_income', type=int, default=0) # 検討
    url = request.form.get('url')
    capital = request.form.get('capital', type=int, default=0) # 検討
    established = request.form.get('established')
    employees = request.form.get('employees', type=int, default=0) # 検討
    head_office = request.form.get('head_office')
    representative = request.form.get('representative')
    business_content = request.form.get('business_content')
    message = request.form.get('message')
    is_published = request.form.get('is_published', type=bool)
    print(is_published)
    del_flg = request.form.get('del_flg', type=bool)
    print(del_flg)
    companydata = Company(name=name, industry_id=industry_id, occupation_id=occupation_id, work_location=work_location, job_role=job_role, \
                 ideal=ideal, anuual_income=anuual_income, monthly_income=monthly_income, url=url, capital=capital, established=established, \
                 employees=employees, head_office=head_office, representative=representative, business_content=business_content, \
                 message=message, is_published=is_published, del_flg=del_flg)
    companydata.insertData()
    return redirect(url_for('admin.top'))

# def getByList(arr):
#     res = []
#     for item in arr:
#         res.append(item.toDict())
#     return res

@admin.route('/delete', methods=['POST'])
@login_required
def delete_company_ajax():
    keyitems = request.form.get('keys')
    keyitems = json.loads(keyitems)
    # リスト型
    for key in keyitems:
        Company.deleteOneData(key)
    return jsonify({'message':'削除が完了しました。'})


@admin.route('/select/<int:id>', methods=['GET'])
@login_required
def select_company_ajax(id):
    companydata = Company.getByPk(id)
    return jsonify(companydata.toDict())

# 更新
@admin.route('/update/<int:id>', methods=['POST'])
@login_required
def update_company_ajax(id):
    name = request.form.get('name')
    industry_id = request.form.get('industry_id', type=int) # 親をプルダウン
    occupation_id = request.form.get('occupation_id', type=int) # 親をプルダウン
    work_location = request.form.get('work_location')
    job_role = request.form.get('job_role')
    ideal = request.form.get('ideal')
    anuual_income = request.form.get('anuual_income', type=int, default=0) # 検討
    monthly_income = request.form.get('monthly_income', type=int, default=0) # 検討
    url = request.form.get('url')
    capital = request.form.get('capital', type=int, default=0) # 検討
    established = request.form.get('established')
    employees = request.form.get('employees', type=int, default=0) # 検討
    head_office = request.form.get('head_office')
    representative = request.form.get('representative')
    business_content = request.form.get('business_content')
    message = request.form.get('message')
    is_published = request.form.get('is_published', type=bool)
    del_flg = request.form.get('del_flg', type=bool)
    companydata = Company(id=id, name=name, industry_id=industry_id, occupation_id=occupation_id, work_location=work_location, job_role=job_role, \
                 ideal=ideal, anuual_income=anuual_income, monthly_income=monthly_income, url=url, capital=capital, established=established, \
                 employees=employees, head_office=head_office, representative=representative, business_content=business_content, \
                 message=message, is_published=is_published, del_flg=del_flg)
    companydata.updateData()
    return jsonify({'message':'更新が完了しました。'})