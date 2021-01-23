# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lifelineamb"
app_title = "LifeLine Ambulance"
app_publisher = "4C Solutions"
app_description = "Website for LifeLine Ambulance"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "4csolutions.in"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lifelineamb/css/lifelineamb.css"
# app_include_js = "/assets/lifelineamb/js/lifelineamb.js"

# include js, css files in header of web template
# web_include_css = "/assets/lifelineamb/css/lifelineamb.css"
# web_include_js = "/assets/lifelineamb/js/lifelineamb.js"
web_include_css = [	
    "assets/lifelineamb/vendor/icofont/icofont.min.css",
    "assets/lifelineamb/vendor/boxicons/css/boxicons.min.css",
    "assets/lifelineamb/vendor/remixicon/remixicon.css",
    "assets/lifelineamb/vendor/venobox/venobox.css",
    "assets/lifelineamb/vendor/owl.carousel/assets/owl.carousel.min.css",
    "assets/lifelineamb/vendor/aos/aos.css",
    "assets/lifelineamb/css/style.css"
]

web_include_js = [    
    "assets/lifelineamb/vendor/jquery.easing/jquery.easing.min.js",
    "assets/lifelineamb/vendor/php-email-form/validate.js",
    "assets/lifelineamb/vendor/waypoints/jquery.waypoints.min.js",
    "assets/lifelineamb/vendor/isotope-layout/isotope.pkgd.min.js",
    "assets/lifelineamb/vendor/venobox/venobox.min.js",
    "assets/lifelineamb/vendor/owl.carousel/owl.carousel.min.js",
    "assets/lifelineamb/vendor/aos/aos.js",
    "assets/lifelineamb/js/main.js"
]
# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "lifelineamb/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "index"

default_mail_footer = """
	<span>
		Sent via
		<a class="text-muted" href="https://lifelineambulance.in?source=via_email_footer" target="_blank">
			LifeLine Ambulance
		</a>
	</span>
"""
# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lifelineamb.install.before_install"
# after_install = "lifelineamb.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lifelineamb.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lifelineamb.tasks.all"
# 	],
# 	"daily": [
# 		"lifelineamb.tasks.daily"
# 	],
# 	"hourly": [
# 		"lifelineamb.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lifelineamb.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lifelineamb.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lifelineamb.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lifelineamb.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "lifelineamb.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

