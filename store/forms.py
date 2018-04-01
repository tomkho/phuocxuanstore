from django import forms
from .models import Profile

from django.core.validators import RegexValidator

class ProfileForm(forms.Form):
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,13}$', message="Số điện thoại không thích hợp.(Chỉ gồm 9-13 ký tự số)")
    fullname = forms.CharField(max_length=100,label='Họ Tên',help_text='*. Cần điền đầy đủ họ tên.',required=True)
    address = forms.CharField(max_length=500,label='Địa Chỉ',help_text='*. Cần điền địa chỉ.',required=True)
    sdt = forms.CharField(label='Số Điện Thoại',help_text='*. Cần điền số điện thoại.',required=True,validators=[phone_regex])
    #class Meta:
    #    model = Profile
    #    fields = ('fullname','address','sdt','added_date')

class ReviewForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea,label='',required=True)



