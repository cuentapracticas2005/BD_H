from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from wtforms import Form, StringField, PasswordField, validators
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from . import db
from .models import User, RoleEnum


class LoginForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=6, max=128)])


class CreateUserForm(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired(), Length(min=3, max=80)])
    password = PasswordField("Contraseña", validators=[DataRequired(), Length(min=8, max=128)])
    role = StringField("Rol", validators=[DataRequired()])


auth_bp = Blueprint("auth", __name__)


@auth_bp.get("/login")
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for("main.dashboard"))
    form = LoginForm()
    return render_template("auth/login.html", form=form)


@auth_bp.post("/login")
def login_post():
    form = LoginForm()
    if not form.validate_on_submit():
        flash("Credenciales inválidas", "error")
        return redirect(url_for("auth.login_page"))

    user = User.query.filter_by(username=form.username.data).first()
    if not user or not user.check_password(form.password.data):
        flash("Usuario o contraseña incorrectos", "error")
        return redirect(url_for("auth.login_page"))

    if not user.is_active:
        flash("Cuenta deshabilitada", "error")
        return redirect(url_for("auth.login_page"))

    login_user(user)
    return redirect(url_for("main.dashboard"))


@auth_bp.post("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login_page"))


@auth_bp.get("/register")
@login_required
def register_page():
    if not current_user.is_admin:
        flash("Solo administradores", "error")
        return redirect(url_for("main.dashboard"))
    form = CreateUserForm()
    return render_template("auth/register.html", form=form)


@auth_bp.post("/register")
@login_required
def register_post():
    if not current_user.is_admin:
        flash("Solo administradores", "error")
        return redirect(url_for("main.dashboard"))

    form = CreateUserForm()
    if not form.validate_on_submit():
        flash("Datos inválidos", "error")
        return redirect(url_for("auth.register_page"))

    if form.role.data not in (RoleEnum.ADMIN.value, RoleEnum.WORKER.value):
        flash("Rol inválido", "error")
        return redirect(url_for("auth.register_page"))

    if User.query.filter_by(username=form.username.data).first():
        flash("Usuario ya existe", "error")
        return redirect(url_for("auth.register_page"))

    user = User(username=form.username.data, role=RoleEnum(form.role.data))
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash("Usuario creado", "success")
    return redirect(url_for("main.dashboard"))