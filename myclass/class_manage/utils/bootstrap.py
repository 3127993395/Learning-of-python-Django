from django import forms


class Bootstrap:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            if field.widgets.attrs:
                field.widgets.attrs["class"] = "form-control"
                field.widgets.attrs["placeholder"] = field.labels
            else:
                field.widgets.attrs = {
                    "class": "form-control",
                    "placeholder": field.labels,
                }


class BootstrapModelForm(Bootstrap, forms.ModelForm):
    pass


class BootstrapForm(Bootstrap, forms.Form):
    pass
