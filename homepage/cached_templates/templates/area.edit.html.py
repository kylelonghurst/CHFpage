# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423346552.492217
_enable_loop = True
_template_filename = '/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/area.edit.html'
_template_uri = 'area.edit.html'
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
        form = context.get('form', UNDEFINED)
        area = context.get('area', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        area = context.get('area', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      <h3>This is the Area Page</h3>\n      <h4>Edit Area Page</h4>\n    </div>\n    \n    <form method=\'POST\'>\n        <table>\n            ')
        __M_writer(str( form ))
        __M_writer('\n        </table>\n        <button type="submit" class="btn btn-primary">Submit</button>\n        <a href="/homepage/area.delete/')
        __M_writer(str( area.id ))
        __M_writer('/" class="btn btn-danger">Delete Account</a>\n    </form>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "area.edit.html", "line_map": {"64": 58, "36": 1, "54": 3, "55": 11, "56": 11, "57": 14, "58": 14, "27": 0, "46": 3}, "filename": "/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/area.edit.html"}
__M_END_METADATA
"""
