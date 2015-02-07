# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423340403.316577
_enable_loop = True
_template_filename = '/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/venue.html'
_template_uri = 'venue.html'
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
        venues = context.get('venues', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        venues = context.get('venues', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      <h3>This is the Venue Page</h3>\n      <h4>Venue Page</h4>\n    </div>\n\n    <div class="text-right">\n    \t<a href="/homepage/venue.create/" class="btn btn-warning">Create New Venue</a>\n    </div>\n    <table id="venues_table" class="table table-striped table-bordered">\n    \t<tr>\n    \t\t<th>ID</th>\n    \t\t<th>Name</th>\n    \t\t<th>Address</th>\n    \t\t<th>City</th>\n    \t\t<th>State</th>\n    \t\t<th>ZIP</th>\n            <th>Email</th>\n            <th>Actions</th>\n')
        for venue in venues:
            __M_writer('\t    \t<tr>\n\t    \t\t<td>')
            __M_writer(str( venue.id ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( venue.name ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( venue.address ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( venue.city ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( venue.state ))
            __M_writer('</td>\n                <td>')
            __M_writer(str( venue.zip ))
            __M_writer('</td>\n                <td>')
            __M_writer(str( venue.email ))
            __M_writer('</td>\n\t    \t\t<td>\n\t    \t\t\t<a href="/homepage/venue.edit/')
            __M_writer(str( venue.id ))
            __M_writer('/" class="btn btn-xs btn-primary">edit</a>\n\t    \t\t</td>\n\t    \t</tr>\n')
        __M_writer('    </table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/venue.html", "line_map": {"64": 28, "65": 29, "66": 29, "67": 30, "68": 30, "69": 32, "70": 32, "71": 36, "77": 71, "27": 0, "35": 1, "45": 3, "52": 3, "53": 22, "54": 23, "55": 24, "56": 24, "57": 25, "58": 25, "59": 26, "60": 26, "61": 27, "62": 27, "63": 28}, "uri": "venue.html"}
__M_END_METADATA
"""
