from optparse import OptionParser
import re
import os
import urllib.request
import xml.etree.cElementTree as ET
import lxml.etree as LET


__version__ = "0.4"


def version():
    return __version__


def main():

    junit_xml_output = "ansible-lint-nunit.xml"
    nunit_xsl_url = "https://raw.githubusercontent.com/artberri/junit-to-nunit/master/junit-to-nunit.xsl"
    nunit_xsl_file = "junit-to-nunit.xsl"

    parser = OptionParser(
        usage="%prog [ansible-lint output file] [options]",
        version="%prog " + version()
    )

    parser.add_option("-o", "--output", action="store", dest="output_file", help="output XML to file", default=junit_xml_output)
    parser.add_option("-v", "--verbose", action="store_true", dest="verbose", help="print XML to console as command output", default=False)

    (options, args) = parser.parse_args()

    if not args or not args[0]:
        parser.print_help()
        parser.error('You need to provide file with output from "ansible-lint -p" command.')
        exit(1)

    ansible_lint_output = open(args[0], "r").read().split("\n")

    testsuites = ET.Element("testsuites")
    errors_count = "0"

    for line in ansible_lint_output:
        if line:
            errors_count = str(len(ansible_lint_output) - 1)
            break

    testsuite = ET.SubElement(testsuites, "testsuite", errors=errors_count, failures="0", tests=errors_count, time="0")

    line_regex = re.compile('^(.*?):(\d+?):\s\[(.*)\]\s(.*)$')

    if not ansible_lint_output:
        testcase = ET.SubElement(testsuite, "testcase", name="dummy_testcase.py")
    else:
        parsed_lines = []
        for line in ansible_lint_output:
            if 0 < len(line):
                # print(line)

                line_match = line_regex.match(line)

                line_data = {
                    "filename": line_match.group(1),
                    "line": int(line_match.group(2)),
                    "error": {
                        "code": line_match.group(3),
                        "message": line_match.group(4),
                        "text": "[" + line_match.group(3) + "] " + line_match.group(4)
                    }
                }
                parsed_lines.append(line_data)
                testcase = ET.SubElement(testsuite, "testcase", name=line_data['filename'])
                ET.SubElement(
                    testcase,
                    "failure",
                    file=line_data['filename'],
                    line=str(line_data['line']),
                    message=line_data['error']['text'],
                    type="Ansible Lint"
                ).text = line_data['error']['text']

    tree = ET.ElementTree(testsuites)
    tmp_file = 'tmp_'+options.output_file
    tree.write(tmp_file, encoding='utf8', method='xml')
    parsed_lines_xml = ET.tostring(testsuites, encoding='utf8', method='xml')

    # XSLT
    urllib.request.urlretrieve(nunit_xsl_url, nunit_xsl_file)
    dom = LET.parse(tmp_file)
    xslt = LET.parse(nunit_xsl_file)
    transform = LET.XSLT(xslt)
    newdom = transform(dom)
    parsed_lines_xml = LET.tostring(newdom, pretty_print=True)
    newdom.write(options.output_file, encoding='utf-8', xml_declaration=True, pretty_print=True)

    os.remove(tmp_file)
    os.remove(nunit_xsl_file)

    if options.verbose:
        print(parsed_lines_xml)
