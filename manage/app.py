from flask import Flask, render_template, redirect
import manage.jinja_filters as jinja_filters

app = Flask(__name__)

# Register Jinja filters
app.jinja_env.filters['noWrap'] = jinja_filters.no_wrap
app.jinja_env.filters['asHint'] = jinja_filters.as_hint
app.jinja_env.filters['formatWords'] = jinja_filters.format_words
app.jinja_env.filters['formatDate'] = jinja_filters.format_date
app.jinja_env.filters['formatDateTime'] = jinja_filters.format_date_time
app.jinja_env.filters['formatTime'] = jinja_filters.format_time
app.jinja_env.filters['formatTimeRange'] = jinja_filters.format_time_range

@app.route("/")
def index():
    return redirect("/clinics")

@app.route("/clinics")
def clinics():
    return render_template("clinics.html", filteredClinicCounts={
        'today': 0,
        'upcoming': 0,
        'completed': 0,
        'all': 0
    })