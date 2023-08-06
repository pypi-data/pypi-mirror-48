# django-bootstrap-datetimepicker

This package includes a Django widget for displaying date pickers with Bootstrap 4. It uses [Bootstrap datepicker widget version 1.6.4 ](https://github.com/uxsolutions/bootstrap-datepicker).

## Install

    pip install django-bootstrap-datepicker

Make sure to add `bootstrap_datepicker` to your `INSTALLED_APPS`. Then run `manage.py collectstatic` to include the bootstrap-datepicker js and css files.

## To-Do

    General cleanup and testing

## Example

#### forms.py

```python
from bootstrap_datepicker.widgets import DatePicker
from django import forms

class ToDoForm(forms.Form):
    todo = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control"}))
    date = forms.DateField(
        widget=DatePicker(
            options={
                "format": "mm/dd/yyyy",
                "autoclose": True
            }
        )
    )
```

The `options` will be passed to the JavaScript datepicker instance, and are documented and demonstrated here:

* [Bootstrap Datepicker Documentation](https://bootstrap-datepicker.readthedocs.org/en/stable/) (ReadTheDocs.com)
* [Interactive Demo Sandbox of All Options](https://uxsolutions.github.io/bootstrap-datepicker/)

You don't need to set the `language` option, because it will be set the current language of the thread automatically.

#### template.html

```html
<!DOCTYPE html>
<html>
  <head>
    <link rel="stylesheet" href="{% static 'contrib/bootstrap.css' %}">
    <link rel="stylesheet" href="{% static 'contrib/font-awesome.min.css' %}">
    <script src="{% static 'contrib/bootstrap.js' %}"></script>
  </head>
  <body>
    <form method="post" role="form">
      {{ form|bootstrap }}
      {% csrf_token %}
      <div class="form-group">
        <input type="submit" value="Submit" class="btn btn-primary" />
      </div>
    </form>
  </body>
</html>
```

Here we assume you're using [django-bootstrap-form](https://github.com/tzangms/django-bootstrap-form) or 
[django-jinja-bootstrap-form](https://github.com/samuelcolvin/django-jinja-bootstrap-form) but you can
draw out your HTML manually.

## Requirements

* Python >= 3.4
* Django >= 2.0
* Bootstrap >= 4.0
* jquery >= 1.7.1
* font-awesome >= 4.5.X
