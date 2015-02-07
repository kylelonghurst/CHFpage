# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423279021.381326
_enable_loop = True
_template_filename = '/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/users.html'
_template_uri = 'users.html'
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
        users = context.get('users', UNDEFINED)
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
        users = context.get('users', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    <div class="content">\n      <h3>This is the Users Page</h3>\n      <h4>Users Page</h4>\n    </div>\n\n    <div class="text-right">\n    \t<a href="/homepage/users.create/" class="btn btn-warning">Create New User</a>\n    </div>\n    <table id="users_table" class="table table-striped table-bordered">\n    \t<tr>\n    \t\t<th>ID</th>\n    \t\t<th>Username</th>\n    \t\t<th>First Name</th>\n    \t\t<th>Last Name</th>\n    \t\t<th>Email</th>\n    \t\t<th>Actions</th>\n')
        for user in users:
            __M_writer('\t    \t<tr>\n\t    \t\t<td>')
            __M_writer(str( user.id ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( user.username ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( user.first_name ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( user.last_name ))
            __M_writer('</td>\n\t    \t\t<td>')
            __M_writer(str( user.email ))
            __M_writer('</td>\n\t    \t\t<td>\n\t    \t\t\t<a href="/homepage/users.edit/')
            __M_writer(str( user.id ))
            __M_writer('/" class="btn btn-xs btn-primary">edit</a>\n\t    \t\t</td>\n\t    \t</tr>\n')
        __M_writer('    </table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "users.html", "source_encoding": "ascii", "filename": "/Users/kylelonghurst/Dropbox/Development/Python/test_dmp/homepage/templates/users.html", "line_map": {"64": 26, "65": 28, "66": 28, "35": 1, "73": 67, "45": 3, "27": 0, "67": 32, "52": 3, "53": 20, "54": 21, "55": 22, "56": 22, "57": 23, "58": 23, "59": 24, "60": 24, "61": 25, "62": 25, "63": 26}}
__M_END_METADATA
"""
