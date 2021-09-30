from app import app
from flask import render_template
# contendra todas nuestra vistas


@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")


@app.route("/admin/profile")
def admin_profile():
    return render_template("admin/adm_Profile.html")
