from flask import Flask, render_template, url_for, request, flash, redirect, request
from interface import GA_Interface
from src import Knapsack_GA,Knapsack_DP
app = Flask(__name__)

app.config['SECRET_KEY'] = '2cff3d8754a9518a11dc02bf940d7ebe'

def get_ga(form):
    weight_list = list()
    weight_list.append(form.weight1.data)
    if(form.weight2.data != None):
        weight_list.append(form.weight2.data)
    if(form.weight3.data != None):
        weight_list.append(form.weight3.data)
    if(form.weight4.data != None):
        weight_list.append(form.weight4.data)
    value_list = list()
    value_list.append(form.value1.data)
    if(form.value2.data != None):
        value_list.append(form.value2.data)
    if(form.value3.data != None):
        value_list.append(form.value3.data)
    if(form.value4.data != None):
        value_list.append(form.value4.data)
    knapsack_value  = form.knapsack_value.data
    gene_count = ( form.gene_count.data if form.gene_count.data else 8)
    gen_count = ( form.generation_count.data if form.generation_count.data else 50)
    crossover_rate = ( form.crossover_rate.data if form.crossover_rate.data else 0.8)
    mutation_rate = ( form.mutation_rate.data if form.mutation_rate.data else 0.4)
    ga_obj = Knapsack_GA.Knapsack_Class_GA(weight_list,value_list,knapsack_value,gene_count,gen_count,crossover_rate,mutation_rate)
    return ga_obj

def get_dp_sol(form):
    weight_list = list()
    weight_list.append(form.weight1.data)
    if(form.weight2.data != None):
        weight_list.append(form.weight2.data)
    if(form.weight3.data != None):
        weight_list.append(form.weight3.data)
    if(form.weight4.data != None):
        weight_list.append(form.weight4.data)
    value_list = list()
    value_list.append(form.value1.data)
    if(form.value2.data != None):
        value_list.append(form.value2.data)
    if(form.value3.data != None):
        value_list.append(form.value3.data)
    if(form.value4.data != None):
        value_list.append(form.value4.data)
    knapsack_value  = form.knapsack_value.data
    dp_obj = Knapsack_DP.Knapsack_Class_DP()
    return dp_obj.knapSack(knapsack_value,weight_list,value_list,len(weight_list))

@app.route("/", methods=['GET','POST'])
def home():
    # print('hello home !')
    form = GA_Interface()
    if form.validate_on_submit():
        ga_obj = get_ga(form)
        dp_result = get_dp_sol(form)
        ga_result = ga_obj.get_solution_ga()
        ga_graph_base64  = ga_obj.get_graph()
        #return redirect(url_for('result',title="Results",heading="Results",GA_Result=ga_result,DP_Result=dp_result))
        return render_template('result.html',title="Results",heading="Results",GA_Result=ga_result,DP_Result=dp_result,Graph_GA_Result=ga_graph_base64)
    try:
        ga_graph_base64
        del ga_graph_base64
    except NameError:
        pass
    return render_template('home.html',title="Home",form=form,heading='Problem Details')

@app.route("/result")
def result():
    return render_template('result.html',title="Results",heading="Results",GA_Result=False,DP_Result=False,Graph_GA_Result=url_for('static',filename='images/Figure_1.png'))

@app.route("/layout")
def layout():
    return render_template('layout.html',title = "Layout")

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()