from django.forms import widgets
from django.forms.util import flatatt
from django.utils.html import conditional_escape
from django.utils.encoding import force_unicode
from django.utils.safestring import mark_safe
from django.forms.widgets import MultiWidget
from time import strftime

# CUSTOM BUTTONSET RENDER
# SLIGHTLY MODIFIED CheckboxSelectMultiple


class ButtonSetButton(widgets.RadioInput):
    """
    An object that is similar to a radio button but it formatted for Bootstrap
    """

    def tag(self):
        if 'id' in self.attrs:
            self.attrs['id'] = '%s_%s' % (self.attrs['id'], self.index)
            
        final_attrs = dict(self.attrs, type='button', name=self.name,
                           value=self.choice_value)
            
        final_attrs["class"] = "btn"
        
        if self.is_checked():
            final_attrs['class'] += ' active'

        choice_label = conditional_escape(force_unicode(self.choice_label))
        
        return mark_safe(u'<button%s>%s</button>' %
                         (flatatt(final_attrs), choice_label))
        
    def render(self, name=None, value=None, attrs=None, choices=()):
        name = name or self.name
        value = value or self.value
        attrs = attrs or self.attrs
        if 'id' in self.attrs:
            label_for = ' for="%s_%s"' % (self.attrs['id'], self.index)
        else:
            label_for = ''

        choice_label = conditional_escape(force_unicode(self.choice_label))
        
        return mark_safe(u'%s' % (self.tag(), ))


class ButtonSetRenderer(widgets.RadioFieldRenderer):
    """
    An object used by ButtonSet to enable custom Bootstrap-based radio buttons
    """
    
    def __iter__(self):
        for i, choice in enumerate(self.choices):
            yield ButtonSetButton(self.name, self.value,
                                  self.attrs.copy(), choice, i)

    def __getitem__(self, idx):
        choice = self.choices[idx] # Let the IndexError propogate
        return ButtonSetButton(self.name, self.value,
                               self.attrs.copy(), choice, idx)
        
    def render(self):
        output = mark_safe(u"<div class=\"btn-group form-btn-group\" "
                           u"data-toggle-for=\"#%s\" data-toggle=\""
                           u"buttons-radio\">" % (self.attrs["id"], ))
        output += u'\n'.join([u'%s\n' % w for w in self])
        output += u"</div>"
        output += mark_safe(u"<input type=\"hidden\" id=\"%s\" name=\"%s\" "
                            u"value=\"%s\" />" %
                            (self.attrs["id"], self.name, self.value))
        
        return mark_safe(output)


class ButtonSet(widgets.RadioSelect):
    renderer = ButtonSetRenderer

    def id_for_label(self, id_):
        # RESETS ID SO IT DOES NOT MESS ANYTHING UP
        
        return id_


class Input(widgets.Input):
    """
    Exists solely for overriding all inputs on Django forms at once
    """
    
    def __init__(self, attrs=None):
        extra_attrs = {"class": "input-block-level"}
        
        if attrs:
            extra_attrs.update(attrs)
        
        super(Input, self).__init__(extra_attrs)
        
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
            
        final_attrs = self.build_attrs(attrs, type=self.input_type, name=name)
        
        if value != '':
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(self._format_value(value))
            
        if self.is_required:
            final_attrs["required"] = "required"
            
        return mark_safe(u'<input%s />' % flatatt(final_attrs))


class TextInput(Input, widgets.TextInput):
    pass


class NumberInput(TextInput):
    input_type = "number"


class PasswordInput(TextInput):
    input_type = "password"


class EmailInput(TextInput):
    input_type = "email"


class DateInput(TextInput):
    input_type = "date"


class UrlInput(TextInput):
    input_type = "url"


class Select(widgets.Select):
    def __init__(self, attrs=None):
        default_attrs = {"class": "input-block-level", }
        
        if attrs:
            default_attrs.update(attrs)
        
        super(Select, self).__init__(default_attrs)
        

class SelectMultipleAsSingle(widgets.Select):
    def __init__(self, attrs=None):
        default_attrs = {"class": "input-block-level", }
        
        if attrs:
            default_attrs.update(attrs)
        
        super(SelectMultipleAsSingle, self).__init__(default_attrs)
        
    def value_from_datadict(self, data, files, name):
        data = super(SelectMultipleAsSingle, self).value_from_datadict(data, files, name)
        return [data]
    
    
class Textarea(widgets.Textarea):
    
    def __init__(self, attrs=None):
        default_attrs = {"class": "input-block-level", }
        
        if attrs:
            default_attrs.update(attrs)
            
        super(Textarea, self).__init__(default_attrs)
    
    def render(self, name, value, attrs=None):
        if value is None:
            value = ''
        
        final_attrs = self.build_attrs(attrs, name=name)
            
        if self.is_required:
            final_attrs["required"] = "required"
        
        return mark_safe(u'<textarea%s>%s</textarea>' %
                         (flatatt(final_attrs),
                          conditional_escape(force_unicode(value))))


class CheckboxInput(widgets.CheckboxInput):

    def render(self, name, value, attrs=None):
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        
        try:
            result = self.check_test(value)
        except:  # Silently catch exceptions
            result = False
            
        if result:
            final_attrs['checked'] = 'checked'
            
        if not (value is True or value is False or value is None or value == ''):
            # Only add the 'value' attribute if a value is non-empty.
            final_attrs['value'] = force_unicode(value)
            
        return mark_safe(u'<input%s /></label>' % flatatt(final_attrs))


class BootstrapSplitDateTimeWidget(MultiWidget):
    """
    Bootstrap Split DateTime Widget

    github.com/stholmes/django-bootstrap-datetime-widgets/

    format_output slightly modified.
    """
    
    def __init__(self, attrs=None, date_format=None, time_format=None):
        from django.forms.widgets import DateInput, TimeInput

        date_class = attrs['date_class']
        time_class = attrs['time_class']
        del attrs['date_class']
        del attrs['time_class']

        time_attrs = attrs.copy()
        time_attrs['class'] = time_class

        date_attrs = attrs.copy()
        date_attrs['class'] = date_class

        widgets = (DateInput(attrs=date_attrs, format=date_format),
                   TimeInput(attrs=time_attrs))

        super(BootstrapSplitDateTimeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            d = strftime("%Y-%m-%d", value.timetuple())
            hour = strftime("%H", value.timetuple())
            minute = strftime("%M", value.timetuple())
            meridian = strftime("%p", value.timetuple())
            return d, hour+":"+minute, meridian
        else:
            return None, None, None

    def format_output(self, rendered_widgets):
        """
        Given a list of rendered widgets (as strings), it inserts an HTML
        linebreak between them.

        Returns a Unicode string representing the HTML for the whole lot.
        """
        return "<label>Date:</label> %s<br/><label>Time:</label> %s" % \
               (rendered_widgets[0], rendered_widgets[1])
