import frappe

@frappe.whitelist()

def custom_query(doctype, txt, searchfield, start, page_len, filters):
    # console.log("sadfafd")
    # frappe.logger("").debug({"ttt":"ggg"})
    frappe.logger("frappe.web").debug({
        "sdfsd": "####", "filters":filters , "txt":txt, "searchfield": searchfield})

    filtered_list =  frappe.db.sql("""
                select u.name, concat(u.first_name, ' ', u.last_name)
                from tabUser u, `tabHas Role` r
                where u.name = r.parent and r.role = 'Supplier'
                and u.enabled = 1 and u.name like %s
        """, ("%" + txt + "%"))

    # filtered_list=[]
    return filtered_list
