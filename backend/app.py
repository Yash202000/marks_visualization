import json
from venv import create
from flask import Flask, render_template,send_file, request,jsonify
from werkzeug import secure_filename
import os
from flask_cors import CORS, cross_origin
import shutil



from components.modules.preprocess_file import create_all_dataset
from components.modules.operations import *



UPLOAD_FOLDER = './datasets'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','xlsx','csv'}

app = Flask(__name__)
CORS(app)



app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')  
def upload():  
    return render_template("file_upload_form.html")  
 
@app.route('/success', methods = ['POST'])  
def success():  
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)
        file_name = f.filename
        return render_template("success.html", name = f.filename)

@app.route('/test_uploader', methods=['GET','POST'])
def test_uploader():
    if request.method =='POST':
        return jsonify('success')



@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file():
    global file_name
    if request.method == 'POST':
        f = request.files['file']
        if(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))):
            print('inside uploader and exists...')
            return 'success'
        else:
            if(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],'final.csv'))):
                print('inside not exists removing directory...')
                
                shutil.rmtree('datasets')
                os.mkdir('datasets')

                f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
                file_name = f.filename
                if create_all_dataset(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))):
                    
                    return 'success'
            else:
                f.save(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename)))
                file_name = f.filename
                if create_all_dataset(os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(f.filename))):
                    
                    return 'success'
        
        # return "file uploaded successfully"


@app.route('/get_table/<string:val>',methods=['GET','POST'])
def get_sem1_table(val):
    return jsonify(get_tables(val))
    


@app.route('/sem1/<string:val>',methods=['GET','POST'])
def sem1(val):

    return jsonify(get_single_column_values(int(val)))
    # return give_result_sheet(3)


@app.route('/sem2/<string:val>',methods=['GET','POST'])
def sem2(val):

    return jsonify(get_single_column_values_sem2(int(val)))
    # return give_result_sheet(3)
            
@app.route('/get_col_list/<string:val>',methods=['GET','POST'])
def get_col_list(val):
    return jsonify(get_columns(int(val)))



@app.route('/get_backlog_details_th',methods=['GET','POST'])
def backlog_details_th():
    return jsonify(get_backlog_details_th())


@app.route('/get_backlog_details_pr',methods=['GET','POST'])
def backlog_details_pr():
    return jsonify(get_backlog_details_pr())

@app.route('/get_backlog_details',methods=['GET','POST'])
def backlog_details_total():
    return jsonify(get_backlog_details())

@app.route('/get_ranks',methods=['GET','POST'])
def get_ranks():
    return jsonify(give_me_ranks())

@app.route('/get_sgpa',methods=['GET','POST'])
def get_sgpa():
    return jsonify(give_me_sgpa())


@app.route('/get_class',methods=['GET','POST'])
def get_class():
    return jsonify(give_class())








if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')