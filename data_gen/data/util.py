import os


def get_template(template_name):
    template_filename = os.path.join(os.path.dirname(__file__), 'templates', template_name)
    with open(template_filename, "r") as f:
        template_string = f.read()

    return template_string


