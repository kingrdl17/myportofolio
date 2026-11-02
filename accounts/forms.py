from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


FORM_CONTROL_CLASSES = (
    "w-full rounded-xl border border-[#0a84ff] bg-[rgba(30,30,30,0.75)] p-3 "
    "font-sans text-[#f5f5f7] focus:border-[#0a84ff] focus:outline "
    "focus:outline-2 focus:outline-[#0a84ff]"
)


def style_form_controls(form):
    for field in form.fields.values():
        existing_classes = field.widget.attrs.get("class", "")
        field.widget.attrs["class"] = f"{existing_classes} {FORM_CONTROL_CLASSES}".strip()
    return form


class StyledAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_form_controls(self)


class StyledUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        style_form_controls(self)
