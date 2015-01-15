# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421303596.288976
_enable_loop = True
_template_filename = '/Users/kylelonghurst/test_dmp/homepage/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['header', 'content', 'sidebar', 'footer']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def header():
            return render_header(context._locals(__M_locals))
        def sidebar():
            return render_sidebar(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def footer():
            return render_footer(context._locals(__M_locals))
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\n\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    \n    <title>Colonial Heritage Foundation</title>\n    \n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>\n   <!-- \n    <script src="//code.jquery.com/jquery-1.11.2.min.js"></script>\n    <script src="//code.jquery.com/jquery-migrate-1.2.1.min.js"></script>\n   -->\n  \n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\n\n    <link rel="icon" type="image/x-icon" href="/static/homepage/media/faviconred-02.ico" />\n  \n  </head>\n  <body>\n  \n    <header>\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'header'):
            context['self'].header(**pageargs)
        

        __M_writer('\n    </header>\n\n\n  <div id="wrap">\n    <div id="main" class="container clear-top">\n\n    <div class="col-md-2 left-menu">\n      ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sidebar'):
            context['self'].sidebar(**pageargs)
        

        __M_writer('\n    </div>\n\n    <div class="col-md-10 center">\n      ')
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
        __M_writer = context.writer()
        __M_writer('\n        <img src="/static/homepage/media/CHFlogo.png" />\n      ')
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


"""
__M_BEGIN_METADATA
{"uri": "base.htm", "line_map": {"64": 70, "65": 70, "66": 70, "72": 32, "78": 32, "16": 4, "18": 0, "84": 55, "90": 55, "96": 42, "33": 2, "34": 4, "35": 5, "102": 42, "39": 5, "40": 15, "41": 24, "42": 24, "43": 24, "108": 64, "48": 34, "114": 64, "53": 51, "120": 114, "58": 57, "63": 66}, "filename": "/Users/kylelonghurst/test_dmp/homepage/templates/base.htm", "source_encoding": "ascii"}
__M_END_METADATA
"""
