import frappe
from frappe import _

def get_context(context):

    frappe.logger("frappe.web").debug({
        "fefefed": "####a"})

    current_user = frappe.session.user
    role = frappe.get_roles(frappe.session.user)
    print(role)

    if 'Supplier' not in role:
        frappe.msgprint(_("adfs"))
        return

    u_name = frappe.db.get_value("User", current_user, ["name"])
    context.items =  frappe.get_list("Item",{"supplier":u_name})

    for item in frappe.get_list("Item"):
        name = item.name
        # get detail from db by name(id)
        pass

    context.name = "text from py"
    context.user = current_user
    context.user_name = frappe.db.get_value("User", current_user, ["email"], as_dict=True)


    return context
