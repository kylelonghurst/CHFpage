# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421252843.699388
_enable_loop = True
_template_filename = '/Users/kylelonghurst/test_dmp/homepage/templates/about.html'
_template_uri = 'about.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        range = context.get('range', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      <h3>Congratulations -- you\'ve successfully created a new django-mako-plus app!</h3>\n      <h4>about page</h4>\n    </div>\n\n')
        for i in range(50):
            if i % 9 == 0:
                __M_writer('    \t\t<p>')
                __M_writer(str(i))
                __M_writer(': Welcome to my site</p>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"35": 1, "52": 3, "53": 9, "54": 10, "55": 11, "56": 11, "57": 11, "27": 0, "45": 3, "63": 57}, "uri": "about.html", "source_encoding": "ascii", "filename": "/Users/kylelonghurst/test_dmp/homepage/templates/about.html"}
__M_END_METADATA
"""
