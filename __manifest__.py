# STeSI Consulting - Michele Di Croce
# License OPL-1 (https://www.odoo.com/documentation/user/19.0/legal/licenses/licenses.html).
# Portal Product Availability — Cybrosys Technologies adaptation
{
    'name': "Portal Product Availability",
    'version': '19.0.1.0.0',
    'category': 'Sales',
    'summary': "Portal users can check product availability",
    'license': 'OPL-1',
    'author': "STeSI Consulting",
    'website': "https://github.com/ingegniamo/portal_stock_check",
    'depends': ['portal', 'sale_management', 'stock', 'contacts'],
    'data': ['views/portal_inherited.xml'],
    'assets': {
        'web.assets_frontend': [
            'portal_stock_check/static/src/js/search_products.js',
            'portal_stock_check/static/src/xml/product_list.xml'
        ],
    },
}
