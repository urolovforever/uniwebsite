from django import forms


class ContactForm(forms.Form):
    INQUIRY_CHOICES = [
        ('', 'Select a topic'),
        ('admissions', 'Admissions'),
        ('academics', 'Academics'),
        ('financial', 'Tuition & Financial Aid'),
        ('international', 'International Students'),
        ('careers', 'Career Services'),
        ('it', 'IT Support'),
        ('general', 'General Inquiry'),
    ]

    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Your full name',
            'class': 'contact-input',
        }),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'placeholder': 'Your email address',
            'class': 'contact-input',
        }),
    )
    topic = forms.ChoiceField(
        choices=INQUIRY_CHOICES,
        widget=forms.Select(attrs={
            'class': 'contact-input',
        }),
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'How can we help you?',
            'class': 'contact-input contact-textarea',
            'rows': 5,
        }),
    )
