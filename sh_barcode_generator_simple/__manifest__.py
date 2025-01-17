# -*- coding: utf-8 -*-
{
    "name": "Product Barcode Generator",
    "author": "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "version": "0.0.1",
    "category": "Sales",
    "summary": "Default Make Barcode Module New Product Barcode Generate App Existing Product Barcode Generate Application Existing Multi Product Barcode Create Custom Product Barcode Generator Odoo Automatic Generate Product Barcode Odoo Auto Generate New Product Barcode Automatic Generate Existing Product Barcode Auto Create Existing Multi Product Barcode Generator Product Multi Barcode for Product multiple Barcode for Product barcode Search product based on barcode Product barcode generator Product different barcode Product many barcode Product multi barcode for sale multi barcode Create multiple Barcode for product Generate automatic barcode for products Generate auto barcode for product Auto ean13 barcode for product Automatic barcode generation Auto barcode generation Automatic ean13 barcode generation Auto serial Automatic Auto Generate Product Barcode Generator Barcode product ean13 Barcode product auto Barcode ean13",
    "description": """
    Currently in odoo barcode number not auto-generated in the product, our module help to the generated barcode for the product. You can also create/update mass product barcodes. you can also choose different barcode types.""",
    "depends": [
        "product",
        "base_setup",
        "sale_management",
    ],
    "images": [
        "static/description/background.jpg",
    ],
    "data": [
        "security/sh_barcode_generator_groups.xml",
        "security/ir.model.access.csv",
        "views/sh_generate_product_barcode_views.xml",
        "views/product_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
    "license": "OPL-1",
    "auto_install": False,
    "application": True,
    "price": 12,
    "currency": "EUR",
}
