from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from paramiko import SSHClient, AutoAddPolicy
from forms import SearchForm
import json

ssh = SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(AutoAddPolicy())
port = 3637
hostname = "158.129.140.201"
username = "user033"
password = "D71E4x3N"
ssh.connect(hostname, port, username, password)

searchinput=""


app = Flask(__name__)
#CSRF Protection
app.config['SECRET_KEY'] = '477679530321ba4cfc7def294d03ba93'


def getdata(end):
    print("SEARCHING FOR " + end)
    start = "bitcoin-cli "
    middle = "getblockheader "
    try:
        print("Trying by getblockheader")
        command = start + middle + end
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
        y = json.loads(ssh_stdout.read())
        print(y["height"])

        print("Success")
        return y
    except:
        try:
            print("Trying by getblockhash")
            middle = "getblockhash "
            command = start + middle + end
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            y = ssh_stdout.read()
            if not y:
                print("EMPTY")
                raise Exception("nothing found")
            middle = "getblockheader "
            command = start + middle + y.decode("utf-8")
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            y = json.loads(ssh_stdout.read())
            print("Success")
            return y
        except:
            try:
                print("Trying by getrawtransaction")
                middle = "getrawtransaction "
                command = start + middle + end + " true"
                ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
                y = json.loads(ssh_stdout.read())
                print("Success")
                return y
            except:
                print("could not be found")
                y = {
                 "Nothing": "Found"
                }
                return y


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        searchinput = request.form["searchinput"]
    form = SearchForm()
    return render_template('index.html', form=form)


@app.route("/results", methods=['POST', 'GET'])
def results():
    if request.method == "POST":
        result = request.form
        query = result['searchinput']
        result = getdata(result['searchinput'])

        return render_template("results.html", result=result, query=query)
    return render_template("results.html")


if __name__ == "__main__":
    app.run(debug=True)