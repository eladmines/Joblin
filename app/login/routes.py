
from flask import Blueprint, render_template,request, jsonify
from app.login.actions import checkLoginDetails

login_bp = Blueprint("login_bp", __name__ , template_folder='login')

@login_bp.route("/")
def index():
    return render_template('login.html') 

@login_bp.route("/", methods=["POST"])
def handle_post_request():
    data = request.get_json()
    loginDetails=checkLoginDetails(data)
    return jsonify(loginDetails)

