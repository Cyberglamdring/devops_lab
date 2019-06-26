from jinja2 import Template

template = Template('Hello {{ name }}!')
message = template.render(name='John Doe')

print(message)
