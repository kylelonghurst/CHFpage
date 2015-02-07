# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423342182.484568
_enable_loop = True
_template_filename = '/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'footer', 'content']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        def footer():
            return render_footer(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html lang="en">\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>Colonial Heritage Foundation</title>\n\n    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1">\n    \n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n   <!-- \n    <script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n   -->\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n    <link rel="icon" type="image/x-icon" href="/static/homepage/media/faviconred-02.ico" />\n  \n  </head>\n  <body>\n  \n    <header>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n    </header>\n\n\n  <div id="wrap">\n    <div id="main" class="container clear-top">\n\n    <div class="col-md-10 center">\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('  \n    </div>\n  </div>\n\n  </div>\n\n  <footer class="footer">\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'footer'):
            context['self'].footer(**pageargs)
        

        __M_writer('\n  </footer>\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\n  \n  </body>\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n        <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n  \n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" rel="home" href="/homepage/index/"><img id="logo" src="/static/homepage/media/CHFlogo.png" /></a>\n          </div>\n  \n  <div class="collapse navbar-collapse">\n    \n    <ul class="nav navbar-nav">\n        <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">CRUD Pages<b class="caret"></b></a>\n              <ul class="dropdown-menu">\n                <li class="divider"></li>\n                <li><a href="/homepage/venue/">Venues</a></li>\n                <li><a href="/homepage/photo/">Photographs</a></li>\n                <li><a href="/homepage/inventory/">Inventory</a></li>\n                <li><a href="/homepage/saleitem/">Sale Item</a></li>\n                <li><a href="/homepage/area/">Area</a></li>\n              </ul>\n            </li>\n      <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Sales Catalog<b class="caret"></b></a>\n              <ul class="dropdown-menu">\n                <li class="divider"></li>\n                <li><a href="#">Artisan Item</a></li>\n                <li><a href="#">Made-To-Order Item</a></li>\n                <li><a href="#">Mass-Produced Item</a></li>\n              </ul>\n            </li>\n      <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Rentals <b class="caret"></b></a>\n              <ul class="dropdown-menu">\n                <li><a href="#">Wardrobe Item</a></li>\n                <li><a href="#">Other Items</a></li>\n                <li class="divider"></li>\n            <!--\n                <li><a href="#">Separated link</a></li>\n                <li class="divider"></li>\n                <li><a href="#">One more separated link</a></li>\n            -->\n              </ul>\n            </li>\n    </ul>\n  <!--\n    <button type="button" class="btn btn-default navbar-btn">Button</button>\n  -->\n          <!-- <div class="col-sm-4 col-md-4 pull-right">\n           <div class="navbar-text"> -->\n        <ul class="nav navbar-nav pull-right">\n            <li><a href="/homepage/users/">Users</a></li>\n              <form class="navbar-form navbar-left" role="search">\n                <div class="input-group">\n                  <input type="text" class="form-control" placeholder="Search" name="srch-term" id="srch-term">\n                  <div class="input-group-btn">\n                    <button class="btn btn-default" type="submit"><i class="glyphicon glyphicon-search"></i></button>\n                  </div>\n                </div>\n              </form>\n')
        if request.user.is_authenticated():
            __M_writer('              <li class="dropdown">\n                <a href="#" class="dropdown-toggle" data-toggle="dropdown">My Account</a>\n                  <ul class="dropdown-menu" role="menu">\n                    <li><a href="/homepage/login.logout_view/">Logout</a></li>\n                  </ul>\n              </li>\n')
        else:
            __M_writer('              <li><a href="/homepage/login/">Login</a></li>\n')
        __M_writer('        </ul>\n\n    \n          </div>\n        </div>\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n        Site content goes here in sub-templates.\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 34, "72": 34, "73": 99, "74": 100, "75": 106, "76": 107, "77": 109, "16": 4, "18": 0, "83": 131, "89": 131, "101": 122, "31": 2, "32": 4, "33": 5, "37": 5, "38": 17, "39": 26, "40": 26, "41": 26, "95": 122, "107": 101, "46": 114, "51": 124, "56": 133, "57": 137, "58": 137, "59": 137}, "filename": "/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/base.htm", "uri": "base.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
