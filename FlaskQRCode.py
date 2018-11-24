from flask import Flask,render_template,url_for,request,redirect
import qrcode,quopri

app = Flask(__name__)



@app.route('/',methods=["GET","POST"])
def index():
    if request.method == "POST":
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        value = request.form['value']
        qr.add_data(value)
        qr.make(fit=True)

        image = qr.make_image(fill_color="black", back_color="white")
        image.save('genqr1.png')
        return redirect(url_for('QR_Code'))
    return render_template('index.html')


@app.route('/QRCode',methods=["GET","POST"])
def QR_Code():
    return render_template('QRCode.html')



if __name__ == "__main__":
     app.run(debug=True)   

