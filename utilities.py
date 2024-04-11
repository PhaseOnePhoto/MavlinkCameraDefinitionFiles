
"""
MIT License Copyright (c) 2022 Phase One A/S

Contributors:
 - David Wuthier (dwu@phaseone.com)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is furnished
to do so, subject to the following conditions:

The above copyright notice and this permission notice (including the next
paragraph) shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS
OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF
OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""


from xml.etree import ElementTree


def get_template(filename : str):
    return ElementTree.parse(filename)

def limit_options(options : ElementTree.Element, min : float, max : float):
    for option in options.findall('./option'):
        value = float(option.get('value'))

        if value < min or value > max:
            options.remove(option)

def get_options(filename : str):
    return ElementTree.parse(filename).getroot()

def remove_option(template : ElementTree, parameter : str, option : str):
    e1 = template.find(f'./parameters/parameter[@name="{parameter}"]/options')
    e2 = e1.find(f'./option[@name="{option}"]')
    e1.remove(e2)

def remove_exclude(template : ElementTree, parameter : str, option : str, exclude : str):
    e1 = template.find(f'./parameters/parameter[@name="{parameter}"]/options/option[@name="{option}"]/exclusions')
    e2 = e1.find(f'./exclude[.="{exclude}"]')
    e1.remove(e2)

def remove_parameter(template : ElementTree, parameter : str):
    e1 = template.find(f'./parameters')
    e2 = e1.find(f'./parameter[@name="{parameter}"]')
    e1.remove(e2)

def write_file(template : ElementTree, version : str, model : str, vendor : str):
    ElementTree.indent(template, '    ')

    template.write(f'{vendor}_{model}_0{version}.xml', encoding='utf-8', xml_declaration=True)

def copy_options(template : ElementTree, name : str, options : ElementTree.Element):
    e = template.find(f'./parameters/parameter[@name="{name}"]')
    e[1] = options

def set_text(template : ElementTree, path : str, text : str):
    e = template.find(path)
    e.text = text

def set_attribute(template : ElementTree, path : str, attribute : str, value : str):
    e = template.find(path)
    e.set(attribute, value)
