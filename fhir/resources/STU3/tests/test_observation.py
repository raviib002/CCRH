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
from .. import observation
from ..fhirdate import FHIRDate


@pytest.mark.usefixtures("base_settings")
class ObservationTests(unittest.TestCase):
    def instantiate_from(self, filename):
        datadir = os.environ.get('FHIR_UNITTEST_DATADIR') or ''
        with io.open(os.path.join(datadir, filename), 'r', encoding='utf-8') as handle:
            js = json.load(handle)
            self.assertEqual("Observation", js["resourceType"])
        return observation.Observation(js)
    
    def testObservation1(self):
        inst = self.instantiate_from("observation-example-date-lastmp.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation1(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation1(inst2)
    
    def implObservation1(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("survey"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Survey"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://hl7.org/fhir/observation-category"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("AOE"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8665-2"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Date last menstrual period"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Date last menstrual period"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2016-01-24").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-01-24")
        self.assertEqual(force_bytes(inst.id), force_bytes("date-lastmp"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(inst.valueDateTime.date, FHIRDate("2016-12-30").date)
        self.assertEqual(inst.valueDateTime.as_json(), "2016-12-30")
    
    def testObservation2(self):
        inst = self.instantiate_from("observation-example-body-temperature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation2(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation2(inst2)
    
    def implObservation2(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://hl7.org/fhir/observation-category"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8310-5"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Body temperature"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Body temperature"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("body-temperature"))
        self.assertEqual(force_bytes(inst.meta.profile[0]), force_bytes("http://hl7.org/fhir/StructureDefinition/vitalsigns"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.valueQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("C"))
        self.assertEqual(inst.valueQuantity.value, 36.5)
    
    def testObservation3(self):
        inst = self.instantiate_from("observation-example-phenotype.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation3(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation3(inst2)
    
    def implObservation3(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("79716-7"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("CYP2C9 gene product metabolic activity interpretation"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/observation-geneticsGene"))
        self.assertEqual(force_bytes(inst.extension[0].valueCodeableConcept.coding[0].code), force_bytes("2623"))
        self.assertEqual(force_bytes(inst.extension[0].valueCodeableConcept.coding[0].display), force_bytes("CYP2C9"))
        self.assertEqual(force_bytes(inst.extension[0].valueCodeableConcept.coding[0].system), force_bytes("http://www.genenames.org"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-phenotype"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(force_bytes(inst.related[0].type), force_bytes("derived-from"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueCodeableConcept.coding[0].code), force_bytes("LA25391-6"))
        self.assertEqual(force_bytes(inst.valueCodeableConcept.coding[0].display), force_bytes("Normal metabolizer"))
        self.assertEqual(force_bytes(inst.valueCodeableConcept.coding[0].system), force_bytes("http://loinc.org"))
    
    def testObservation4(self):
        inst = self.instantiate_from("observation-example-2minute-apgar-score.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation4(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation4(inst2)
    
    def implObservation4(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("survey"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Survey"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://hl7.org/fhir/observation-category"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Survey"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("9273-4"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("2 minute Apgar Score"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("2 minute Apgar Score"))
        self.assertEqual(force_bytes(inst.component[0].code.coding[0].code), force_bytes("249227004"))
        self.assertEqual(force_bytes(inst.component[0].code.coding[0].display), force_bytes("Apgar color score"))
        self.assertEqual(force_bytes(inst.component[0].code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.component[0].code.text), force_bytes("Apgar color score"))
        self.assertEqual(force_bytes(inst.component[0].valueCodeableConcept.coding[0].code), force_bytes("LA6723-6"))
        self.assertEqual(force_bytes(inst.component[0].valueCodeableConcept.coding[0].display), force_bytes("Good color in body with bluish hands or feet"))
        self.assertEqual(force_bytes(inst.component[0].valueCodeableConcept.coding[0].extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/iso21090-CO-value"))
        self.assertEqual(inst.component[0].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(force_bytes(inst.component[0].valueCodeableConcept.coding[0].system), force_bytes("http://loinc.org/la"))
        self.assertEqual(force_bytes(inst.component[0].valueCodeableConcept.coding[1].code), force_bytes("1"))
        self.assertEqual(force_bytes(inst.component[0].valueCodeableConcept.coding[1].system), force_bytes("http:/acme.ped/apgarcolor"))
        self.assertEqual(force_bytes(inst.component[0].valueCodeableConcept.text), force_bytes("1. Good color in body with bluish hands or feet"))
        self.assertEqual(force_bytes(inst.component[1].code.coding[0].code), force_bytes("249223000"))
        self.assertEqual(force_bytes(inst.component[1].code.coding[0].display), force_bytes("Apgar heart rate score"))
        self.assertEqual(force_bytes(inst.component[1].code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.component[1].code.text), force_bytes("Apgar respiratory effort score"))
        self.assertEqual(force_bytes(inst.component[1].valueCodeableConcept.coding[0].code), force_bytes("LA6720-2"))
        self.assertEqual(force_bytes(inst.component[1].valueCodeableConcept.coding[0].display), force_bytes("Fewer than 100 beats per minute"))
        self.assertEqual(force_bytes(inst.component[1].valueCodeableConcept.coding[0].extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/iso21090-CO-value"))
        self.assertEqual(inst.component[1].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(force_bytes(inst.component[1].valueCodeableConcept.coding[0].system), force_bytes("http://loinc.org/la"))
        self.assertEqual(force_bytes(inst.component[1].valueCodeableConcept.coding[1].code), force_bytes("1"))
        self.assertEqual(force_bytes(inst.component[1].valueCodeableConcept.coding[1].system), force_bytes("http:/acme.ped/apgarheartrate"))
        self.assertEqual(force_bytes(inst.component[1].valueCodeableConcept.text), force_bytes("1. Fewer than 100 beats per minute"))
        self.assertEqual(force_bytes(inst.component[2].code.coding[0].code), force_bytes("249226008"))
        self.assertEqual(force_bytes(inst.component[2].code.coding[0].display), force_bytes("Apgar response to stimulus score"))
        self.assertEqual(force_bytes(inst.component[2].code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.component[2].code.text), force_bytes("Apgar response to stimulus score"))
        self.assertEqual(force_bytes(inst.component[2].valueCodeableConcept.coding[0].code), force_bytes("LA6721-0"))
        self.assertEqual(force_bytes(inst.component[2].valueCodeableConcept.coding[0].display), force_bytes("Grimace during suctioning"))
        self.assertEqual(force_bytes(inst.component[2].valueCodeableConcept.coding[0].extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/iso21090-CO-value"))
        self.assertEqual(inst.component[2].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(force_bytes(inst.component[2].valueCodeableConcept.coding[0].system), force_bytes("http://loinc.org/la"))
        self.assertEqual(force_bytes(inst.component[2].valueCodeableConcept.coding[1].code), force_bytes("1"))
        self.assertEqual(force_bytes(inst.component[2].valueCodeableConcept.coding[1].system), force_bytes("http:/acme.ped/apgarreflexirritability"))
        self.assertEqual(force_bytes(inst.component[2].valueCodeableConcept.text), force_bytes("1. Grimace during suctioning"))
        self.assertEqual(force_bytes(inst.component[3].code.coding[0].code), force_bytes("249225007"))
        self.assertEqual(force_bytes(inst.component[3].code.coding[0].display), force_bytes("Apgar muscle tone score"))
        self.assertEqual(force_bytes(inst.component[3].code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.component[3].code.text), force_bytes("Apgar muscle tone score"))
        self.assertEqual(force_bytes(inst.component[3].valueCodeableConcept.coding[0].code), force_bytes("LA6714-5"))
        self.assertEqual(force_bytes(inst.component[3].valueCodeableConcept.coding[0].display), force_bytes("Some flexion of arms and legs"))
        self.assertEqual(force_bytes(inst.component[3].valueCodeableConcept.coding[0].extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/iso21090-CO-value"))
        self.assertEqual(inst.component[3].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(force_bytes(inst.component[3].valueCodeableConcept.coding[0].system), force_bytes("http://loinc.org/la"))
        self.assertEqual(force_bytes(inst.component[3].valueCodeableConcept.coding[1].code), force_bytes("1"))
        self.assertEqual(force_bytes(inst.component[3].valueCodeableConcept.coding[1].system), force_bytes("http:/acme.ped/apgarmuscletone"))
        self.assertEqual(force_bytes(inst.component[3].valueCodeableConcept.text), force_bytes("1. Some flexion of arms and legs"))
        self.assertEqual(force_bytes(inst.component[4].code.coding[0].code), force_bytes("249224006"))
        self.assertEqual(force_bytes(inst.component[4].code.coding[0].display), force_bytes("Apgar respiratory effort score"))
        self.assertEqual(force_bytes(inst.component[4].code.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.component[4].code.text), force_bytes("Apgar respiratory effort score"))
        self.assertEqual(force_bytes(inst.component[4].valueCodeableConcept.coding[0].code), force_bytes("LA6726-9"))
        self.assertEqual(force_bytes(inst.component[4].valueCodeableConcept.coding[0].display), force_bytes("Weak cry; may sound like whimpering, slow or irregular breathing"))
        self.assertEqual(force_bytes(inst.component[4].valueCodeableConcept.coding[0].extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/iso21090-CO-value"))
        self.assertEqual(inst.component[4].valueCodeableConcept.coding[0].extension[0].valueDecimal, 1)
        self.assertEqual(force_bytes(inst.component[4].valueCodeableConcept.coding[0].system), force_bytes("http://loinc.org/la"))
        self.assertEqual(force_bytes(inst.component[4].valueCodeableConcept.coding[1].code), force_bytes("1"))
        self.assertEqual(force_bytes(inst.component[4].valueCodeableConcept.coding[1].system), force_bytes("http:/acme.ped/apgarrespiratoryeffort"))
        self.assertEqual(force_bytes(inst.component[4].valueCodeableConcept.text), force_bytes("1. Weak cry; may sound like whimpering, slow or irregular breathing"))
        self.assertEqual(force_bytes(inst.contained[0].id), force_bytes("newborn"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("2016-05-18T22:33:22Z").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "2016-05-18T22:33:22Z")
        self.assertEqual(force_bytes(inst.id), force_bytes("2minute-apgar-score"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("{score}"))
        self.assertEqual(force_bytes(inst.valueQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(inst.valueQuantity.value, 5)
    
    def testObservation5(self):
        inst = self.instantiate_from("observation-example-f202-temperature.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation5(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation5(inst2)
    
    def implObservation5(self, inst):
        self.assertEqual(force_bytes(inst.bodySite.coding[0].code), force_bytes("74262004"))
        self.assertEqual(force_bytes(inst.bodySite.coding[0].display), force_bytes("Oral cavity"))
        self.assertEqual(force_bytes(inst.bodySite.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://hl7.org/fhir/observation-category"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("BT"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Body temperature"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://acme.lab"))
        self.assertEqual(force_bytes(inst.code.coding[1].code), force_bytes("8310-5"))
        self.assertEqual(force_bytes(inst.code.coding[1].display), force_bytes("Body temperature"))
        self.assertEqual(force_bytes(inst.code.coding[1].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.coding[2].code), force_bytes("8331-1"))
        self.assertEqual(force_bytes(inst.code.coding[2].display), force_bytes("Oral temperature"))
        self.assertEqual(force_bytes(inst.code.coding[2].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.coding[3].code), force_bytes("56342008"))
        self.assertEqual(force_bytes(inst.code.coding[3].display), force_bytes("Temperature taking"))
        self.assertEqual(force_bytes(inst.code.coding[3].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Temperature"))
        self.assertEqual(force_bytes(inst.id), force_bytes("f202"))
        self.assertEqual(force_bytes(inst.interpretation.coding[0].code), force_bytes("H"))
        self.assertEqual(force_bytes(inst.interpretation.coding[0].system), force_bytes("http://hl7.org/fhir/v2/0078"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-04T13:27:00+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-04T13:27:00+01:00")
        self.assertEqual(force_bytes(inst.method.coding[0].code), force_bytes("89003005"))
        self.assertEqual(force_bytes(inst.method.coding[0].display), force_bytes("Oral temperature taking"))
        self.assertEqual(force_bytes(inst.method.coding[0].system), force_bytes("http://snomed.info/sct"))
        self.assertEqual(force_bytes(inst.referenceRange[0].high.unit), force_bytes("degrees C"))
        self.assertEqual(inst.referenceRange[0].high.value, 38.2)
        self.assertEqual(force_bytes(inst.status), force_bytes("entered-in-error"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("Cel"))
        self.assertEqual(force_bytes(inst.valueQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("degrees C"))
        self.assertEqual(inst.valueQuantity.value, 39)
    
    def testObservation6(self):
        inst = self.instantiate_from("observation-example-haplotype1.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation6(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation6(inst2)
    
    def implObservation6(self, inst):
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("55233-1"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Genetic analysis master panel-- This is the parent OBR for the panel holding all of the associated observations that can be reported with a molecular genetics analysis result."))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.extension[0].url), force_bytes("http://hl7.org/fhir/StructureDefinition/observation-geneticsGene"))
        self.assertEqual(force_bytes(inst.extension[0].valueCodeableConcept.coding[0].code), force_bytes("2625"))
        self.assertEqual(force_bytes(inst.extension[0].valueCodeableConcept.coding[0].display), force_bytes("CYP2D6"))
        self.assertEqual(force_bytes(inst.extension[0].valueCodeableConcept.coding[0].system), force_bytes("http://www.genenames.org"))
        self.assertEqual(force_bytes(inst.extension[1].url), force_bytes("http://hl7.org/fhir/StructureDefinition/observation-geneticsSequence"))
        self.assertEqual(force_bytes(inst.extension[2].url), force_bytes("http://hl7.org/fhir/StructureDefinition/observation-geneticsSequence"))
        self.assertEqual(force_bytes(inst.id), force_bytes("example-haplotype1"))
        self.assertEqual(inst.issued.date, FHIRDate("2013-04-03T15:30:10+01:00").date)
        self.assertEqual(inst.issued.as_json(), "2013-04-03T15:30:10+01:00")
        self.assertEqual(force_bytes(inst.related[0].type), force_bytes("derived-from"))
        self.assertEqual(force_bytes(inst.related[1].type), force_bytes("derived-from"))
        self.assertEqual(force_bytes(inst.status), force_bytes("unknown"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueCodeableConcept.coding[0].code), force_bytes("PA165971587"))
        self.assertEqual(force_bytes(inst.valueCodeableConcept.coding[0].display), force_bytes("*35B"))
        self.assertEqual(force_bytes(inst.valueCodeableConcept.coding[0].system), force_bytes("http://pharmakb.org"))
    
    def testObservation7(self):
        inst = self.instantiate_from("observation-example-vitals-panel.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation7(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation7(inst2)
    
    def implObservation7(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://hl7.org/fhir/observation-category"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("85353-1"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Vital signs, weight, height, head circumference, oxygen saturation and BMI panel"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Vital signs Panel"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("vitals-panel"))
        self.assertEqual(force_bytes(inst.meta.profile[0]), force_bytes("http://hl7.org/fhir/StructureDefinition/vitalsigns"))
        self.assertEqual(force_bytes(inst.related[0].type), force_bytes("has-member"))
        self.assertEqual(force_bytes(inst.related[1].type), force_bytes("has-member"))
        self.assertEqual(force_bytes(inst.related[2].type), force_bytes("has-member"))
        self.assertEqual(force_bytes(inst.related[3].type), force_bytes("has-member"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
    
    def testObservation8(self):
        inst = self.instantiate_from("observation-example-mbp.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation8(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation8(inst2)
    
    def implObservation8(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://hl7.org/fhir/observation-category"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8478-0"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Mean blood pressure"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Mean blood pressure"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("mbp"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("mm[Hg]"))
        self.assertEqual(force_bytes(inst.valueQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("mm[Hg]"))
        self.assertEqual(inst.valueQuantity.value, 80)
    
    def testObservation9(self):
        inst = self.instantiate_from("observation-example-head-circumference.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation9(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation9(inst2)
    
    def implObservation9(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://hl7.org/fhir/observation-category"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("8287-5"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Head Occipital-frontal circumference by Tape measure"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Head Circumference"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("head-circumference"))
        self.assertEqual(force_bytes(inst.meta.profile[0]), force_bytes("http://hl7.org/fhir/StructureDefinition/vitalsigns"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("cm"))
        self.assertEqual(force_bytes(inst.valueQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("cm"))
        self.assertEqual(inst.valueQuantity.value, 51.2)
    
    def testObservation10(self):
        inst = self.instantiate_from("observation-example-respiratory-rate.json")
        self.assertIsNotNone(inst, "Must have instantiated a Observation instance")
        self.implObservation10(inst)
        
        js = inst.as_json()
        self.assertEqual("Observation", js["resourceType"])
        inst2 = observation.Observation(js)
        self.implObservation10(inst2)
    
    def implObservation10(self, inst):
        self.assertEqual(force_bytes(inst.category[0].coding[0].code), force_bytes("vital-signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].display), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.category[0].coding[0].system), force_bytes("http://hl7.org/fhir/observation-category"))
        self.assertEqual(force_bytes(inst.category[0].text), force_bytes("Vital Signs"))
        self.assertEqual(force_bytes(inst.code.coding[0].code), force_bytes("9279-1"))
        self.assertEqual(force_bytes(inst.code.coding[0].display), force_bytes("Respiratory rate"))
        self.assertEqual(force_bytes(inst.code.coding[0].system), force_bytes("http://loinc.org"))
        self.assertEqual(force_bytes(inst.code.text), force_bytes("Respiratory rate"))
        self.assertEqual(inst.effectiveDateTime.date, FHIRDate("1999-07-02").date)
        self.assertEqual(inst.effectiveDateTime.as_json(), "1999-07-02")
        self.assertEqual(force_bytes(inst.id), force_bytes("respiratory-rate"))
        self.assertEqual(force_bytes(inst.meta.profile[0]), force_bytes("http://hl7.org/fhir/StructureDefinition/vitalsigns"))
        self.assertEqual(force_bytes(inst.status), force_bytes("final"))
        self.assertEqual(force_bytes(inst.text.status), force_bytes("generated"))
        self.assertEqual(force_bytes(inst.valueQuantity.code), force_bytes("/min"))
        self.assertEqual(force_bytes(inst.valueQuantity.system), force_bytes("http://unitsofmeasure.org"))
        self.assertEqual(force_bytes(inst.valueQuantity.unit), force_bytes("breaths/minute"))
        self.assertEqual(inst.valueQuantity.value, 26)

