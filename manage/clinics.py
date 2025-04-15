from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from manage.models import Clinic

bp = Blueprint('clinics', __name__, url_prefix='/clinics')

@bp.route("/")
def clinics():
    filtered_clinics = Clinic.query.all()
    return render_template("clinics.html", filteredClinicCounts={
        'today': 0,
        'upcoming': 0,
        'completed': 0,
        'all': 0
    }, filteredClinics=filtered_clinics)