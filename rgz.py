from flask import Blueprint, redirect, url_for, render_template, Blueprint, request, session
from db import db

from db.models import users, articles
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, login_required, current_user, logout_user

rgz = Blueprint('laba6', __name__)