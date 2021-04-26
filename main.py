from flask import Flask, render_template, request,flash,redirect,url_for,flash,abort
import math
from csv import reader

app = Flask(__name__)
app.secret_key = "asdasdas"
language="Türkce"

height_difference=0
Elbow=0

def debi_func(gas_type,DN,allowed_p_l):
## gaz tipine ve dn'e gore csv'e girip  Q'yu dönuyor
    x=str(allowed_p_l).replace(".", ",")
    csv_val=gas_type+'.csv'
    print(csv_val)

    row_check={15:[0,1], 20:[3,4], 25:[6,7], 32:[6,7], 40:[12,13], 50:[15,16]}
    row1=row_check[DN][0]
    row2=row_check[DN][1]
    print(row1,row2)

    with open(csv_val, 'r') as read_obj:
        # pass the file object to reader() to get the reader object
        csv_reader = reader(read_obj,delimiter=';')
        # Iterate over each row in the csv using reader object
        set_dic={}
        if gas_type=="G31":
            for line in csv_reader: # row variable is a list that represents a row in csv
                set_dic[line[row1+1]]=line[row2+1]
        else:
            for line in csv_reader:
                set_dic[line[row1]]=line[row2]

    result=set_dic[x]
    return result


@app.route('/english', methods=['GET', 'POST'])
def english():
    
    
    if request.method=="POST":
        if request.form['submit'] == 'hesapla':
            try:
                height_difference=float(request.form['height_difference'])
                
            except:
                height_difference=0
                
            try:
                Elbow=int(request.form['Elbow'])
            except:
                Elbow=0


            DN_=str(request.form.getlist('DN')[0])
            DN=int(DN_[2:])
            
            Line_Length=float(request.form['Line_Length'])
            
            gas_type=str(request.form.getlist('inlineRadioOptions')[0])
            print(gas_type)
            print(DN)
            Inlet_press=21
            drop=1
            print(Inlet_press)
            print(drop)
            
            if gas_type== "G20":
                Inlet_press=21
                drop=1
                height_difference_effect= 0.046*(height_difference)
                allowed_pressure_drop=height_difference_effect+1

            if gas_type== "G25":
                
                Inlet_press=25
                drop=1
                height_difference_effect= 0.048*(height_difference)
                allowed_pressure_drop=height_difference_effect+1  

            if gas_type=="Propane":
                Inlet_press=37
                drop=2
                height_difference_effect= (-0.048)*(height_difference)
                allowed_pressure_drop=height_difference_effect+2 ## pressure_drop=2
                
            
            tee_effected_total_length=Line_Length+(0.5*Elbow)
            allowed_p_l=round((allowed_pressure_drop)/(tee_effected_total_length),3)
            print("Inlet_Press: ",Inlet_press)
            print("height_difference_effect", height_difference_effect)
            print("tee_effected_total_length: ", tee_effected_total_length)
            print("allowed_p_l: ",allowed_p_l)

            if gas_type=='Propane':
                gas_type_2='G31'
            else:
                gas_type_2=gas_type
            
            print("({},{},{})".format(gas_type_2,DN,allowed_p_l))
            try:
                basinc_kaybi=debi_func(gas_type_2,DN,allowed_p_l)
            except:
                print("error returned")
                basinc_kaybi=0
                return render_template("english.html",basinc_kaybi=basinc_kaybi)

            return render_template("english.html",basinc_kaybi=basinc_kaybi,height_difference=height_difference,DN=DN,Line_Length=Line_Length,gas_type=gas_type,Inlet_press=Inlet_press,drop=drop)
    else:
        basinc_kaybi=0
        return render_template("english.html",basinc_kaybi=basinc_kaybi)
            


@app.route('/', methods=['GET', 'POST'])
def main_page():
    if request.method=="POST":
        if request.form['submit'] == 'hesapla':

            try:
                height_difference=float(request.form['height_difference'])
                
            except:
                height_difference=0
                
            try:
                Elbow=int(request.form['Elbow'])
            except:
                Elbow=0
            DN_=str(request.form.getlist('DN')[0])
            DN=int(DN_[2:])
            
            Line_Length=float(request.form['Line_Length'])
            gas_type=str(request.form.getlist('inlineRadioOptions')[0])
            print(gas_type)
            print(DN)

            if gas_type== "G20":
                Inlet_press=21
                height_difference_effect= 0.046*(height_difference)
                allowed_pressure_drop=height_difference_effect+1

            if gas_type== "G25":
                
                Inlet_press=25
                height_difference_effect= 0.048*(height_difference)
                allowed_pressure_drop=height_difference_effect+1  

            if gas_type=="Propane":
                Inlet_press=37
                height_difference_effect= (-0.048)*(height_difference)
                allowed_pressure_drop=height_difference_effect+1 ## pressure_drop=1
                
            
            tee_effected_total_length=Line_Length+(0.5*Elbow)
            allowed_p_l=round((allowed_pressure_drop)/(tee_effected_total_length),3)
            print("Inlet_Press: ",Inlet_press)
            print("height_difference_effect", height_difference_effect)
            print("tee_effected_total_length: ", tee_effected_total_length)
            print("allowed_p_l: ",allowed_p_l)

            if gas_type=='Propane':
                gas_type_2='G31'
            else:
                gas_type_2=gas_type
            
            print("({},{},{})".format(gas_type_2,DN,allowed_p_l))
            try:
                basinc_kaybi=debi_func(gas_type_2,DN,allowed_p_l)
            except:
                print("error returned")
                basinc_kaybi=0
                return render_template("dutch.html",basinc_kaybi=basinc_kaybi)

            return render_template("dutch.html",basinc_kaybi=basinc_kaybi,height_difference=height_difference,DN=DN,Line_Length=Line_Length,gas_type=gas_type)
    else:
        basinc_kaybi=0
        return render_template("dutch.html",basinc_kaybi=basinc_kaybi)

    
            
            
@app.route('/francais', methods=['GET', 'POST'])
def francais():
    if request.method=="POST":
        if request.form['submit'] == 'hesapla':

            try:
                height_difference=float(request.form['height_difference'])
                
            except:
                height_difference=0
                
            try:
                Elbow=int(request.form['Elbow'])
            except:
                Elbow=0
            DN_=str(request.form.getlist('DN')[0])
            DN=int(DN_[2:])
            
            Line_Length=float(request.form['Line_Length'])
            gas_type=str(request.form.getlist('inlineRadioOptions')[0])
            print(gas_type)
            print(DN)

            if gas_type== "G20":
                Inlet_press=21
                height_difference_effect= 0.046*(height_difference)
                allowed_pressure_drop=height_difference_effect+1

            if gas_type== "G25":
                
                Inlet_press=25
                height_difference_effect= 0.048*(height_difference)
                allowed_pressure_drop=height_difference_effect+1  

            if gas_type=="Propane":
                Inlet_press=37
                height_difference_effect= (-0.048)*(height_difference)
                allowed_pressure_drop=height_difference_effect+1 ## pressure_drop=1
                
            
            tee_effected_total_length=Line_Length+(0.5*Elbow)
            allowed_p_l=round((allowed_pressure_drop)/(tee_effected_total_length),3)
            print("Inlet_Press: ",Inlet_press)
            print("height_difference_effect", height_difference_effect)
            print("tee_effected_total_length: ", tee_effected_total_length)
            print("allowed_p_l: ",allowed_p_l)

            if gas_type=='Propane':
                gas_type_2='G31'
            else:
                gas_type_2=gas_type
            
            print("({},{},{})".format(gas_type_2,DN,allowed_p_l))
            try:
                basinc_kaybi=debi_func(gas_type_2,DN,allowed_p_l)
            except:
                print("error returned")
                basinc_kaybi=0
                return render_template("francais.html",basinc_kaybi=basinc_kaybi)

            return render_template("francais.html",basinc_kaybi=basinc_kaybi,height_difference=height_difference,DN=DN,Line_Length=Line_Length,gas_type=gas_type)
    else:
        basinc_kaybi=0
        return render_template("francais.html",basinc_kaybi=basinc_kaybi)
   
            
            
@app.route('/dutch', methods=['GET', 'POST'])
def dutch():
    if request.method=="POST":
        if request.form['submit'] == 'hesapla':

            try:
                height_difference=float(request.form['height_difference'])
                
            except:
                height_difference=0
                
            try:
                Elbow=int(request.form['Elbow'])
            except:
                Elbow=0
            DN_=str(request.form.getlist('DN')[0])
            DN=int(DN_[2:])
            
            Line_Length=float(request.form['Line_Length'])
            gas_type=str(request.form.getlist('inlineRadioOptions')[0])
            print(gas_type)
            print(DN)

            if gas_type== "G20":
                Inlet_press=21
                height_difference_effect= 0.046*(height_difference)
                allowed_pressure_drop=height_difference_effect+1

            if gas_type== "G25":
                
                Inlet_press=25
                height_difference_effect= 0.048*(height_difference)
                allowed_pressure_drop=height_difference_effect+1  

            if gas_type=="Propane":
                Inlet_press=37
                height_difference_effect= (-0.048)*(height_difference)
                allowed_pressure_drop=height_difference_effect+1 ## pressure_drop=1
                
            
            tee_effected_total_length=Line_Length+(0.5*Elbow)
            allowed_p_l=round((allowed_pressure_drop)/(tee_effected_total_length),3)
            print("Inlet_Press: ",Inlet_press)
            print("height_difference_effect", height_difference_effect)
            print("tee_effected_total_length: ", tee_effected_total_length)
            print("allowed_p_l: ",allowed_p_l)

            if gas_type=='Propane':
                gas_type_2='G31'
            else:
                gas_type_2=gas_type
            
            print("({},{},{})".format(gas_type_2,DN,allowed_p_l))
            try:
                basinc_kaybi=debi_func(gas_type_2,DN,allowed_p_l)
            except:
                print("error returned")
                basinc_kaybi=0
                return render_template("dutch.html",basinc_kaybi=basinc_kaybi)

            return render_template("dutch.html",basinc_kaybi=basinc_kaybi,height_difference=height_difference,DN=DN,Line_Length=Line_Length,gas_type=gas_type)
    else:
        basinc_kaybi=0
        return render_template("dutch.html",basinc_kaybi=basinc_kaybi)

@app.route('/deutsch', methods=['GET', 'POST'])
def deutsch():
    if request.method=="POST":
        if request.form['submit'] == 'hesapla':
            try:
                height_difference=float(request.form['height_difference'])
                
            except:
                height_difference=0
                
            try:
                Elbow=int(request.form['Elbow'])
            except:
                Elbow=0

            DN_=str(request.form.getlist('DN')[0])
            DN=int(DN_[2:])
            
            Line_Length=float(request.form['Line_Length'])
            gas_type=str(request.form.getlist('inlineRadioOptions')[0])
            print(gas_type)
            print(DN)

            if gas_type== "G20":
                Inlet_press=21
                height_difference_effect= 0.046*(height_difference)
                allowed_pressure_drop=height_difference_effect+1

            if gas_type== "G25":
                
                Inlet_press=25
                height_difference_effect= 0.048*(height_difference)
                allowed_pressure_drop=height_difference_effect+1  

            if gas_type=="Propane":
                Inlet_press=37
                height_difference_effect= (-0.048)*(height_difference)
                allowed_pressure_drop=height_difference_effect+1 ## pressure_drop=1
                
            
            tee_effected_total_length=Line_Length+(0.5*Elbow)
            allowed_p_l=round((allowed_pressure_drop)/(tee_effected_total_length),3)
            print("Inlet_Press: ",Inlet_press)
            print("height_difference_effect", height_difference_effect)
            print("tee_effected_total_length: ", tee_effected_total_length)
            print("allowed_p_l: ",allowed_p_l)

            if gas_type=='Propane':
                gas_type_2='G31'
            else:
                gas_type_2=gas_type
            
            print("({},{},{})".format(gas_type_2,DN,allowed_p_l))
            try:
                basinc_kaybi=debi_func(gas_type_2,DN,allowed_p_l)
            except:
                print("error returned")
                basinc_kaybi=0
                return render_template("deutsch.html",basinc_kaybi=basinc_kaybi)

            return render_template("deutsch.html",basinc_kaybi=basinc_kaybi,height_difference=height_difference,DN=DN,Line_Length=Line_Length,gas_type=gas_type)
    else:
        basinc_kaybi=0
        return render_template("deutsch.html",basinc_kaybi=basinc_kaybi)

@app.route('/turkce', methods=['GET', 'POST'])
def turkce():
    if request.method=="POST":
        if request.form['submit'] == 'hesapla':

            try:
                height_difference=float(request.form['height_difference'])
                
            except:
                height_difference=0
                
            try:
                Elbow=int(request.form['Elbow'])
            except:
                Elbow=0
            DN_=str(request.form.getlist('DN')[0])
            DN=int(DN_[2:])
            
            Line_Length=float(request.form['Line_Length'])
            gas_type=str(request.form.getlist('inlineRadioOptions')[0])
            print(gas_type)
            print(DN)

            if gas_type== "G20":
                Inlet_press=21
                height_difference_effect= 0.046*(height_difference)
                allowed_pressure_drop=height_difference_effect+0.8

            if gas_type== "G25":
                
                Inlet_press=25
                height_difference_effect= 0.048*(height_difference)
                allowed_pressure_drop=height_difference_effect+0.8 

            if gas_type=="Propane":
                Inlet_press=37
                height_difference_effect= (-0.048)*(height_difference)
                allowed_pressure_drop=height_difference_effect+0.8 ## pressure_drop=1
                
            
            tee_effected_total_length=Line_Length+(0.5*Elbow)
            allowed_p_l=round((allowed_pressure_drop)/(tee_effected_total_length),3)
            print("Inlet_Press: ",Inlet_press)
            print("height_difference_effect", height_difference_effect)
            print("tee_effected_total_length: ", tee_effected_total_length)
            print("allowed_p_l: ",allowed_p_l)

            if gas_type=='Propane':
                gas_type_2='G31'
            else:
                gas_type_2=gas_type
            
            print("({},{},{})".format(gas_type_2,DN,allowed_p_l))
            try:
                basinc_kaybi=debi_func(gas_type_2,DN,allowed_p_l)
            except:
                print("error returned")
                basinc_kaybi=0
                return render_template("turkce.html",basinc_kaybi=basinc_kaybi)

            return render_template("turkce.html",basinc_kaybi=basinc_kaybi,height_difference=height_difference,DN=DN,Line_Length=Line_Length,gas_type=gas_type)
    else:
        basinc_kaybi=0
        return render_template("turkce.html",basinc_kaybi=basinc_kaybi)
            
        
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'),404


if __name__ == '__main__':

    app.run()