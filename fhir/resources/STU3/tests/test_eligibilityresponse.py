#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 3.0.1.11917 on 2019-05-13.
#  2019, SMART Health IT.

import os
import pytest
import io
import unittest
import json

from .fixtures import force_bytes
from .. import eligibilityresponse
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class EligibilityResponseTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("EligibilityResponse", js["resourceType"])
        return eligibilityresponse.EligibilityResponse(js)
    
    def testEligibilityResponse1(self):
        inst = self.instantiate_from("eligibilityresponse-example-error.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse1(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse1(inst2)
    
    def implEligibilityResponse1(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(force_bytes(inst.disposition), force_bytes("Eligibiliy request could not be processed, please address errors before submitting."))
        self.assertEqual(force_bytes(inst.error[0].code.coding[0].code), force_bytes("a001"))
        self.assertEqual(force_bytes(inst.error[0].code.coding[0].system), force_bytes("http://hl7.org/fhir/adjudication-error"))
        self.assertEqual(force_bytes(inst.form.coding[0].code), force_bytes("ELRSP/2017/01"))
        self.assertEqual(force_bytes(inst.form.coding[0].system), force_bytes("http://national.org/form"))
        self.assertEqual(force_bytes(inst.id), force_bytes("E2503"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/eligibilityresponse"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("8812343"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("error"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/remittance-outcome"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testEligibilityResponse2(self):
        inst = self.instantiate_from("eligibilityresponse-example-benefits-2.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse2(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse2(inst2)
    
    def implEligibilityResponse2(self, inst):
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("patient-1"))
        self.assertEqual(force_bytes(inst.contained[1].id), force_bytes("coverage-1"))
        self.assertEqual(inst.created.date, FHIRDate("2014-09-16").date)
        self.assertEqual(inst.created.as_json(), "2014-09-16")
        self.assertEqual(force_bytes(inst.disposition), force_bytes("Policy is currently in-force."))
        self.assertEqual(force_bytes(inst.form.coding[0].code), force_bytes("ELRSP/2017/01"))
        self.assertEqual(force_bytes(inst.form.coding[0].system), force_bytes("http://national.org/form"))
        self.assertEqual(force_bytes(inst.id), force_bytes("E2502"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/eligibilityresponse"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("8812342"))
        self.assertTrue(inst.inforce)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].category.coding[0].code), force_bytes("medical"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].category.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.value, 500000)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[0].type.coding[0].code), force_bytes("benefit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[0].usedMoney.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[0].usedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].usedMoney.value, 3748.0)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.value, 100)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[1].type.coding[0].code), force_bytes("copay-maximum"))
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[2].allowedUnsignedInt, 20)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[2].type.coding[0].code), force_bytes("copay-percent"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].network.coding[0].code), force_bytes("in"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].network.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-network"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].subCategory.coding[0].code), force_bytes("30"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].subCategory.coding[0].display), force_bytes("Health Benefit Plan Coverage"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].subCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].term.coding[0].code), force_bytes("annual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].term.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-term"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].unit.coding[0].code), force_bytes("individual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].unit.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-unit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].category.coding[0].code), force_bytes("medical"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].category.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.value, 15000)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].financial[0].type.coding[0].code), force_bytes("benefit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].network.coding[0].code), force_bytes("in"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].network.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-network"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].subCategory.coding[0].code), force_bytes("69"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].subCategory.coding[0].display), force_bytes("Maternity"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].subCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].term.coding[0].code), force_bytes("annual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].term.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-term"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].unit.coding[0].code), force_bytes("individual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].unit.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-unit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].category.coding[0].code), force_bytes("oral"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].category.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.code), force_bytes("USD"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.value, 2000)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].financial[0].type.coding[0].code), force_bytes("benefit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].network.coding[0].code), force_bytes("in"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].network.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-network"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].subCategory.coding[0].code), force_bytes("F3"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].subCategory.coding[0].display), force_bytes("Dental Coverage"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].subCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].term.coding[0].code), force_bytes("annual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].term.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-term"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].unit.coding[0].code), force_bytes("individual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].unit.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-unit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].category.coding[0].code), force_bytes("vision"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].category.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].description), force_bytes("Vision products and services such as exams, glasses and contatc lenses."))
        self.assertTrue(inst.insurance[0].benefitBalance[3].excluded)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].name), force_bytes("Vision"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].subCategory.coding[0].code), force_bytes("F6"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].subCategory.coding[0].display), force_bytes("Vision Coverage"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].subCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/remittance-outcome"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testEligibilityResponse3(self):
        inst = self.instantiate_from("eligibilityresponse-example.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse3(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse3(inst2)
    
    def implEligibilityResponse3(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.disposition), force_bytes("Policy is currently in-force."))
        self.assertEqual(force_bytes(inst.id), force_bytes("E2500"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/eligibilityresponse"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("881234"))
        self.assertTrue(inst.inforce)
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/remittance-outcome"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testEligibilityResponse4(self):
        inst = self.instantiate_from("eligibilityresponse-example-benefits.json")
        self.assertIsNotNone(inst, "Must have instantiated a EligibilityResponse instance")
        self.implEligibilityResponse4(inst)
        
        js = inst.as_json()
        self.assertEqual("EligibilityResponse", js["resourceType"])
        inst2 = eligibilityresponse.EligibilityResponse(js)
        self.implEligibilityResponse4(inst2)
    
    def implEligibilityResponse4(self, inst):
        self.assertEqual(inst.created.date, FHIRDate("2014-08-16").date)
        self.assertEqual(inst.created.as_json(), "2014-08-16")
        self.assertEqual(force_bytes(inst.disposition), force_bytes("Policy is currently in-force."))
        self.assertEqual(force_bytes(inst.id), force_bytes("E2501"))
        self.assertEqual(force_bytes(inst.identifier[0].system), force_bytes("http://www.BenefitsInc.com/fhir/eligibilityresponse"))
        self.assertEqual(force_bytes(inst.identifier[0].value), force_bytes("881234"))
        self.assertTrue(inst.inforce)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].category.coding[0].code), force_bytes("medical"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].category.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.code), force_bytes("SAR"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[0].allowedMoney.value, 500000)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[0].type.coding[0].code), force_bytes("benefit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.code), force_bytes("SAR"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[1].allowedMoney.value, 100)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[1].type.coding[0].code), force_bytes("copay-maximum"))
        self.assertEqual(inst.insurance[0].benefitBalance[0].financial[2].allowedUnsignedInt, 20)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].financial[2].type.coding[0].code), force_bytes("copay-percent"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].network.coding[0].code), force_bytes("in"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].network.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-network"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].subCategory.coding[0].code), force_bytes("30"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].subCategory.coding[0].display), force_bytes("Health Benefit Plan Coverage"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].subCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].term.coding[0].code), force_bytes("annual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].term.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-term"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].unit.coding[0].code), force_bytes("individual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[0].unit.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-unit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].category.coding[0].code), force_bytes("medical"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].category.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.code), force_bytes("SAR"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[1].financial[0].allowedMoney.value, 15000)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].financial[0].type.coding[0].code), force_bytes("benefit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].network.coding[0].code), force_bytes("in"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].network.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-network"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].subCategory.coding[0].code), force_bytes("69"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].subCategory.coding[0].display), force_bytes("Maternity"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].subCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].term.coding[0].code), force_bytes("annual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].term.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-term"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].unit.coding[0].code), force_bytes("individual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[1].unit.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-unit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].category.coding[0].code), force_bytes("oral"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].category.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.code), force_bytes("SAR"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[2].financial[0].allowedMoney.value, 2000)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].financial[0].type.coding[0].code), force_bytes("benefit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].network.coding[0].code), force_bytes("in"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].network.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-network"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].subCategory.coding[0].code), force_bytes("F3"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].subCategory.coding[0].display), force_bytes("Dental Coverage"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].subCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].term.coding[0].code), force_bytes("annual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].term.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-term"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].unit.coding[0].code), force_bytes("individual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[2].unit.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-unit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].category.coding[0].code), force_bytes("vision"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].category.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].financial[0].allowedMoney.code), force_bytes("SAR"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].financial[0].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[3].financial[0].allowedMoney.value, 400)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].financial[0].type.coding[0].code), force_bytes("benefit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].network.coding[0].code), force_bytes("in"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].network.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-network"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].subCategory.coding[0].code), force_bytes("F6"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].subCategory.coding[0].display), force_bytes("Vision Coverage"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].subCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].term.coding[0].code), force_bytes("annual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].term.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-term"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].unit.coding[0].code), force_bytes("individual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[3].unit.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-unit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].category.coding[0].code), force_bytes("vision"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].category.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-category"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].financial[0].allowedString), force_bytes("shared"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].financial[0].type.coding[0].code), force_bytes("room"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].financial[1].allowedMoney.code), force_bytes("SAR"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].financial[1].allowedMoney.system), force_bytes("urn:iso:std:iso:4217"))
        self.assertEqual(inst.insurance[0].benefitBalance[4].financial[1].allowedMoney.value, 600)
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].financial[1].type.coding[0].code), force_bytes("benefit"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].network.coding[0].code), force_bytes("in"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].network.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-network"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].subCategory.coding[0].code), force_bytes("49"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].subCategory.coding[0].display), force_bytes("Hospital Room and Board"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].subCategory.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-subcategory"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].term.coding[0].code), force_bytes("day"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].term.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-term"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].unit.coding[0].code), force_bytes("individual"))
        self.assertEqual(force_bytes(inst.insurance[0].benefitBalance[4].unit.coding[0].system), force_bytes("http://hl7.org/fhir/benefit-unit"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].code), force_bytes("complete"))
        self.assertEqual(force_bytes(inst.outcome.coding[0].system), force_bytes("http://hl7.org/fhir/remittance-outcome"))
        self.assertEqual(force_bytes(inst.status), force_bytes("active"))
        self.assertEqual(force_bytes(inst.text.div), force_bytes("<div xmlns=\"http://www.w3.org/1999/xhtml\">A human-readable rendering of the EligibilityResponse.</div>"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))

