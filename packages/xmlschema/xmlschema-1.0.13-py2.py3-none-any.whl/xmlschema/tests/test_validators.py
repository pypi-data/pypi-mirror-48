#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c), 2016-2019, SISSA (International School for Advanced Studies).
# All rights reserved.
# This file is distributed under the terms of the MIT License.
# See the file 'LICENSE' in the root directory of the present
# distribution, or http://opensource.org/licenses/MIT.
#
# @author Davide Brunato <brunato@sissa.it>
#
"""
This module runs tests concerning the validation/decoding/encoding of XML files.
"""
import unittest
import pdb
import os
import sys
import pickle
from decimal import Decimal
import base64
import warnings
from elementpath import datatypes

import xmlschema
from xmlschema import (
    XMLSchemaEncodeError, XMLSchemaValidationError, ParkerConverter,
    BadgerFishConverter, AbderaConverter, JsonMLConverter
)
from xmlschema.compat import unicode_type, ordered_dict_class
from xmlschema.etree import etree_element, etree_tostring, is_etree_element, ElementTree, \
    etree_elements_assert_equal, lxml_etree, lxml_etree_element
from xmlschema.helpers import local_name
from xmlschema.qnames import XSI_TYPE
from xmlschema.resources import fetch_namespaces
from xmlschema.tests import XMLSchemaTestCase, tests_factory
from xmlschema.validators import XMLSchema11

_VEHICLES_DICT = {
    '@xmlns:vh': 'http://example.com/vehicles',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@xsi:schemaLocation': 'http://example.com/vehicles vehicles.xsd',
    'vh:cars': {
        'vh:car': [
            {'@make': 'Porsche', '@model': '911'},
            {'@make': 'Porsche', '@model': '911'}
        ]},
    'vh:bikes': {
        'vh:bike': [
            {'@make': 'Harley-Davidson', '@model': 'WL'},
            {'@make': 'Yamaha', '@model': 'XS650'}
        ]}
}

_VEHICLES_DICT_ALT = [
    {'vh:cars': [
        {'vh:car': None, '@make': 'Porsche', '@model': '911'},
        {'vh:car': None, '@make': 'Porsche', '@model': '911'}
    ]},
    {'vh:bikes': [
        {'vh:bike': None, '@make': 'Harley-Davidson', '@model': 'WL'},
        {'vh:bike': None, '@make': 'Yamaha', '@model': 'XS650'}
    ]},
    {'@xsi:schemaLocation': 'http://example.com/vehicles vehicles.xsd'}
]

_COLLECTION_DICT = {
    '@xmlns:col': 'http://example.com/ns/collection',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@xsi:schemaLocation': 'http://example.com/ns/collection collection.xsd',
    'object': [{
        '@available': True,
        '@id': 'b0836217462',
        'author': {
            '@id': 'PAR',
            'born': '1841-02-25',
            'dead': '1919-12-03',
            'name': 'Pierre-Auguste Renoir',
            'qualification': 'painter'
        },
        'estimation': Decimal('10000.00'),
        'position': 1,
        'title': 'The Umbrellas',
        'year': '1886'},
        {
            '@available': True,
            '@id': 'b0836217463',
            'author': {
                '@id': 'JM',
                'born': '1893-04-20',
                'dead': '1983-12-25',
                'name': u'Joan Miró',
                'qualification': 'painter, sculptor and ceramicist'
            },
            'position': 2,
            'title': None,
            'year': '1925'
    }]
}

_COLLECTION_PARKER = {
    'object': [{'author': {'born': '1841-02-25',
                           'dead': '1919-12-03',
                           'name': 'Pierre-Auguste Renoir',
                           'qualification': 'painter'},
                'estimation': 10000.0,
                'position': 1,
                'title': 'The Umbrellas',
                'year': '1886'},
               {'author': {'born': '1893-04-20',
                           'dead': '1983-12-25',
                           'name': u'Joan Miró',
                           'qualification': 'painter, sculptor and ceramicist'},
                'position': 2,
                'title': None,
                'year': '1925'}]}

_COLLECTION_PARKER_ROOT = {
    'col:collection': {'object': [{'author': {'born': '1841-02-25',
                                              'dead': '1919-12-03',
                                              'name': 'Pierre-Auguste Renoir',
                                              'qualification': 'painter'},
                                   'estimation': 10000.0,
                                   'position': 1,
                                   'title': 'The Umbrellas',
                                   'year': '1886'},
                                  {'author': {'born': '1893-04-20',
                                              'dead': '1983-12-25',
                                              'name': u'Joan Miró',
                                              'qualification': 'painter, sculptor and ceramicist'},
                                   'position': 2,
                                   'title': None,
                                   'year': '1925'}]}}

_COLLECTION_BADGERFISH = {
    '@xmlns': {
        'col': 'http://example.com/ns/collection',
        'xsi': 'http://www.w3.org/2001/XMLSchema-instance'},
    'col:collection': {
        '@xsi:schemaLocation': 'http://example.com/ns/collection collection.xsd',
        'object': [{
            '@available': True,
            '@id': 'b0836217462',
            'author': {
                '@id': 'PAR',
                'born': {'$': '1841-02-25'},
                'dead': {'$': '1919-12-03'},
                'name': {'$': 'Pierre-Auguste Renoir'},
                'qualification': {'$': 'painter'}},
            'estimation': {'$': 10000.0},
            'position': {'$': 1},
            'title': {'$': 'The Umbrellas'},
            'year': {'$': '1886'}},
            {
                '@available': True,
                '@id': 'b0836217463',
                'author': {
                    '@id': 'JM',
                    'born': {'$': '1893-04-20'},
                    'dead': {'$': '1983-12-25'},
                    'name': {'$': u'Joan Miró'},
                    'qualification': {
                        '$': 'painter, sculptor and ceramicist'}
                },
                'position': {'$': 2},
                'title': {},
                'year': {'$': '1925'}
        }]
    }
}

_COLLECTION_ABDERA = {
    'attributes': {
        'xsi:schemaLocation': 'http://example.com/ns/collection collection.xsd'
    },
    'children': [
        {
            'object': [
                {
                    'attributes': {'available': True, 'id': 'b0836217462'},
                    'children': [{
                        'author': {
                            'attributes': {'id': 'PAR'},
                            'children': [{
                                'born': '1841-02-25',
                                'dead': '1919-12-03',
                                'name': 'Pierre-Auguste Renoir',
                                'qualification': 'painter'}
                            ]},
                        'estimation': 10000.0,
                        'position': 1,
                        'title': 'The Umbrellas',
                        'year': '1886'}
                    ]},
                {
                    'attributes': {'available': True, 'id': 'b0836217463'},
                    'children': [{
                        'author': {
                            'attributes': {'id': 'JM'},
                            'children': [{
                                'born': '1893-04-20',
                                'dead': '1983-12-25',
                                'name': u'Joan Miró',
                                'qualification': 'painter, sculptor and ceramicist'}
                            ]},
                        'position': 2,
                        'title': [],
                        'year': '1925'
                    }]
                }]
        }
    ]}

_COLLECTION_JSON_ML = [
    'col:collection',
    {'xmlns:col': 'http://example.com/ns/collection',
     'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
     'xsi:schemaLocation': 'http://example.com/ns/collection collection.xsd'},
    ['object',
     {'available': True, 'id': 'b0836217462'},
     ['position', 1],
     ['title', 'The Umbrellas'],
     ['year', '1886'],
     [
         'author',
         {'id': 'PAR'},
         ['name', 'Pierre-Auguste Renoir'],
         ['born', '1841-02-25'],
         ['dead', '1919-12-03'],
         ['qualification', 'painter']
     ],
     [
         'estimation',
         Decimal('10000.00')
     ]],
    ['object',
     {'available': True, 'id': 'b0836217463'},
     ['position', 2],
     ['title'],
     ['year', '1925'],
     [
         'author',
         {'id': 'JM'},
         ['name', u'Joan Miró'],
         ['born', '1893-04-20'],
         ['dead', '1983-12-25'],
         ['qualification', 'painter, sculptor and ceramicist']
     ]]
]

_DATA_DICT = {
    '@xmlns:ns': 'ns',
    '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
    '@xsi:schemaLocation': 'ns ./simple-types.xsd',
    'certification': [
        {'$': 'ISO-9001', '@Year': 1999},
        {'$': 'ISO-27001', '@Year': 2009}
    ],
    'decimal_value': [Decimal('1')],
    u'menù': u'baccalà mantecato',
    u'complex_boolean': [
        {'$': True, '@Type': 2}, {'$': False, '@Type': 1}, True, False
    ],
    u'simple_boolean': [True, False]
}


def iter_nested_items(items, dict_class=dict, list_class=list):
    if isinstance(items, dict_class):
        for k, v in items.items():
            for value in iter_nested_items(v, dict_class, list_class):
                yield value
    elif isinstance(items, list_class):
        for item in items:
            for value in iter_nested_items(item, dict_class, list_class):
                yield value
    elif isinstance(items, dict):
        raise TypeError("%r: is a dict() instead of %r." % (items, dict_class))
    elif isinstance(items, list):
        raise TypeError("%r: is a list() instead of %r." % (items, list_class))
    else:
        yield items


def make_validator_test_class(test_file, test_args, test_num, schema_class, check_with_lxml):
    """
    Creates a validator test class.

    :param test_file: the XML test file path.
    :param test_args: line arguments for test case.
    :param test_num: a positive integer number associated with the test case.
    :param schema_class: the schema class to use.
    :param check_with_lxml: if `True` compare with lxml XMLSchema class, reporting anomalies. \
    Works only for XSD 1.0 tests.
    """
    xml_file = os.path.relpath(test_file)
    msg_tmpl = "\n\n{}: %s.".format(xml_file)

    # Extract schema test arguments
    expected_errors = test_args.errors
    expected_warnings = test_args.warnings
    inspect = test_args.inspect
    locations = test_args.locations
    defuse = test_args.defuse
    skip_strict = test_args.skip
    debug_mode = test_args.debug

    class TestValidator(XMLSchemaTestCase):

        @classmethod
        def setUpClass(cls):
            # Builds schema instance using 'lax' validation mode to accepts also schemas with not crashing errors.
            cls.schema_class = schema_class
            source, _locations = xmlschema.fetch_schema_locations(xml_file, locations)
            cls.schema = schema_class(source, validation='lax', locations=_locations, defuse=defuse)
            if check_with_lxml and lxml_etree is not None:
                cls.lxml_schema = lxml_etree.parse(source)

            cls.errors = []
            cls.chunks = []
            cls.longMessage = True

            if debug_mode:
                print("\n##\n## Testing %r validation in debug mode.\n##" % xml_file)
                pdb.set_trace()

        def check_etree_encode(self, root, converter=None, **kwargs):
            data1 = self.schema.decode(root, converter=converter, **kwargs)
            if isinstance(data1, tuple):
                data1 = data1[0]  # When validation='lax'

            for _ in iter_nested_items(data1, dict_class=ordered_dict_class):
                pass

            elem1 = self.schema.encode(data1, path=root.tag, converter=converter, **kwargs)
            if isinstance(elem1, tuple):
                # When validation='lax'
                if converter is not ParkerConverter:
                    for e in elem1[1]:
                        self.check_namespace_prefixes(unicode_type(e))
                elem1 = elem1[0]

            # Checks the encoded element to not contains reserved namespace prefixes
            if 'namespaces' in kwargs and all('ns%d' % k not in kwargs['namespaces'] for k in range(10)):
                self.check_namespace_prefixes(etree_tostring(elem1, namespaces=kwargs['namespaces']))

            # Main check: compare original a re encoded tree
            try:
                etree_elements_assert_equal(root, elem1, strict=False)
            except AssertionError as err:
                # If the check fails retry only if the converter is lossy (eg. ParkerConverter)
                # or if the XML case has defaults taken from the schema or some part of data
                # decoding is skipped by schema wildcards (set the specific argument in testfiles).
                if converter not in (ParkerConverter, AbderaConverter, JsonMLConverter) and not skip_strict:
                    if debug_mode:
                        pdb.set_trace()
                    raise AssertionError(str(err) + msg_tmpl % "encoded tree differs from original")
                elif converter is ParkerConverter and any(XSI_TYPE in e.attrib for e in root.iter()):
                    return  # can't check encode equivalence if xsi:type is provided
                else:
                    # Lossy or augmenting cases are checked after a re decoding-encoding pass
                    data2 = self.schema.decode(elem1, converter=converter, **kwargs)
                    if isinstance(data2, tuple):
                        data2 = data2[0]

                    if sys.version_info >= (3, 6):
                        # For Python < 3.6 cannot ensure attribute decoding order
                        try:
                            self.assertEqual(data1, data2, msg_tmpl % "re decoded data changed")
                        except AssertionError:
                            if debug_mode:
                                pdb.set_trace()
                            raise

                    elem2 = self.schema.encode(data2, path=root.tag, converter=converter, **kwargs)
                    if isinstance(elem2, tuple):
                        elem2 = elem2[0]

                    try:
                        etree_elements_assert_equal(elem1, elem2, strict=False)
                    except AssertionError as err:
                        if debug_mode:
                            pdb.set_trace()
                        raise AssertionError(str(err) + msg_tmpl % "encoded tree differs after second pass")

        def check_json_serialization(self, root, converter=None, **kwargs):
            data1 = xmlschema.to_json(root, schema=self.schema, converter=converter, **kwargs)
            if isinstance(data1, tuple):
                data1 = data1[0]

            elem1 = xmlschema.from_json(data1, schema=self.schema, path=root.tag, converter=converter, **kwargs)
            if isinstance(elem1, tuple):
                elem1 = elem1[0]

            data2 = xmlschema.to_json(elem1, schema=self.schema, converter=converter, **kwargs)
            if isinstance(data2, tuple):
                data2 = data2[0]

            if converter is ParkerConverter and any(XSI_TYPE in e.attrib for e in root.iter()):
                return  # can't check encode equivalence if xsi:type is provided
            elif sys.version_info >= (3, 6):
                self.assertEqual(data2, data1, msg_tmpl % "serialized data changed at second pass")
            else:
                elem2 = xmlschema.from_json(data2, schema=self.schema, path=root.tag, converter=converter, **kwargs)
                if isinstance(elem2, tuple):
                    elem2 = elem2[0]
                try:
                    self.assertIsNone(etree_elements_assert_equal(elem1, elem2, strict=False, skip_comments=True))
                except AssertionError as err:
                    self.assertIsNone(err, None)

        def check_decoding_with_element_tree(self):
            del self.errors[:]
            del self.chunks[:]

            def do_decoding():
                for obj in self.schema.iter_decode(xml_file):
                    if isinstance(obj, (xmlschema.XMLSchemaDecodeError, xmlschema.XMLSchemaValidationError)):
                        self.errors.append(obj)
                    else:
                        self.chunks.append(obj)

            if expected_warnings == 0:
                do_decoding()
            else:
                with warnings.catch_warnings(record=True) as ctx:
                    warnings.simplefilter("always")
                    do_decoding()
                    self.assertEqual(len(ctx), expected_warnings, "Wrong number of include/import warnings")

            self.check_errors(xml_file, expected_errors)

            if not self.chunks:
                raise ValueError("No decoded object returned!!")
            elif len(self.chunks) > 1:
                raise ValueError("Too many ({}) decoded objects returned: {}".format(len(self.chunks), self.chunks))
            elif not isinstance(self.chunks[0], dict):
                raise ValueError("Decoded object is not a dictionary: {}".format(self.chunks))
            else:
                self.assertTrue(True, "Successfully test decoding for {}".format(xml_file))

        def check_schema_serialization(self):
            # Repeat with serialized-deserialized schema (only for Python 3)
            serialized_schema = pickle.dumps(self.schema)
            deserialized_schema = pickle.loads(serialized_schema)
            errors = []
            chunks = []
            for obj in deserialized_schema.iter_decode(xml_file):
                if isinstance(obj, xmlschema.XMLSchemaValidationError):
                    errors.append(obj)
                else:
                    chunks.append(obj)

            self.assertEqual(len(errors), len(self.errors), msg_tmpl % "wrong number errors")
            self.assertEqual(chunks, self.chunks, msg_tmpl % "decoded data differ")

        def check_decode_api(self):
            # Compare with the decode API and other validation modes
            strict_data = self.schema.decode(xml_file)
            lax_data = self.schema.decode(xml_file, validation='lax')
            skip_data = self.schema.decode(xml_file, validation='skip')
            self.assertEqual(strict_data, self.chunks[0], msg_tmpl % "decode() API has a different result")
            self.assertEqual(lax_data[0], self.chunks[0], msg_tmpl % "'lax' validation has a different result")
            self.assertEqual(skip_data, self.chunks[0], msg_tmpl % "'skip' validation has a different result")

        def check_encoding_with_element_tree(self):
            root = ElementTree.parse(xml_file).getroot()
            namespaces = fetch_namespaces(xml_file)
            options = {'namespaces': namespaces, 'dict_class': ordered_dict_class}

            self.check_etree_encode(root, cdata_prefix='#', **options)  # Default converter
            self.check_etree_encode(root, ParkerConverter, validation='lax', **options)
            self.check_etree_encode(root, ParkerConverter, validation='skip', **options)
            self.check_etree_encode(root, BadgerFishConverter, **options)
            self.check_etree_encode(root, AbderaConverter, **options)
            self.check_etree_encode(root, JsonMLConverter, **options)

            options.pop('dict_class')
            self.check_json_serialization(root, cdata_prefix='#', **options)
            self.check_json_serialization(root, ParkerConverter, validation='lax', **options)
            self.check_json_serialization(root, ParkerConverter, validation='skip', **options)
            self.check_json_serialization(root, BadgerFishConverter, **options)
            self.check_json_serialization(root, AbderaConverter, **options)
            self.check_json_serialization(root, JsonMLConverter, **options)

        def check_decoding_and_encoding_with_lxml(self):
            xml_tree = lxml_etree.parse(xml_file)
            namespaces = fetch_namespaces(xml_file)
            errors = []
            chunks = []
            for obj in self.schema.iter_decode(xml_tree, namespaces=namespaces):
                if isinstance(obj, xmlschema.XMLSchemaValidationError):
                    errors.append(obj)
                else:
                    chunks.append(obj)

            self.assertEqual(chunks, self.chunks, msg_tmpl % "decode data change with lxml")
            self.assertEqual(len(errors), len(self.errors), msg_tmpl % "errors number change with lxml")

            if not errors:
                root = xml_tree.getroot()
                options = {
                    'etree_element_class': lxml_etree_element,
                    'namespaces': namespaces,
                    'dict_class': ordered_dict_class,
                }

                self.check_etree_encode(root, cdata_prefix='#', **options)  # Default converter
                self.check_etree_encode(root, ParkerConverter, validation='lax', **options)
                self.check_etree_encode(root, ParkerConverter, validation='skip', **options)
                self.check_etree_encode(root, BadgerFishConverter, **options)
                self.check_etree_encode(root, AbderaConverter, **options)
                self.check_etree_encode(root, JsonMLConverter, **options)

                options.pop('dict_class')
                self.check_json_serialization(root, cdata_prefix='#', **options)
                self.check_json_serialization(root, ParkerConverter, validation='lax', **options)
                self.check_json_serialization(root, ParkerConverter, validation='skip', **options)
                self.check_json_serialization(root, BadgerFishConverter, **options)
                self.check_json_serialization(root, AbderaConverter, **options)
                self.check_json_serialization(root, JsonMLConverter, **options)

        def check_validate_and_is_valid_api(self):
            if expected_errors:
                self.assertFalse(self.schema.is_valid(xml_file), msg_tmpl % "file with errors is valid")
                self.assertRaises(XMLSchemaValidationError, self.schema.validate, xml_file)
            else:
                self.assertTrue(self.schema.is_valid(xml_file), msg_tmpl % "file without errors is not valid")
                self.assertEqual(self.schema.validate(xml_file), None,
                                 msg_tmpl % "file without errors not validated")

        def check_iter_errors(self):
            self.assertEqual(len(list(self.schema.iter_errors(xml_file))), expected_errors,
                             msg_tmpl % "wrong number of errors (%d expected)" % expected_errors)

        def check_lxml_validation(self):
            try:
                schema = lxml_etree.XMLSchema(self.lxml_schema.getroot())
            except lxml_etree.XMLSchemaParseError:
                print("\nSkip lxml.etree.XMLSchema validation test for {!r} ({})".
                      format(xml_file, TestValidator.__name__, ))
            else:
                xml_tree = lxml_etree.parse(xml_file)
                if self.errors:
                    self.assertFalse(schema.validate(xml_tree))
                else:
                    self.assertTrue(schema.validate(xml_tree))

        def test_xml_document_validation(self):
            self.check_decoding_with_element_tree()

            if not inspect and sys.version_info >= (3,):
                self.check_schema_serialization()

            if not self.errors:
                self.check_encoding_with_element_tree()

            if lxml_etree is not None:
                self.check_decoding_and_encoding_with_lxml()

            self.check_iter_errors()
            self.check_validate_and_is_valid_api()
            if check_with_lxml and lxml_etree is not None:
                self.check_lxml_validation()

    TestValidator.__name__ = TestValidator.__qualname__ = 'TestValidator{0:03}'.format(test_num)
    return TestValidator


class TestValidation(XMLSchemaTestCase):

    def check_validity(self, xsd_component, data, expected, use_defaults=True):
        if isinstance(expected, type) and issubclass(expected, Exception):
            self.assertRaises(expected, xsd_component.is_valid, data, use_defaults=use_defaults)
        elif expected:
            self.assertTrue(xsd_component.is_valid(data, use_defaults=use_defaults))
        else:
            self.assertFalse(xsd_component.is_valid(data, use_defaults=use_defaults))

    @unittest.skipIf(lxml_etree is None, "The lxml library is not available.")
    def test_lxml(self):
        xs = xmlschema.XMLSchema(self.casepath('examples/vehicles/vehicles.xsd'))
        xt1 = lxml_etree.parse(self.casepath('examples/vehicles/vehicles.xml'))
        xt2 = lxml_etree.parse(self.casepath('examples/vehicles/vehicles-1_error.xml'))
        self.assertTrue(xs.is_valid(xt1))
        self.assertFalse(xs.is_valid(xt2))
        self.assertTrue(xs.validate(xt1) is None)
        self.assertRaises(xmlschema.XMLSchemaValidationError, xs.validate, xt2)

    def test_issue_064(self):
        self.check_validity(self.st_schema, '<name xmlns="ns"></name>', False)

    def test_document_validate_api(self):
        self.assertIsNone(xmlschema.validate(self.vh_xml_file))
        self.assertIsNone(xmlschema.validate(self.vh_xml_file, use_defaults=False))

        vh_2_file = self.casepath('examples/vehicles/vehicles-2_errors.xml')
        self.assertRaises(XMLSchemaValidationError, xmlschema.validate, vh_2_file)

        try:
            xmlschema.validate(vh_2_file, namespaces={'vhx': "http://example.com/vehicles"})
        except XMLSchemaValidationError as err:
            path_line = str(err).splitlines()[-1]
        else:
            path_line = ''
        self.assertEqual('Path: /vhx:vehicles/vhx:cars', path_line)

        # Issue #80
        vh_2_xt = ElementTree.parse(vh_2_file)
        self.assertRaises(XMLSchemaValidationError, xmlschema.validate, vh_2_xt, self.vh_xsd_file)

    def _test_document_validate_api_lazy(self):
        source = xmlschema.XMLResource(self.col_xml_file, lazy=True)
        source.root[0].clear()
        source.root[1].clear()
        xsd_element = self.col_schema.elements['collection']

        for result in xsd_element.iter_decode(source.root, 'strict', namespaces=source.get_namespaces(),
                                              source=source, _no_deep=None):
            del result

        self.assertIsNone(xmlschema.validate(self.col_xml_file, lazy=True))


class TestValidation11(TestValidation):
    schema_class = XMLSchema11

    def test_default_attributes(self):
        """<?xml version="1.0" encoding="UTF-8"?>
                <ns:node xmlns:ns="ns" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
                xsi:schemaLocation="ns ./default_attributes.xsd" colour="red">Root Node</ns:node>
        """
        xs = self.schema_class(self.casepath('features/attributes/default_attributes.xsd'))
        self.assertTrue(xs.is_valid("<tree xmlns='ns'>"
                                    "   <node node-id='1'>alpha</node>"
                                    "   <node node-id='2' colour='red'>beta</node>"
                                    "</tree>"))
        self.assertFalse(xs.is_valid("<tree xmlns='ns'>"
                                     "   <node>alpha</node>"  # Misses required attribute
                                     "   <node node-id='2' colour='red'>beta</node>"
                                     "</tree>"))


class TestDecoding(XMLSchemaTestCase):

    def check_decode(self, xsd_component, data, expected, **kwargs):
        if isinstance(expected, type) and issubclass(expected, Exception):
            self.assertRaises(expected, xsd_component.decode, data, **kwargs)
        else:
            obj = xsd_component.decode(data, **kwargs)
            if isinstance(obj, tuple) and len(obj) == 2 and isinstance(obj[1], list) \
                    and isinstance(obj[1][0], Exception):
                self.assertEqual(expected, obj[0])
                self.assertTrue(isinstance(obj[0], type(expected)))
            else:
                self.assertEqual(expected, obj)
                self.assertTrue(isinstance(obj, type(expected)))

    @unittest.skipIf(lxml_etree is None, "The lxml library is not available.")
    def test_lxml(self):
        vh_xml_tree = lxml_etree.parse(self.vh_xml_file)
        self.assertEqual(self.vh_schema.to_dict(vh_xml_tree), _VEHICLES_DICT)
        self.assertEqual(xmlschema.to_dict(vh_xml_tree, self.vh_schema.url), _VEHICLES_DICT)

    def test_to_dict_from_etree(self):
        vh_xml_tree = ElementTree.parse(self.vh_xml_file)
        col_xml_tree = ElementTree.parse(self.col_xml_file)

        xml_dict = self.vh_schema.to_dict(vh_xml_tree)
        self.assertNotEqual(xml_dict, _VEHICLES_DICT)

        xml_dict = self.vh_schema.to_dict(vh_xml_tree, namespaces=self.vh_namespaces)
        self.assertEqual(xml_dict, _VEHICLES_DICT)

        xml_dict = xmlschema.to_dict(vh_xml_tree, self.vh_schema.url, namespaces=self.vh_namespaces)
        self.assertEqual(xml_dict, _VEHICLES_DICT)

        xml_dict = self.col_schema.to_dict(col_xml_tree)
        self.assertNotEqual(xml_dict, _COLLECTION_DICT)

        xml_dict = self.col_schema.to_dict(col_xml_tree, namespaces=self.col_namespaces)
        self.assertEqual(xml_dict, _COLLECTION_DICT)

        xml_dict = xmlschema.to_dict(col_xml_tree, self.col_schema.url, namespaces=self.col_namespaces)
        self.assertEqual(xml_dict, _COLLECTION_DICT)

    def test_to_dict_from_string(self):
        with open(self.vh_xml_file) as f:
            vh_xml_string = f.read()

        with open(self.col_xml_file) as f:
            col_xml_string = f.read()

        xml_dict = self.vh_schema.to_dict(vh_xml_string, namespaces=self.vh_namespaces)
        self.assertEqual(xml_dict, _VEHICLES_DICT)

        xml_dict = xmlschema.to_dict(vh_xml_string, self.vh_schema.url, namespaces=self.vh_namespaces)
        self.assertEqual(xml_dict, _VEHICLES_DICT)

        xml_dict = self.col_schema.to_dict(col_xml_string, namespaces=self.col_namespaces)
        self.assertTrue(xml_dict, _COLLECTION_DICT)

        xml_dict = xmlschema.to_dict(col_xml_string, self.col_schema.url, namespaces=self.col_namespaces)
        self.assertTrue(xml_dict, _COLLECTION_DICT)

    def test_json_dump_and_load(self):
        vh_xml_tree = ElementTree.parse(self.vh_xml_file)
        col_xml_tree = ElementTree.parse(self.col_xml_file)
        with open(self.vh_json_file, 'w') as f:
            xmlschema.to_json(self.vh_xml_file, f)

        with open(self.vh_json_file) as f:
            root = xmlschema.from_json(f, self.vh_schema)

        os.remove(self.vh_json_file)
        self.check_etree_elements(vh_xml_tree, root)

        with open(self.col_json_file, 'w') as f:
            xmlschema.to_json(self.col_xml_file, f)

        with open(self.col_json_file) as f:
            root = xmlschema.from_json(f, self.col_schema)

        os.remove(self.col_json_file)
        self.check_etree_elements(col_xml_tree, root)

    def test_path(self):
        xt = ElementTree.parse(self.vh_xml_file)
        xd = self.vh_schema.to_dict(xt, '/vh:vehicles/vh:cars', namespaces=self.vh_namespaces)
        self.assertEqual(xd['vh:car'], _VEHICLES_DICT['vh:cars']['vh:car'])
        xd = self.vh_schema.to_dict(xt, '/vh:vehicles/vh:bikes', namespaces=self.vh_namespaces)
        self.assertEqual(xd['vh:bike'], _VEHICLES_DICT['vh:bikes']['vh:bike'])

    def test_validation_strict(self):
        self.assertRaises(
            xmlschema.XMLSchemaValidationError,
            self.vh_schema.to_dict,
            ElementTree.parse(self.casepath('examples/vehicles/vehicles-2_errors.xml')),
            validation='strict',
            namespaces=self.vh_namespaces
        )

    def test_validation_skip(self):
        xt = ElementTree.parse(self.casepath('features/decoder/data3.xml'))
        xd = self.st_schema.decode(xt, validation='skip', namespaces={'ns': 'ns'})
        self.assertEqual(xd['decimal_value'], ['abc'])

    def test_datatypes(self):
        xt = ElementTree.parse(self.casepath('features/decoder/data.xml'))
        xd = self.st_schema.to_dict(xt, namespaces=self.default_namespaces)
        self.assertEqual(xd, _DATA_DICT)

    def test_datetime_types(self):
        xs = self.get_schema('<element name="dt" type="dateTime"/>')
        self.assertEqual(xs.decode('<ns:dt xmlns:ns="ns">2019-01-01T13:40:00</ns:dt>'), '2019-01-01T13:40:00')
        self.assertEqual(xs.decode('<ns:dt xmlns:ns="ns">2019-01-01T13:40:00</ns:dt>', datetime_types=True),
                         datatypes.DateTime10.fromstring('2019-01-01T13:40:00'))

        xs = self.get_schema('<element name="dt" type="date"/>')
        self.assertEqual(xs.decode('<ns:dt xmlns:ns="ns">2001-04-15</ns:dt>'), '2001-04-15')
        self.assertEqual(xs.decode('<ns:dt xmlns:ns="ns">2001-04-15</ns:dt>', datetime_types=True),
                         datatypes.Date10.fromstring('2001-04-15'))

    def test_duration_type(self):
        xs = self.get_schema('<element name="td" type="duration"/>')
        self.assertEqual(xs.decode('<ns:td xmlns:ns="ns">P5Y3MT60H30.001S</ns:td>'), 'P5Y3MT60H30.001S')
        self.assertEqual(xs.decode('<ns:td xmlns:ns="ns">P5Y3MT60H30.001S</ns:td>', datetime_types=True),
                         datatypes.Duration.fromstring('P5Y3M2DT12H30.001S'))

    def test_default_converter(self):
        self.assertEqual(self.col_schema.to_dict(self.col_xml_file), _COLLECTION_DICT)

        default_dict = self.col_schema.to_dict(self.col_xml_file, converter=xmlschema.XMLSchemaConverter)
        self.assertEqual(default_dict, _COLLECTION_DICT)

        default_dict_root = self.col_schema.to_dict(self.col_xml_file, preserve_root=True)
        self.assertEqual(default_dict_root, {'col:collection': _COLLECTION_DICT})

    def test_parker_converter(self):
        parker_dict = self.col_schema.to_dict(self.col_xml_file, converter=xmlschema.ParkerConverter)
        self.assertEqual(parker_dict, _COLLECTION_PARKER)

        parker_dict_root = self.col_schema.to_dict(
            self.col_xml_file, converter=xmlschema.ParkerConverter(preserve_root=True), decimal_type=float)
        self.assertEqual(parker_dict_root, _COLLECTION_PARKER_ROOT)

    def test_badgerfish_converter(self):
        badgerfish_dict = self.col_schema.to_dict(
            self.col_xml_file, converter=xmlschema.BadgerFishConverter, decimal_type=float)
        self.assertEqual(badgerfish_dict, _COLLECTION_BADGERFISH)

    def test_abdera_converter(self):
        abdera_dict = self.col_schema.to_dict(
            self.col_xml_file, converter=xmlschema.AbderaConverter, decimal_type=float, dict_class=dict)
        self.assertEqual(abdera_dict, _COLLECTION_ABDERA)

    def test_json_ml_converter(self):
        json_ml_dict = self.col_schema.to_dict(self.col_xml_file, converter=xmlschema.JsonMLConverter)
        self.assertEqual(json_ml_dict, _COLLECTION_JSON_ML)

    def test_dict_granularity(self):
        """Based on Issue #22, test to make sure an xsd indicating list with
        dictionaries, returns just that even when it has a single dict. """
        xsd_string = self.casepath('issues/issue_022/xsd_string.xsd')
        xml_string_1 = self.casepath('issues/issue_022/xml_string_1.xml')
        xml_string_2 = self.casepath('issues/issue_022/xml_string_2.xml')
        xsd_schema = xmlschema.XMLSchema(xsd_string)
        xml_data_1 = xsd_schema.to_dict(xml_string_1)
        xml_data_2 = xsd_schema.to_dict(xml_string_2)
        self.assertTrue(isinstance(xml_data_1['bar'], type(xml_data_2['bar'])),
                        msg="XSD with an array that return a single element from xml must still yield a list.")

    def test_any_type(self):
        any_type = xmlschema.XMLSchema.meta_schema.types['anyType']
        xml_data_1 = ElementTree.Element('dummy')
        self.assertEqual(any_type.decode(xml_data_1), (None, [], []))
        xml_data_2 = ElementTree.fromstring('<root>\n    <child_1/>\n    <child_2/>\n</root>')
        self.assertEqual(any_type.decode(xml_data_2), (None, [], []))  # Currently no decoding yet

    def test_choice_model_decoding(self):
        schema = xmlschema.XMLSchema(self.casepath('issues/issue_041/issue_041.xsd'))
        data = schema.to_dict(self.casepath('issues/issue_041/issue_041.xml'))
        self.assertEqual(data, {
            '@xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
            '@xsi:noNamespaceSchemaLocation': 'issue_041.xsd',
            'Name': 'SomeNameValueThingy',
            'Value': {'Integer': 0}
        })

    def test_cdata_decoding(self):
        schema = xmlschema.XMLSchema(self.casepath('issues/issue_046/issue_046.xsd'))
        xml_file = self.casepath('issues/issue_046/issue_046.xml')
        self.assertEqual(
            schema.decode(xml_file, dict_class=ordered_dict_class, cdata_prefix='#'),
            ordered_dict_class(
                [('@xmlns:xsi', 'http://www.w3.org/2001/XMLSchema-instance'),
                 ('@xsi:noNamespaceSchemaLocation', 'issue_046.xsd'),
                 ('#1', 'Dear Mr.'), ('name', 'John Smith'),
                 ('#2', '.\n  Your order'), ('orderid', 1032),
                 ('#3', 'will be shipped on'), ('shipdate', '2001-07-13'), ('#4', '.')]
            ))

    def test_string_facets(self):
        none_empty_string_type = self.st_schema.types['none_empty_string']
        self.check_decode(none_empty_string_type, '', XMLSchemaValidationError)
        name_type = self.st_schema.types['NameType']
        self.check_decode(name_type, '', XMLSchemaValidationError)

    def test_binary_data_facets(self):
        hex_code_type = self.st_schema.types['hexCode']
        self.check_decode(hex_code_type, u'00D7310A', u'00D7310A')

        base64_code_type = self.st_schema.types['base64Code']
        self.check_decode(base64_code_type, base64.b64encode(b'ok'), XMLSchemaValidationError)
        base64_value = base64.b64encode(b'hello')
        self.check_decode(base64_code_type, base64_value, base64_value.decode('utf-8'))
        self.check_decode(base64_code_type, base64.b64encode(b'abcefgh'), u'YWJjZWZnaA==')
        self.check_decode(base64_code_type, b' Y  W J j ZWZ\t\tn\na A= =', u'Y W J j ZWZ n a A= =')
        self.check_decode(base64_code_type, u' Y  W J j ZWZ\t\tn\na A= =', u'Y W J j ZWZ n a A= =')
        self.check_decode(base64_code_type, base64.b64encode(b'abcefghi'), u'YWJjZWZnaGk=')

        self.check_decode(base64_code_type, u'YWJjZWZnaA=', XMLSchemaValidationError)
        self.check_decode(base64_code_type, u'YWJjZWZna$==', XMLSchemaValidationError)

        base64_length4_type = self.st_schema.types['base64Length4']
        self.check_decode(base64_length4_type, base64.b64encode(b'abc'), XMLSchemaValidationError)
        self.check_decode(base64_length4_type, base64.b64encode(b'abce'), u'YWJjZQ==')
        self.check_decode(base64_length4_type, base64.b64encode(b'abcef'), XMLSchemaValidationError)

        base64_length5_type = self.st_schema.types['base64Length5']
        self.check_decode(base64_length5_type, base64.b64encode(b'1234'), XMLSchemaValidationError)
        self.check_decode(base64_length5_type, base64.b64encode(b'12345'), u'MTIzNDU=')
        self.check_decode(base64_length5_type, base64.b64encode(b'123456'), XMLSchemaValidationError)

    def test_decimal_type(self):
        schema = self.get_schema("""
        <element name="A" type="ns:A_type" />
        <simpleType name="A_type">
            <restriction base="decimal">
                <minInclusive value="100.50"/>
            </restriction>
        </simpleType>
        """)

        self.check_decode(schema, '<A xmlns="ns">120.48</A>', Decimal('120.48'))
        self.check_decode(schema, '<A xmlns="ns">100.50</A>', Decimal('100.50'), process_namespaces=False)
        self.check_decode(schema, '<A xmlns="ns">100.49</A>', XMLSchemaValidationError)
        self.check_decode(schema, '<A xmlns="ns">120.48</A>', 120.48, decimal_type=float)
        # Issue #66
        self.check_decode(schema, '<A xmlns="ns">120.48</A>', '120.48', decimal_type=str)

    def test_nillable(self):
        # Issue #76
        xsd_string = """<?xml version="1.0" encoding="UTF-8"?>
        <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" elementFormDefault="qualified">
            <xs:element name="foo" type="Foo" />
            <xs:complexType name="Foo">
                <xs:sequence minOccurs="1" maxOccurs="1">
                    <xs:element name="bar" type="xs:integer" nillable="true" />
                </xs:sequence>
            </xs:complexType>
        </xs:schema>
        """
        xsd_schema = xmlschema.XMLSchema(xsd_string)
        xml_string_1 = "<foo><bar>0</bar></foo>"
        xml_string_2 = """<?xml version="1.0" encoding="UTF-8"?>
        <foo xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
            <bar xsi:nil="true"></bar>
        </foo>
        """
        self.assertTrue(xsd_schema.is_valid(source=xml_string_1, use_defaults=False))
        self.assertTrue(xsd_schema.is_valid(source=xml_string_2, use_defaults=False))
        obj = xsd_schema.decode(xml_string_2, use_defaults=False)
        self.check_etree_elements(ElementTree.fromstring(xml_string_2), xsd_schema.encode(obj))

    def test_default_namespace(self):
        # Issue #77
        xs = xmlschema.XMLSchema("""<?xml version="1.0" encoding="UTF-8"?>
        <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" targetNamespace="http://example.com/foo">
            <xs:element name="foo" type="xs:string" />
        </xs:schema>""")
        self.assertEqual(xs.to_dict("""<foo xmlns="http://example.com/foo">bar</foo>""",
                                    path='/foo', namespaces={'': 'http://example.com/foo'}), 'bar')
        self.assertEqual(xs.to_dict("""<foo>bar</foo>""",
                                    path='/foo', namespaces={'': 'http://example.com/foo'}), None)

    def test_complex_with_simple_content_restriction(self):
        xs = self.schema_class(self.casepath('features/derivations/complex-with-simple-content-restriction.xsd'))
        self.assertTrue(xs.is_valid('<value>10</value>'))
        self.assertFalse(xs.is_valid('<value>alpha</value>'))
        self.assertEqual(xs.decode('<value>10</value>'), 10)

    def test_union_types(self):
        # For testing issue #103
        decimal_or_nan = self.st_schema.types['myType']
        self.check_decode(decimal_or_nan, '95.0', Decimal('95.0'))
        self.check_decode(decimal_or_nan, 'NaN', u'NaN')

    def test_default_values(self):
        # From issue #108
        xsd_text = """<?xml version="1.0" encoding="utf-8"?>
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
              <xs:element name="root" type="root" default="default_value"/>
              <xs:complexType name="root">
                <xs:simpleContent>
                  <xs:extension base="xs:string">
                    <xs:attribute name="attr" type="xs:string"/>
                    <xs:attribute name="attrWithDefault" type="xs:string" default="default_value"/>
                    <xs:attribute name="attrWithFixed" type="xs:string" fixed="fixed_value"/>
                  </xs:extension>
                </xs:simpleContent>
              </xs:complexType>
              <xs:element name="simple_root" type="xs:string" default="default_value"/>
            </xs:schema>"""

        schema = self.schema_class(xsd_text)
        self.assertEqual(schema.to_dict("<root>text</root>"),
                         {'@attrWithDefault': 'default_value',
                          '@attrWithFixed': 'fixed_value',
                          '$': 'text'})
        self.assertEqual(schema.to_dict("<root/>"),
                         {'@attrWithDefault': 'default_value',
                          '@attrWithFixed': 'fixed_value',
                          '$': 'default_value'})
        self.assertEqual(schema.to_dict("""<root attr="attr_value">text</root>"""),
                         {'$': 'text',
                          '@attr': 'attr_value',
                          '@attrWithDefault': 'default_value',
                          '@attrWithFixed': 'fixed_value'})

        self.assertEqual(schema.to_dict("<root>text</root>", use_defaults=False),
                         {'@attrWithFixed': 'fixed_value', '$': 'text'})
        self.assertEqual(schema.to_dict("""<root attr="attr_value">text</root>""", use_defaults=False),
                         {'$': 'text', '@attr': 'attr_value', '@attrWithFixed': 'fixed_value'})
        self.assertEqual(schema.to_dict("<root/>", use_defaults=False), {'@attrWithFixed': 'fixed_value'})

        self.assertEqual(schema.to_dict("<simple_root/>"), 'default_value')
        self.assertIsNone(schema.to_dict("<simple_root/>", use_defaults=False))

    def test_validation_errors(self):
        xsd_text = """<?xml version="1.0" encoding="utf-8"?>
            <xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
              <xs:element name="root" type="rootType" />
              <xs:complexType name="rootType">
                <xs:simpleContent>
                  <xs:extension base="xs:int">
                    <xs:attribute name="int_attr" type="xs:int"/>
                    <xs:attribute name="bool_attr" type="xs:boolean"/>
                  </xs:extension>
                </xs:simpleContent>
              </xs:complexType>
              <xs:element name="simple_root" type="xs:float"/>
            </xs:schema>"""

        schema = self.schema_class(xsd_text)

        self.assertIsNone(schema.to_dict("<simple_root>alpha</simple_root>", validation='lax')[0])
        self.assertEqual(schema.to_dict("<root int_attr='10'>20</root>"), {'@int_attr': 10, '$': 20})
        self.assertEqual(schema.to_dict("<root int_attr='wrong'>20</root>", validation='lax')[0],
                         {'@int_attr': None, '$': 20})
        self.assertEqual(schema.to_dict("<root int_attr='wrong'>20</root>", validation='skip'),
                         {'@int_attr': 'wrong', '$': 20})

    def test_error_message(self):
        schema = self.schema_class(os.path.join(self.test_cases_dir, 'issues/issue_115/Rotation.xsd'))
        rotation_data = '<tns:rotation xmlns:tns="http://www.example.org/Rotation/" ' \
                        'pitch="0.0" roll="0.0" yaw="-1.0" />'

        message_lines = []
        try:
            schema.decode(rotation_data)
        except Exception as err:
            message_lines = unicode_type(err).split('\n')

        self.assertTrue(message_lines, msg="Empty error message!")
        self.assertEqual(message_lines[-6], 'Instance:')
        self.assertEqual(message_lines[-4].strip(), rotation_data)
        self.assertEqual(message_lines[-2], 'Path: /tns:rotation')


class TestDecoding11(TestDecoding):
    schema_class = XMLSchema11

    def test_datetime_types(self):
        xs = self.get_schema('<element name="dt" type="dateTime"/>')
        self.assertEqual(xs.decode('<ns:dt xmlns:ns="ns">2019-01-01T13:40:00</ns:dt>'), '2019-01-01T13:40:00')
        self.assertEqual(xs.decode('<ns:dt xmlns:ns="ns">2019-01-01T13:40:00</ns:dt>', datetime_types=True),
                         datatypes.DateTime.fromstring('2019-01-01T13:40:00'))

        xs = self.get_schema('<element name="dt" type="date"/>')
        self.assertEqual(xs.decode('<ns:dt xmlns:ns="ns">2001-04-15</ns:dt>'), '2001-04-15')
        self.assertEqual(xs.decode('<ns:dt xmlns:ns="ns">2001-04-15</ns:dt>', datetime_types=True),
                         datatypes.Date.fromstring('2001-04-15'))

    def test_derived_duration_types(self):
        xs = self.get_schema('<element name="td" type="yearMonthDuration"/>')
        self.assertEqual(xs.decode('<ns:td xmlns:ns="ns">P0Y4M</ns:td>'), 'P0Y4M')
        self.assertEqual(xs.decode('<ns:td xmlns:ns="ns">P2Y10M</ns:td>', datetime_types=True),
                         datatypes.Duration.fromstring('P2Y10M'))

        xs = self.get_schema('<element name="td" type="dayTimeDuration"/>')
        self.assertEqual(xs.decode('<ns:td xmlns:ns="ns">P2DT6H30M30.001S</ns:td>'), 'P2DT6H30M30.001S')
        self.assertEqual(xs.decode('<ns:td xmlns:ns="ns">P2DT26H</ns:td>'), 'P2DT26H')
        self.assertEqual(xs.decode('<ns:td xmlns:ns="ns">P2DT6H30M30.001S</ns:td>', datetime_types=True),
                         datatypes.Duration.fromstring('P2DT6H30M30.001S'))

    def test_type_alternatives(self):
        xs = self.schema_class(self.casepath('features/elements/type_alternatives-no-ns.xsd'))
        self.assertTrue(xs.is_valid('<value choice="int">10</value>'))
        self.assertFalse(xs.is_valid('<value choice="int">10.1</value>'))
        self.assertTrue(xs.is_valid('<value choice="float">10.1</value>'))
        self.assertFalse(xs.is_valid('<value choice="float">alpha</value>'))
        self.assertFalse(xs.is_valid('<value choice="bool">alpha</value>'))
        self.assertTrue(xs.is_valid('<value choice="bool">0</value>'))
        self.assertTrue(xs.is_valid('<value choice="bool">true</value>'))

        xs = self.schema_class(self.casepath('features/elements/type_alternatives.xsd'))
        self.assertTrue(xs.is_valid('<ns:value xmlns:ns="ns" choice="int">10</ns:value>'))
        self.assertFalse(xs.is_valid('<ns:value xmlns:ns="ns" choice="int">10.1</ns:value>'))
        self.assertTrue(xs.is_valid('<ns:value xmlns:ns="ns" choice="float">10.1</ns:value>'))
        self.assertFalse(xs.is_valid('<ns:value xmlns:ns="ns" choice="float">alpha</ns:value>'))
        self.assertFalse(xs.is_valid('<ns:value xmlns:ns="ns" choice="bool">alpha</ns:value>'))
        self.assertTrue(xs.is_valid('<ns:value xmlns:ns="ns" choice="bool">0</ns:value>'))
        self.assertTrue(xs.is_valid('<ns:value xmlns:ns="ns" choice="bool">true</ns:value>'))


class TestEncoding(XMLSchemaTestCase):

    def check_encode(self, xsd_component, data, expected, **kwargs):
        if isinstance(expected, type) and issubclass(expected, Exception):
            self.assertRaises(expected, xsd_component.encode, data, **kwargs)
        elif is_etree_element(expected):
            elem = xsd_component.encode(data, **kwargs)
            self.check_etree_elements(expected, elem)
        else:
            obj = xsd_component.encode(data, **kwargs)
            if isinstance(obj, tuple) and len(obj) == 2 and isinstance(obj[1], list):
                self.assertEqual(expected, obj[0])
                self.assertTrue(isinstance(obj[0], type(expected)))
            elif is_etree_element(obj):
                namespaces = kwargs.pop('namespaces', self.default_namespaces)
                self.assertEqual(expected, etree_tostring(obj, namespaces=namespaces).strip())
            else:
                self.assertEqual(expected, obj)
                self.assertTrue(isinstance(obj, type(expected)))

    def test_decode_encode(self):
        filename = self.casepath('examples/collection/collection.xml')
        xt = ElementTree.parse(filename)
        xd = self.col_schema.to_dict(filename, dict_class=ordered_dict_class)
        elem = self.col_schema.encode(xd, path='./col:collection', namespaces=self.col_namespaces)

        self.assertEqual(
            len([e for e in elem.iter()]), 20,
            msg="The encoded tree must have 20 elements as the origin."
        )
        self.assertTrue(all([
            local_name(e1.tag) == local_name(e2.tag)
            for e1, e2 in zip(elem.iter(), xt.getroot().iter())
        ]))

    def test_builtin_string_based_types(self):
        self.check_encode(self.xsd_types['string'], 'sample string ', u'sample string ')
        self.check_encode(self.xsd_types['normalizedString'], ' sample string ', u' sample string ')
        self.check_encode(self.xsd_types['normalizedString'], '\n\r sample\tstring\n', u'   sample string ')
        self.check_encode(self.xsd_types['token'], '\n\r sample\t\tstring\n ', u'sample string')
        self.check_encode(self.xsd_types['language'], 'sample string', XMLSchemaValidationError)
        self.check_encode(self.xsd_types['language'], ' en ', u'en')
        self.check_encode(self.xsd_types['Name'], 'first_name', u'first_name')
        self.check_encode(self.xsd_types['Name'], ' first_name ', u'first_name')
        self.check_encode(self.xsd_types['Name'], 'first name', XMLSchemaValidationError)
        self.check_encode(self.xsd_types['Name'], '1st_name', XMLSchemaValidationError)
        self.check_encode(self.xsd_types['Name'], 'first_name1', u'first_name1')
        self.check_encode(self.xsd_types['Name'], 'first:name', u'first:name')
        self.check_encode(self.xsd_types['NCName'], 'first_name', u'first_name')
        self.check_encode(self.xsd_types['NCName'], 'first:name', XMLSchemaValidationError)
        self.check_encode(self.xsd_types['ENTITY'], 'first:name', XMLSchemaValidationError)
        self.check_encode(self.xsd_types['ID'], 'first:name', XMLSchemaValidationError)
        self.check_encode(self.xsd_types['IDREF'], 'first:name', XMLSchemaValidationError)

    def test_builtin_decimal_based_types(self):
        self.check_encode(self.xsd_types['decimal'], -99.09, u'-99.09')
        self.check_encode(self.xsd_types['decimal'], '-99.09', u'-99.09')
        self.check_encode(self.xsd_types['integer'], 1000, u'1000')
        self.check_encode(self.xsd_types['integer'], 100.0, XMLSchemaEncodeError)
        self.check_encode(self.xsd_types['integer'], 100.0, u'100', validation='lax')
        self.check_encode(self.xsd_types['short'], 1999, u'1999')
        self.check_encode(self.xsd_types['short'], 10000000, XMLSchemaValidationError)
        self.check_encode(self.xsd_types['float'], 100.0, u'100.0')
        self.check_encode(self.xsd_types['float'], 'hello', XMLSchemaEncodeError)
        self.check_encode(self.xsd_types['double'], -4531.7, u'-4531.7')
        self.check_encode(self.xsd_types['positiveInteger'], -1, XMLSchemaValidationError)
        self.check_encode(self.xsd_types['positiveInteger'], 0, XMLSchemaValidationError)
        self.check_encode(self.xsd_types['nonNegativeInteger'], 0, u'0')
        self.check_encode(self.xsd_types['nonNegativeInteger'], -1, XMLSchemaValidationError)
        self.check_encode(self.xsd_types['negativeInteger'], -100, u'-100')
        self.check_encode(self.xsd_types['nonPositiveInteger'], 7, XMLSchemaValidationError)
        self.check_encode(self.xsd_types['unsignedLong'], 101, u'101')
        self.check_encode(self.xsd_types['unsignedLong'], -101, XMLSchemaValidationError)
        self.check_encode(self.xsd_types['nonPositiveInteger'], 7, XMLSchemaValidationError)

    def test_builtin_list_types(self):
        self.check_encode(self.xsd_types['IDREFS'], ['first_name'], u'first_name')
        self.check_encode(self.xsd_types['IDREFS'], 'first_name', u'first_name')  # Transform data to list
        self.check_encode(self.xsd_types['IDREFS'], ['one', 'two', 'three'], u'one two three')
        self.check_encode(self.xsd_types['IDREFS'], [1, 'two', 'three'], XMLSchemaValidationError)
        self.check_encode(self.xsd_types['NMTOKENS'], ['one', 'two', 'three'], u'one two three')
        self.check_encode(self.xsd_types['ENTITIES'], ('mouse', 'cat', 'dog'), u'mouse cat dog')

    def test_list_types(self):
        list_of_strings = self.st_schema.types['list_of_strings']
        self.check_encode(list_of_strings, (10, 25, 40), u'', validation='lax')
        self.check_encode(list_of_strings, (10, 25, 40), u'10 25 40', validation='skip')
        self.check_encode(list_of_strings, ['a', 'b', 'c'], u'a b c', validation='skip')

        list_of_integers = self.st_schema.types['list_of_integers']
        self.check_encode(list_of_integers, (10, 25, 40), u'10 25 40')
        self.check_encode(list_of_integers, (10, 25.0, 40), XMLSchemaValidationError)
        self.check_encode(list_of_integers, (10, 25.0, 40), u'10 25 40', validation='lax')

        list_of_floats = self.st_schema.types['list_of_floats']
        self.check_encode(list_of_floats, [10.1, 25.0, 40.0], u'10.1 25.0 40.0')
        self.check_encode(list_of_floats, [10.1, 25, 40.0], u'10.1 25.0 40.0', validation='lax')
        self.check_encode(list_of_floats, [10.1, False, 40.0], u'10.1 0.0 40.0', validation='lax')

        list_of_booleans = self.st_schema.types['list_of_booleans']
        self.check_encode(list_of_booleans, [True, False, True], u'true false true')
        self.check_encode(list_of_booleans, [10, False, True], XMLSchemaEncodeError)
        self.check_encode(list_of_booleans, [True, False, 40.0], u'true false', validation='lax')
        self.check_encode(list_of_booleans, [True, False, 40.0], u'true false 40.0', validation='skip')

    def test_union_types(self):
        integer_or_float = self.st_schema.types['integer_or_float']
        self.check_encode(integer_or_float, -95, u'-95')
        self.check_encode(integer_or_float, -95.0, u'-95.0')
        self.check_encode(integer_or_float, True, XMLSchemaEncodeError)
        self.check_encode(integer_or_float, True, u'1', validation='lax')

        integer_or_string = self.st_schema.types['integer_or_string']
        self.check_encode(integer_or_string, 89, u'89')
        self.check_encode(integer_or_string, 89.0, u'89', validation='lax')
        self.check_encode(integer_or_string, 89.0, XMLSchemaEncodeError)
        self.check_encode(integer_or_string, False, XMLSchemaEncodeError)
        self.check_encode(integer_or_string, "Venice ", u'Venice ')

        boolean_or_integer_or_string = self.st_schema.types['boolean_or_integer_or_string']
        self.check_encode(boolean_or_integer_or_string, 89, u'89')
        self.check_encode(boolean_or_integer_or_string, 89.0, u'89', validation='lax')
        self.check_encode(boolean_or_integer_or_string, 89.0, XMLSchemaEncodeError)
        self.check_encode(boolean_or_integer_or_string, False, u'false')
        self.check_encode(boolean_or_integer_or_string, "Venice ", u'Venice ')

    def test_simple_elements(self):
        elem = etree_element('{ns}A')
        elem.text = '89'
        self.check_encode(self.get_element('A', type='string'), '89', elem)
        self.check_encode(self.get_element('A', type='integer'), 89, elem)
        elem.text = '-10.4'
        self.check_encode(self.get_element('A', type='float'), -10.4, elem)
        elem.text = 'false'
        self.check_encode(self.get_element('A', type='boolean'), False, elem)
        elem.text = 'true'
        self.check_encode(self.get_element('A', type='boolean'), True, elem)

        self.check_encode(self.get_element('A', type='short'), 128000, XMLSchemaValidationError)
        elem.text = '0'
        self.check_encode(self.get_element('A', type='nonNegativeInteger'), 0, elem)
        self.check_encode(self.get_element('A', type='nonNegativeInteger'), '0', XMLSchemaValidationError)
        self.check_encode(self.get_element('A', type='positiveInteger'), 0, XMLSchemaValidationError)
        elem.text = '-1'
        self.check_encode(self.get_element('A', type='negativeInteger'), -1, elem)
        self.check_encode(self.get_element('A', type='nonNegativeInteger'), -1, XMLSchemaValidationError)

    def test_complex_elements(self):
        schema = self.get_schema("""
        <element name="A" type="ns:A_type" />
        <complexType name="A_type" mixed="true">
            <simpleContent>
                <extension base="string">
                    <attribute name="a1" type="short" use="required"/>
                    <attribute name="a2" type="negativeInteger"/>
                </extension>
            </simpleContent>
        </complexType>
        """)
        self.check_encode(
            schema.elements['A'], data={'@a1': 10, '@a2': -1, '$': 'simple '},
            expected='<ns:A xmlns:ns="ns" a1="10" a2="-1">simple </ns:A>',
        )
        self.check_encode(
            schema.elements['A'], {'@a1': 10, '@a2': -1, '$': 'simple '},
            ElementTree.fromstring('<A xmlns="ns" a1="10" a2="-1">simple </A>'),
        )
        self.check_encode(
            schema.elements['A'], {'@a1': 10, '@a2': -1},
            ElementTree.fromstring('<A xmlns="ns" a1="10" a2="-1"/>')
        )
        self.check_encode(
            schema.elements['A'], {'@a1': 10, '$': 'simple '},
            ElementTree.fromstring('<A xmlns="ns" a1="10">simple </A>')
        )
        self.check_encode(schema.elements['A'], {'@a2': -1, '$': 'simple '}, XMLSchemaValidationError)

        schema = self.get_schema("""
        <element name="A" type="ns:A_type" />
        <complexType name="A_type">
            <sequence>
                <element name="B1" type="string"/>
                <element name="B2" type="integer"/>
                <element name="B3" type="boolean"/>
            </sequence>
        </complexType>
        """)
        self.check_encode(
            xsd_component=schema.elements['A'],
            data=ordered_dict_class([('B1', 'abc'), ('B2', 10), ('B3', False)]),
            expected=u'<ns:A xmlns:ns="ns">\n<B1>abc</B1>\n<B2>10</B2>\n<B3>false</B3>\n</ns:A>',
            indent=0,
        )
        self.check_encode(schema.elements['A'], {'B1': 'abc', 'B2': 10, 'B4': False}, XMLSchemaValidationError)
        self.check_encode(
            xsd_component=schema.elements['A'],
            data=ordered_dict_class([('B1', 'abc'), ('B2', 10), ('#1', 'hello'), ('B3', True)]),
            expected=u'<ns:A xmlns:ns="ns">\n<B1>abc</B1>\n<B2>10</B2>\nhello\n<B3>true</B3>\n</ns:A>',
            indent=0, cdata_prefix='#'
        )
        self.check_encode(
            xsd_component=schema.elements['A'],
            data=ordered_dict_class([('B1', 'abc'), ('B2', 10), ('#1', 'hello')]),
            expected=XMLSchemaValidationError, indent=0, cdata_prefix='#'
        )

    def test_encode_datetime(self):
        xs = self.get_schema('<element name="dt" type="dateTime"/>')

        dt = xs.decode('<ns:dt xmlns:ns="ns">2019-01-01T13:40:00</ns:dt>', datetime_types=True)
        self.assertEqual(
            etree_tostring(xs.encode(dt)),
            '<ns:dt xmlns:ns="ns">2019-01-01T13:40:00</ns:dt>'
        )

    def test_encode_date(self):
        xs = self.get_schema('<element name="dt" type="date"/>')
        date = xs.decode('<ns:dt xmlns:ns="ns">2001-04-15</ns:dt>', datetime_types=True)
        self.assertEqual(
            etree_tostring(xs.encode(date)),
            '<ns:dt xmlns:ns="ns">2001-04-15</ns:dt>'
        )

    def test_duration(self):
        xs = self.get_schema('<element name="td" type="duration"/>')
        duration = xs.decode('<ns:td xmlns:ns="ns">P5Y3MT60H30.001S</ns:td>', datetime_types=True)
        self.assertEqual(
            etree_tostring(xs.encode(duration)),
            '<ns:td xmlns:ns="ns">P5Y3M2DT12H30.001S</ns:td>'
        )

    def test_gregorian_year(self):
        xs = self.get_schema('<element name="td" type="gYear"/>')
        gyear = xs.decode('<ns:td xmlns:ns="ns">2000</ns:td>', datetime_types=True)
        self.assertEqual(
            etree_tostring(xs.encode(gyear)),
            '<ns:td xmlns:ns="ns">2000</ns:td>'
        )

    def test_gregorian_yearmonth(self):
        xs = self.get_schema('<element name="td" type="gYearMonth"/>')
        gyear_month = xs.decode('<ns:td xmlns:ns="ns">2000-12</ns:td>', datetime_types=True)
        self.assertEqual(
            etree_tostring(xs.encode(gyear_month)),
            '<ns:td xmlns:ns="ns">2000-12</ns:td>'
        )

    def test_error_message(self):
        schema = self.schema_class(os.path.join(self.test_cases_dir, 'issues/issue_115/Rotation.xsd'))
        rotation_data = {
            "@roll": 0.0,
            "@pitch": 0.0,
            "@yaw": -1.0  # <----- invalid value, must be between 0 and 360
        }

        message_lines = []
        try:
            schema.encode(rotation_data)
        except Exception as err:
            message_lines = unicode_type(err).split('\n')

        self.assertTrue(message_lines, msg="Empty error message!")
        self.assertEqual(message_lines[-4], 'Instance:')
        if sys.version_info < (3, 8):
            text = '<tns:rotation xmlns:tns="http://www.example.org/Rotation/" pitch="0.0" roll="0.0" yaw="-1.0" />'
        else:
            text = '<tns:rotation xmlns:tns="http://www.example.org/Rotation/" roll="0.0" pitch="0.0" yaw="-1.0" />'
        self.assertEqual(message_lines[-2].strip(), text)


class TestEncoding11(TestEncoding):
    schema_class = XMLSchema11


# Creates decoding/encoding tests classes from XML files
globals().update(tests_factory(make_validator_test_class, 'xml'))


if __name__ == '__main__':
    from xmlschema.tests import print_test_header

    print_test_header()
    unittest.main()
