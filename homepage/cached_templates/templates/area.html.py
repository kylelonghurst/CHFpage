# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423346546.975024
_enable_loop = True
_template_filename = '/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/area.html'
_template_uri = 'area.html'
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
        areas = context.get('areas', UNDEFINED)
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
        areas = context.get('areas', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      <h3>This is the Area Page</h3>\n      <h4>Area Page</h4>\n    </div>\n\n    <div class="text-right">\n    \t<a href="/homepage/area.create/" class="btn btn-warning">Create New Area</a>\n    </div>\n    <table id="areas_table" class="table table-striped table-bordered">\n    \t<tr>\n    \t\t<th>ID</th>\n    \t\t<th>Name</th>\n    \t\t<th>Description</th>\n    \t\t<th>Place Number</th>\n            <th>Actions</th>\n')
        for area in areas:
            __M_writer('\t    \t<tr>\n\t    \t\t<td>')
            __M_writer(str( area.id ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( area.name ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( area.description ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( area.place_number ))
            __M_writer('</td>\n\t    \t\t<td>\n\t    \t\t\t<a href="/homepage/area.edit/')
            __M_writer(str( area.id ))
            __M_writer('/" class="btn btn-xs btn-primary">edit</a>\n\t    \t\t</td>\n\t    \t</tr>\n')
        __M_writer('    </table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "area.html", "line_map": {"64": 26, "65": 30, "35": 1, "71": 65, "45": 3, "27": 0, "52": 3, "53": 19, "54": 20, "55": 21, "56": 21, "57": 22, "58": 22, "59": 23, "60": 23, "61": 24, "62": 24, "63": 26}, "filename": "/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/area.html"}
__M_END_METADATA
"""
