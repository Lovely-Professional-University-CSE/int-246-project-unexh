from flask_wtf import FlaskForm
from wtforms import IntegerField, DecimalField, SubmitField
from wtforms.validators import DataRequired, NumberRange, optional

minn = 0
maxx = 1000

class GA_Interface(FlaskForm):
    weight1 = IntegerField('Weights', validators=[DataRequired(), NumberRange(min=1,max=maxx)])
    weight2 = IntegerField('Weights', validators=[optional(), NumberRange(min=minn,max=maxx)])
    weight3 = IntegerField('Weights', validators=[optional(), NumberRange(min=minn,max=maxx)])
    weight4 = IntegerField('Weights', validators=[optional(), NumberRange(min=minn,max=maxx)])
    
    value1 = IntegerField('Values', validators=[DataRequired(),NumberRange(min=1,max=maxx)])
    value2 = IntegerField('Values', validators=[optional(), NumberRange(min=minn,max=maxx)])
    value3 = IntegerField('Values', validators=[optional(), NumberRange(min=minn,max=maxx)])
    value4 = IntegerField('Values', validators=[optional(), NumberRange(min=minn,max=maxx)])

    knapsack_value   = IntegerField('Knapsack Value', validators=[DataRequired(),NumberRange(min=1,max=maxx)])
    generation_count = IntegerField('Net Generations', validators=[optional(), NumberRange(min=1,max=maxx)])
    gene_count       = IntegerField('Chromosome Length', validators=[optional(), NumberRange(min=1,max=maxx)])
    mutation_rate    = DecimalField('Mutation Rate', validators=[optional(), NumberRange(min=0.001,max=1.0)])
    crossover_rate   = DecimalField('Crossover Rate', validators=[optional(), NumberRange(min=0.001,max=1.0)])
    submit           = SubmitField('Get Results')