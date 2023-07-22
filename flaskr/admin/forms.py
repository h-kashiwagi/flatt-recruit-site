from wtforms.form import Form
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms import ValidationError
from flaskr.models.user import User

# ログイン画面で利用
class LoginForm(Form):
    email = StringField('メール：', validators=[DataRequired(), Email('メールアドレスが誤っています')])
    password = PasswordField('パスワード：', validators=[DataRequired()])
    submit = SubmitField('ログイン')

# 登録画面で利用
class RegisterForm(Form):
    email = StringField('メール；', validators=[DataRequired(), Email()])
    username = StringField('名前：', validators=[DataRequired()])
    password = PasswordField(
        'パスワード：', validators=[
            DataRequired(), 
            EqualTo('password_confirm', message="パスワードが一致しません"), 
            Length(1, 10, '長さは1文字以上10文字以内です')]
    )
    password_confirm = PasswordField('パスワード確認：', validators=[DataRequired()])
    submit = SubmitField('登録')

    def validate_email(self, field):
        if User.select_by_email(field.data):
            raise ValidationError('このメールアドレスはすでに登録されています。')

