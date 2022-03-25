from flask.views import MethodView
from flask import Flask, render_template, request
from wtforms import Form, StringField, SubmitField
from calorie import Calorie
from temperature import Temperature 
from wtforms import Form
from wtforms.validators import Required

app = Flask(__name__) #instanciating an object or a Flask object

class HomePage(MethodView):
    
    def get(self):
        return render_template("index.html")


class CaloriesFormPage(MethodView):
    def get(self):
        calorieform = CalorieForm() #Initializing the CalorieForm class
        return render_template("calories_form_page.html" , calorieform=calorieform) 

    def post(self):
        
        # This is where we process the inputted data and  do the calculations
        calorieform = CalorieForm(request.form) #Initializing the CalorieForm class, but adding the formdata argument
        
        weight = int(calorieform.weight.data) #This is from the front end form
        height = int(calorieform.height.data)
        age = int(calorieform.age.data)
        
        country = calorieform.country.data
        city = calorieform.city.data
        temperature = Temperature(country=country, city=city).get()
        calorie = Calorie(weight, height, age, temperature)
        calorie_value = calorie.calculate()
            
        return render_template("calories_form_page.html" , calorieform=calorieform,
                               result=True, calorie_value=calorie_value)


class CalorieForm(Form): #This is not a page, but a form
    weight = StringField("Weight: ", default= "70") #default values for StringFields
    height = StringField("Height: ", default= "176") #default values for StringFields
    age = StringField("Age: ", default= "32") #default values for StringFields

    country = StringField("Country: ", default= "italy")
    city = StringField("City: ", default= "rome")

    button = SubmitField("Calculate")
    

# StringField(label=None, validators=None, filters=tuple(), description='', id=None, default=None, widget=None, render_kw=None,
#             _form=None, _name=None, _prefix='', _translations=None, _meta=None)
# SubmitField(label=None, validators=None, false_values=None, **kwargs: Any)
# BillForm(formdata=None, obj=None, prefix='', data=None, meta=None, **kwargs: Any)

app.add_url_rule('/', view_func=HomePage.as_view('home_page')) #as_view is gotten from MethodView, home_page, using same name as the class is a good practice
app.add_url_rule('/calories', view_func=CaloriesFormPage.as_view('calories_form_page')) #view_fun, treats this class as a function e.g @app.route('/bill'), def bill_form_page()
# app.add_url_rule('/results', view_func=ResultsPage.as_view('results_page'))


if __name__ == "__main__":
    app.debug = True #This also enables auto reloading
    app.run()
