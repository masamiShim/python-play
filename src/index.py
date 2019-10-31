from bottle import route, run, template, os


def list_files(startpath: str):
    output_string = ""
    for root, dirs, files in os.walk(startpath):
        level: int = root.replace(startpath, '').count(os.sep)
        print(level)
        print(4 * level)
        indent: str = ' ' * (4 * level)
        output_string = output_string + '{}{}/'.format(indent, os.path.basename(root))
        subindent: str = ' ' * (4 * (level + 1))
        for f in files:
            output_string = output_string + '{}{}'.format(subindent, f)
            return output_string


@route('/yourpath')
def hello():
    output_string = list_files('/')
    return template("template", output_string=output_string)


run(host='0.0.0.0', port=5000, reloader=True)
