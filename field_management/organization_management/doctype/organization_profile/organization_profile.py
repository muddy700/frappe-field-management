# Copyright (c) 2021, Mohamed M Mohamed and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class OrganizationProfile(Document):
	def before_save(self):
		org = frappe.get_doc("User", self.organization)
		self.alias = org.username
		self.created_by = org.owner