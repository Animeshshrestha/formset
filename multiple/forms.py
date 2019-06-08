from django import forms


from .models import Post

class PostModelForm(forms.ModelForm):
  
    class Meta:
        model = Post
        fields = [
           
            "title", 
            "slug", 
            "image",
            ]
        labels = {
            "title": "this is title label",
            "slug": "This is slug"
        }
        help_text = {
            "title": "this is title labe",
            "slug": "This is slug"
        }
        error_messages = { }

    def __init__(self, *args, **kwargs):
        super(PostModelForm, self).__init__(*args, **kwargs)
        
        for field in self.fields.values():

            field.error_messages = {
                'required': "You know, {fieldname} is required".format(fieldname=field.label),
                'max_length': "{fieldname} title is too long".format(fieldname=field.label),
                'unique': "The {fieldname} field must be unique".format(fieldname=field.label),

            }
















SOME_CHOICES = [
        ('db-value', 'Display Value'),
        ('db-value2', 'Display Value2'),
        ('db-value3', 'Display Value3'),
    ]

INTS_CHOICES = [tuple([x,x]) for x in range(0, 102)]

YEARS = [x for x in range(1980, 2031)]

class TestForm(forms.Form):
    date_field = forms.DateField(initial="2010-11-20", widget=forms.SelectDateWidget(years=YEARS))
    some_text = forms.CharField(label='Text', widget=forms.Textarea(attrs={"rows": 4, "cols": 10}))
    choices = forms.CharField(label='Text', widget=forms.Select(choices=SOME_CHOICES))
    boolean = forms.BooleanField()
    integer = forms.IntegerField(initial=101, widget=forms.Select(choices=INTS_CHOICES))
    email = forms.EmailField(min_length=10)

    def __init__(self, user=None, *args, **kwargs):
        super(TestForm, self).__init__(*args, **kwargs)
        #print(user)
        if user:
            self.fields["some_text"].initial = user.username

    def clean_integer(self, *args, **kwargs):
        integer = self.cleaned_data.get("integer")
        if integer < 10:
            raise forms.ValidationError("The integer must be greater than 10")
        return integer

    def clean_some_text(self, *args, **kwargs):
        some_text = self.cleaned_data.get("some_text")
        if len(some_text) < 5:
            raise forms.ValidationError("Ensure the text is greater than 5 characters")
        return some_text
