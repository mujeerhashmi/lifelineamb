from __future__ import unicode_literals

import frappe
from frappe.utils import now
from frappe import _

no_cache = 1
no_sitemap = 1

def get_context(context):
	gallery_images = frappe.get_all('Gallery Image', fields=['title','category', 'image'], order_by="title")
	categories = frappe.get_all('Gallery Image', fields='category', group_by='category')

	out = {
		"gallery_images": gallery_images,
		"categories": categories
	}
	
	return out

max_communications_per_hour = 1000

@frappe.whitelist(allow_guest=True)
def send_message(subject="Website Query", message="", sender=""):
	if not message:
		frappe.response["message"] = 'Please write something'
		return

	if not sender:
		frappe.response["message"] = 'Email Address Required'
		return

	# guest method, cap max writes per hour
	if frappe.db.sql("""select count(*) from `tabCommunication`
		where `sent_or_received`="Received"
		and TIMEDIFF(%s, modified) < '01:00:00'""", now())[0][0] > max_communications_per_hour:
		frappe.response["message"] = "Sorry: we believe we have received an unreasonably high number of requests of this kind. Please try later"
		return

	# send email
	forward_to_email = frappe.db.get_value("Contact Us Settings", None, "forward_to_email")
	if forward_to_email:
		frappe.sendmail(recipients=forward_to_email, sender=sender, content=message, subject=subject)


	# add to to-do ?
	frappe.get_doc(dict(
		doctype = 'Communication',
		sender=sender,
		subject= _('New Message from Website Contact Page'),
		sent_or_received='Received',
		content=message,
		status='Open',
	)).insert(ignore_permissions=True)

	return "okay"
