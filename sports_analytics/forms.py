from xml.dom import ValidationErr
from django import forms
from .models import Team,Result
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Fieldset, HTML

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['team_name','team_hit','team_posession']


class ResultForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ResultForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
            Row(
                Column('team1', css_class="form-select p-2"),
                HTML("""<p class="versus center">vs</p>"""),
                Column('team2', css_class="form-select p-2"),
                css_class = "form-row flex"
            ),
            Column('number_runs', css_class="nr_center"),
        )
        
        # self.helper.add_input(Submit('submit', 'Submit', css_class='btn-primary'))

    class Meta:
        model = Result
        fields = ['team1','team2','number_runs']

    def clean(self):
        cleaned_data = super(ResultForm,self).clean()
        team1 = cleaned_data.get('team1')
        team2 = cleaned_data.get('team2')
        runs = cleaned_data.get('number_runs')

        if runs == 0:
            raise forms.ValidationError("Cannot Simulate 0 runs Match.")
            
        if team1 == team2:
            raise forms.ValidationError("Cannot Simulate Match for Same Teams.")
        
        
        
        return cleaned_data
