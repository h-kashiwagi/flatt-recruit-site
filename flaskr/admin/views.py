from flask import Blueprint, request, render_template, redirect, url_for
from flask_login import login_user, login_required, logout_user
from flaskr.admin.forms import LoginForm, RegisterForm
from flaskr.models.admin import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

engine = create_engine('sqlite:///data.sqlite')
# initファイルの設定でこのBlueprintを登録している
# url_prefixを空にすることでIP：ポートのみ
# 第一引数はBlueprintの名前
# url_prefix='admin'→URL先頭に/admin/
# bp = Blueprint('app', __name__, url_prefix='admin')
bp = Blueprint('admin', __name__, template_folder="templates", static_folder="satic", url_prefix='admin')

@bp.route('/')
def home():
    return render_template('admin/home.html')

# ログインしていないと実行されない(login_userが実行されていないと)
# ログインしていない場合はlogin関数(admin.login)に飛ばされる(login_requiredの機能)
@bp.route('/welcom')
@login_required
def welcome():
    return render_template('admin/welcome.html')

@bp.route('/logout')
@login_required
def logout():
    # セッション削除
    logout_user()
    return redirect(url_for('admin.home'))

@bp.route('/login', methods=['GET', 'POST'])
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
                next = url_for('admin.welcome')
            return redirect(next)
    return render_template('admin/login.html', form=form)

@bp.route('/register', methods=['GET', 'POST'])
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
        # user.add_user()
        Session = sessionmaker(bind=engine)
        ses = Session()
        ses.add(user)
        ses.commit()
        ses.close()
        return redirect(url_for('admin.login'))
    return render_template('admin/register.html', form=form)

@bp.route('/user')
@login_required
def user():
    return render_template('admin/user.html')

