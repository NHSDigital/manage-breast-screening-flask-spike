import functools
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

bp = Blueprint('clinics', __name__, url_prefix='/clinics')

@bp.route("/")
def clinics():
    return render_template("clinics.html", filteredClinicCounts={
        'today': 0,
        'upcoming': 0,
        'completed': 0,
        'all': 0
    })