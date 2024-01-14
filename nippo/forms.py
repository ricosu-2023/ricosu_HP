from django import forms
from .models import NippoModel
from bootstrap_datepicker_plus.widgets import DatePickerInput
#from bootstrap_datepicker_plus import DatePickerInput
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
# Django設定をimport
from django.conf import settings


class NippoModelForm(forms.ModelForm):
    date = forms.DateField(
        label="作成日",
        widget=DatePickerInput(format='%Y-%m-%d')
    )

    class Meta:          
        model = NippoModel
        exclude = ["user"]


        #fields = "__all__"

    def __init__(self, user=None,*args, **kwargs):
        for key, field in self.base_fields.items():
            if key != "public":
                field.widget.attrs["class"] = "form-control"
            else:
                field.widget.attrs["class"] = "form-check-input"
        self.user = user
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        nippo_obj = super().save(commit=False)
        if self.user:
            nippo_obj.user = self.user
        if commit:
            nippo_obj.save()
        return nippo_obj
        
class NippoFormClass(forms.Form):
    title = forms.CharField(label="タイトル", widget=forms.TextInput(attrs={'placeholder':'タイトル...'}))
    content = forms.CharField(label="内容",widget=forms.Textarea(attrs={'placeholder':'内容...'}))

    def __init__(self, *args, **kwargs):
        for field in self.base_fields.values():
            field.widget.attrs.update({"class":"form-control"})
        super().__init__(*args, **kwargs)


# 2024-01-06追加
Number=[
    ('radio-1', '食品関係（製品、共同開発、ＯＥＭ等'), 
    ('radio-2', '酵素関係'), 
    ('radio-3', '微生物（食品用）の受託培養・製造関係'),
    ('radio-4', 'その他'),
]
Ken =[
    ('北海道','北海道')	,
    ('青森県','青森県')	,
	('岩手県','岩手県')	,							
	('宮城県','宮城県')	,														
	('秋田県','秋田県')	,												
    ('山形県','山形県')	,							
	('福島県','福島県')	,														
	('茨城県','茨城県')	,												
    ('栃木県','栃木県')	,								
	('群馬県','群馬県')	,														
	('埼玉県','埼玉県')	,												
    ('千葉県','千葉県')	,							
	('東京都','東京都')	,														
	('神奈川県','神奈川県'),													
    ('新潟県','新潟県'),								
	('富山県','富山県')	,														
	('石川県','石川県')	,												
    ('福井県','福井県')	,							
	('山梨県','山梨県')	,														
	('長野県','長野県')	,												
    ('岐阜県','岐阜県')	,								
	('静岡県','静岡県')	,														
	('愛知県','愛知県')	,												
    ('三重県','三重県')	,							
	('滋賀県','滋賀県')	,														
	('京都府','京都府')	,												
    ('大阪府','大阪府')	,							
	('兵庫県','兵庫県')	,														
	('奈良県','奈良県')	,												
    ('和歌山県','和歌山県'),								
	('鳥取県','鳥取県'),															
	('島根県','島根県')	,												
    ('岡山県','岡山県')	,							
	('広島県','広島県')	,														
	('山口県','山口県')	,												
    ('徳島県','徳島県')	,							
	('香川県','香川県')	,														
	('愛媛県','愛媛県')	,												
    ('高知県','高知県')	,								
	('福岡県','福岡県')	,														
	('佐賀県','佐賀県')	,												
    ('長崎県','長崎県')	,					
	('熊本県','熊本県')	,														
	('大分県','大分県')	,												
    ('宮崎県','宮崎県')	,							
	('鹿児島県','鹿児島県')	,												
    ('沖縄県','沖縄県')	,								
]
class ContactForm(forms.Form):
    # フォーム項目として"問い合わせ内容"を定義
    radio = forms.ChoiceField(
        choices=Number,
        label='　　　　　　　　　　　　　　　①問い合わせ内容　　　　',
    )
   
    # フォーム項目として"お名前"を定義
    name = forms.CharField(
        label='　　　　　　　　　　　　　　　②氏名　　　　　　　　　',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "氏名",
        }),
    )
    # フォーム項目として"お名前"を定義
    kana = forms.CharField(
        label='　　　　　　　　　　　　　　　③氏名（カナ）　　　　　',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "氏名（カナ）",
        }),
    )
    # フォーム項目として"会社名"を定義
    org_name = forms.CharField(
        label='　　　　　　　　　　　　　　　④会社名　　　　　　　　',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "会社名",
        }),
    )

    # フォーム項目として"部署名"を定義
    dept_name = forms.CharField(
        label='　　　　　　　　　　　　　　　⑤部署名　　　　　　　　',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "部署名",
        }),
    )
    # フォーム項目として"郵便番号"を定義
    zip_code1 = forms.CharField(
        label='　　　　　　　　　　　　　　　⑥郵便番号（上３桁）　　',
        #label = "",
        max_length=3,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "郵便番号（上３桁）",
        }),

    )
    zip_code2 = forms.CharField(
        label='　　　　　　　　　　　　　　　⑦郵便番号（下４桁）　　',
        #label = "",
        max_length=4,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "郵便番号（下４桁）",
        }),
    )
     # フォーム項目として"都道府県"を定義
    address1 = forms.ChoiceField(
        label='　　　　　　　　　　　　　　　⑧都道府県　　　　　　　',
        choices=Ken,
    )
     # フォーム項目として"市区町村以下"を定義
    address2 = forms.CharField(
        label='　　　　　　　　　　　　　　　⑨市区町村以下　　　　　',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "市区町村以下",
        }),
    )
    # フォーム項目として"建物名・部屋番号"を定義
    apart = forms.CharField(
        required=False,
        label='　　　　　　　　　　　　　　　⑩建物名・部屋番号　　　',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "建物名・部屋番号",
        }),
    )
    # フォーム項目として"電話番号"を定義
    phone = forms.CharField(
        label='　　　　　　　　　　　　　　　⑪電話番号　　　　　　　',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "電話番号",
        }),
    )
    # フォーム項目として"電話番号"を定義
    fax = forms.CharField(
        required=False,
        label='　　　　　　　　　　　　　　　⑫FAX（任意）　　　　　',
        #label = "",
        max_length=255,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': "FAX",
        }),
    )
    # フォーム項目として"メールアドレス"を定義
    mail = forms.EmailField(
        label='　　　　　　　　　　　　　　　⑬メールアドレス　　　　',
        #label = "",
        max_length=255,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': "メールアドレス",
        }),
    )
    # フォーム項目として"お問い合わせ内容"を定義
    inq2 = forms.CharField(
        label='　　　　　　　　　　　　　　　⑭お問い合わせ内容　　　',
        #label = "",
        max_length=255,
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': "お問い合わせ内容",
        }),
    )
    # メールを送信する
    def send_email(self):
 
        message = self.cleaned_data['inq2']
        name = self.cleaned_data['name']
        email = self.cleaned_data['mail']
        from_email = '{name} <{email}>'.format(name=name, email=email)
        # 受信者リストを指定
        recipient_list = [settings.EMAIL_HOST_USER]

        if self.cleaned_data['radio'] == "radio-1":
            message  = '食品関係（製品、共同開発、ＯＥＭ等'
            subject  = '食品関係（製品、共同開発、ＯＥＭ等'
        if self.cleaned_data['radio'] == "radio-2":
            message = '酵素関係'
            subject = '酵素関係'
        if self.cleaned_data['radio'] == "radio-3":
            message = '微生物（食品用）の受託培養・製造関係' 
            subject = '微生物（食品用）の受託培養・製造関係'  
        if self.cleaned_data['radio'] == "radio-4":
            message = 'その他'   
            subject = 'その他'  

        msg = "問い合わせ内容："         + message                    + \
              "\n \n 氏名："             + self.cleaned_data['name']  + \
              "\n \n 氏名（カナ）："     + self.cleaned_data['kana']  + \
              "\n \n 会社名："           + self.cleaned_data['org_name'] + \
              "\n \n 部署名："           + self.cleaned_data['dept_name'] +  \
              "\n \n 郵便番号："         + self.cleaned_data['zip_code1'] + "-" + self.cleaned_data['zip_code2'] + \
              "\n \n 都道府県："         + self.cleaned_data['address1'] + \
              "\n \n 市区町村以下："     + self.cleaned_data['address2'] + \
              "\n \n 建物名・部屋番号：" + self.cleaned_data['apart'] + \
              "\n \n 電話番号："         + self.cleaned_data['phone'] + \
              "\n \n FAX（任意）："      + self.cleaned_data['fax']  + \
              "\n \n メールアドレス："   + self.cleaned_data['mail']  + \
              "\n \n お問い合わせ内容："   + self.cleaned_data['inq2']
        try:
            send_mail(subject, msg, from_email, recipient_list)
            
        except BadHeaderError:
           
            return HttpResponse("無効なヘッダが検出されました。")
        
