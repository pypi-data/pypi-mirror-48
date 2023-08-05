#------------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation.
# All rights reserved.
#
# This code is licensed under the MIT License.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files(the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and / or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions :
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
#------------------------------------------------------------------------------

try:
    from xml.etree import cElementTree as ET
except ImportError:
    from xml.etree import ElementTree as ET
import re

from .mex import Mex


SAML_TOKEN_TYPE_V1 = 'urn:oasis:names:tc:SAML:1.0:assertion'
SAML_TOKEN_TYPE_V2 = 'urn:oasis:names:tc:SAML:2.0:assertion'

# http://docs.oasis-open.org/wss-m/wss/v1.1.1/os/wss-SAMLTokenProfile-v1.1.1-os.html#_Toc307397288
WSS_SAML_TOKEN_PROFILE_V1_1 = "http://docs.oasis-open.org/wss/oasis-wss-saml-token-profile-1.1#SAMLV1.1"
WSS_SAML_TOKEN_PROFILE_V2 = "http://docs.oasis-open.org/wss/oasis-wss-saml-token-profile-1.1#SAMLV2.0"

def parse_response(body):  # Returns {"token": "<saml:assertion ...>", "type": "..."}
    token = parse_token_by_re(body)
    if token:
        return token
    error = parse_error(body)
    raise RuntimeError("WsTrust server returned error in RSTR: %s" % (error or body))

def parse_error(body):  # Returns error as a dict. See unit test case for an example.
    dom = ET.fromstring(body)
    reason_text_node = dom.find('s:Body/s:Fault/s:Reason/s:Text', Mex.NS)
    subcode_value_node = dom.find('s:Body/s:Fault/s:Code/s:Subcode/s:Value', Mex.NS)
    if reason_text_node is not None or subcode_value_node is not None:
        return {"reason": reason_text_node.text, "code": subcode_value_node.text}

def findall_content(xml_string, tag):
    """
    Given a tag name without any prefix,
    this function returns a list of the raw content inside this tag as-is.

    >>> findall_content("<ns0:foo> what <bar> ever </bar> content </ns0:foo>", "foo")
    [" what <bar> ever </bar> content "]

    Motivation:

    Usually we would use XML parser to extract the data by xpath.
    However the ElementTree in Python will implicitly normalize the output
    by "hoisting" the inner inline namespaces into the outmost element.
    The result will be a semantically equivalent XML snippet,
    but not fully identical to the original one.
    While this effect shouldn't become a problem in all other cases,
    it does not seem to fully comply with Exclusive XML Canonicalization spec
    (https://www.w3.org/TR/xml-exc-c14n/), and void the SAML token signature.
    SAML signature algo needs the "XML -> C14N(XML) -> Signed(C14N(Xml))" order.

    The binary extention lxml is probably the canonical way to solve this
    (https://stackoverflow.com/questions/22959577/python-exclusive-xml-canonicalization-xml-exc-c14n)
    but here we use this workaround, based on Regex, to return raw content as-is.
    """
    # \w+ is good enough for https://www.w3.org/TR/REC-xml/#NT-NameChar
    pattern = r"<(?:\w+:)?%(tag)s(?:[^>]*)>(.*)</(?:\w+:)?%(tag)s" % {"tag": tag}
    return re.findall(pattern, xml_string, re.DOTALL)

def parse_token_by_re(raw_response):  # Returns the saml:assertion
    for rstr in findall_content(raw_response, "RequestSecurityTokenResponse"):
        token_types = findall_content(rstr, "TokenType")
        tokens = findall_content(rstr, "RequestedSecurityToken")
        if token_types and tokens:
            return {"token": tokens[0].encode('us-ascii'), "type": token_types[0]}

