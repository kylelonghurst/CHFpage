# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1421284014.038423
_enable_loop = True
_template_filename = '/Users/kylelonghurst/test_dmp/homepage/templates/index.html'
_template_uri = 'index.html'
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
        __M_writer('\n    <div class="content">\n      <h3>Congratulations -- you\'ve successfully created a new django-mako-plus app!</h3>\n      <h4>Next Up: Go through the django-mako-plus tutorial and add Javascript, CSS, and urlparams to this page.\n      <span class="label label-warning">Warning</span></h4>\n      <br>\n      <button type="button" class="btn btn-primary">Primary Button\n      \t<span class="badge">1</span>\n      </button>\n      <button type="button" class="btn btn-success">Success Button\n      \t<span class="badge">2</span>\n      </button>\n    </div>\n\n<!--\n')
        for i in range(50):
            if i % 9 == 0:
                __M_writer('    \t\t<p>')
                __M_writer(str(i))
                __M_writer(': Welcome to my site</p>\n')
        __M_writer('-->\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 58, "35": 1, "52": 3, "53": 18, "54": 19, "55": 20, "56": 20, "57": 20, "58": 23, "27": 0, "45": 3}, "filename": "/Users/kylelonghurst/test_dmp/homepage/templates/index.html", "source_encoding": "ascii", "uri": "index.html"}
__M_END_METADATA
"""
