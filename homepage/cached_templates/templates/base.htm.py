# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423255511.220462
_enable_loop = True
_template_filename = '/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content', 'footer', 'header', 'sidebar']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def footer():
            return render_footer(context._locals(__M_locals))
        def header():
            return render_header(context._locals(__M_locals))
        def sidebar():
            return render_sidebar(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        self = context.get('self', UNDEFINED)
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
        

        __M_writer('\n    </header>\n\n\n  <div id="wrap">\n    <div id="main" class="container clear-top">\n\'\'\'\n    <div class="col-md-2 left-menu">\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sidebar'):
            context['self'].sidebar(**pageargs)
        

        __M_writer('\n    </div>\n\'\'\'\n    <div class="col-md-10 center">\n      ')
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


def render_footer(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def footer():
            return render_footer(context)
        __M_writer = context.writer()
        __M_writer('\n        This is the bottom\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def header():
            return render_header(context)
        __M_writer = context.writer()
        __M_writer('\n        <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">\n  \n          <div class="navbar-header">\n            <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n            <span class="sr-only">Toggle navigation</span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            <span class="icon-bar"></span>\n            </button>\n            <a class="navbar-brand" rel="home" href="#"><img id="logo" src="/static/homepage/media/CHFlogo.png" /></a>\n          </div>\n  \n  <div class="collapse navbar-collapse">\n    \n    <ul class="nav navbar-nav">\n      <li><a href="#">Events</a></li>\n      <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Sales Catalog<b class="caret"></b></a>\n              <ul class="dropdown-menu">\n                <li class="divider"></li>\n                <li><a href="#">Artisan Item</a></li>\n                <li><a href="#">Made-To-Order Item</a></li>\n                <li><a href="#">Mass-Produced Item</a></li>\n              </ul>\n            </li>\n      <li class="dropdown">\n              <a href="#" class="dropdown-toggle" data-toggle="dropdown">Rentals <b class="caret"></b></a>\n              <ul class="dropdown-menu">\n                <li><a href="#">Wardrobe Item</a></li>\n                <li><a href="#">Other Items</a></li>\n                <li class="divider"></li>\n            <!--\n                <li><a href="#">Separated link</a></li>\n                <li class="divider"></li>\n                <li><a href="#">One more separated link</a></li>\n            -->\n              </ul>\n            </li>\n    </ul>\n  <!--\n    <button type="button" class="btn btn-default navbar-btn">Button</button>\n  -->\n          <div class="col-sm-4 col-md-4 pull-right">\n              <div class="navbar-text"><a href="#">My Account</a></div>\n          <form class="navbar-form" role="search">\n          <div class="input-group">\n            <input type="text" class="form-control" placeholder="Search" name="srch-term" id="srch-term">\n            <div class="input-group-btn">\n              <button class="btn btn-default" type="submit"><i class="glyphicon glyphicon-search"></i></button>\n            </div>\n          </div>\n          </form>\n          </div>\n    \n          </div>\n        </div>\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sidebar(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def sidebar():
            return render_sidebar(context)
        __M_writer = context.writer()
        __M_writer('\n        <h3>Navigation </h3>\n        <ul class="nav nav-pills nav-stacked">\n          <li role="presentation"><a href="index">\n            <span class="glyphicon glyphicon-home" aria-hidden="true"></span>Home</a></li>\n          <li role="presentation"><a href="about">About</a></li>\n          <li role="presentation"><a href="contact">Contact</a></li>\n          <li role="presentation"><a href="terms">Terms</a></li>\n        </ul>\n      ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 127, "65": 127, "66": 127, "72": 112, "78": 112, "16": 4, "18": 0, "84": 121, "90": 121, "96": 34, "33": 2, "34": 4, "35": 5, "102": 34, "39": 5, "40": 17, "41": 26, "42": 26, "43": 26, "108": 99, "48": 91, "114": 99, "53": 108, "120": 114, "58": 114, "63": 123}, "uri": "base.htm", "source_encoding": "ascii", "filename": "/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/base.htm"}
__M_END_METADATA
"""
