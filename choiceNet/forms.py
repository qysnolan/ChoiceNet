from django.forms import forms
from django.forms import models as model_forms


class BaseForm(forms.BaseForm):
    error_css_class = "error"
    required_css_class = "required"

    def as_bootstrap(self):
        """Returns this form rendered with a Bootstrap feel"""
        return self._html_output(
            normal_row=u'<div%(html_class_attr)s>%(label)s %(field)s%(help_text)s</div>',
            error_row=u'<div class="alert alert-error form-error-list">%s</div>',
            row_ender='</div>',
            help_text_html=u' <span class="helptext">%s</span>',
            errors_on_separate_row=True)

    def __getitem__(self, name):
        """Returns a BaseField with the given name."""
        try:
            field = self.fields[name]
        except KeyError:
            raise KeyError('Key %r not found in Form' % name)
        return BaseField(self, field, name)


class Form(BaseForm, forms.Form):
    pass


class ModelForm(BaseForm, model_forms.ModelForm):
    pass


class BaseField(forms.BoundField):
    def label_tag(self, contents=None, attrs=None):
        """
        Wraps the given contents in a <label>, if the field has an ID attribute.
        Does not HTML-escape the contents. If contents aren't given, uses the
        field's HTML-escaped label.

        If attrs are given, they're used as HTML attributes on the <label> tag.
        """
        contents = contents or conditional_escape(self.label)
        widget = self.field.widget
        id_ = widget.attrs.get('id') or self.auto_id

        if id_:

            attrs = attrs and flatatt(attrs) or ''

            # Display checkbox labels to the right of checkboxes

            if isinstance(widget, django_widgets.CheckboxInput):
                contents = u'<label for="%s"%s class="checkbox">%s' % (widget.id_for_label(id_), attrs, unicode(contents))
            elif id_ == "id_department":
                contents = u'<label for="%s"%s>Group:</label>' % (widget.id_for_label(id_), attrs)
            else:
                contents = u'<label for="%s"%s>%s</label>' % (widget.id_for_label(id_), attrs, unicode(contents))
        return mark_safe(contents)

    def css_classes(self, extra_classes=None):
        """
        Returns a string of space-separated CSS classes for this field.
        """
        if hasattr(extra_classes, 'split'):
            extra_classes = extra_classes.split()
        extra_classes = set(extra_classes or [])
        if self.errors and hasattr(self.form, 'error_css_class'):
            extra_classes.add(self.form.error_css_class)
        if self.field.required and hasattr(self.form, 'required_css_class'):
            extra_classes.add(self.form.required_css_class)

        return ' '.join(extra_classes)

