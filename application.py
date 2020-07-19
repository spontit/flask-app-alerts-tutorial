from flask import Flask, render_template

application = Flask(__name__, template_folder='template', static_url_path='/static')
application.config.from_object(__name__)
application.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
application.url_map.strict_slashes = False


@application.route("/", endpoint="apiary", methods=["GET"])
def apiary():
    return render_template("hello.html")


# run the app.
if __name__ == "__main__":
    # Setting debug to True enables debug output. This line should be
    # removed before deploying a production app.
    application.debug = True
    application.run()

else:
    application.debug = True
    application.run()
