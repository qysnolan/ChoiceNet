# from django.forms import forms
#
#
# class BaseForm(forms.BaseForm):
#     error_css_class = "error"
#     required_css_class = "required"
#
#     def as_bootstrap(self):
#         """Returns this form rendered with a Bootstrap feel"""
#         return self._html_output(
#             normal_row=u'<div%(html_class_attr)s>%(label)s %(field)s%(help_text)s</div>',
#             error_row=u'<div class="alert alert-error form-error-list">%s</div>',
#             row_ender='</div>',
#             help_text_html=u' <span class="helptext">%s</span>',
#             errors_on_separate_row=True)
#
#     def __getitem__(self, name):
#         """Returns a BaseField with the given name."""
#         try:
#             field = self.fields[name]
#         except KeyError:
#             raise KeyError('Key %r not found in Form' % name)
#         return BaseField(self, field, name)
#
#
# class Form(BaseForm, forms.Form):
#     pass

