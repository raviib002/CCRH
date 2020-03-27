#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Generated from FHIR 4.0.0-a53ec6ee1b (http://hl7.org/fhir/StructureDefinition/MedicationDispense) on 2019-05-13.
#  2019, SMART Health IT.


from . import domainresource

class MedicationDispense(domainresource.DomainResource):
    """ Dispensing a medication to a named patient.

    Indicates that a medication product is to be or has been dispensed for a
    named person/patient.  This includes a description of the medication
    product (supply) provided and the instructions for administering the
    medication.  The medication dispense is the result of a pharmacy system
    responding to a medication order.
    """

    resource_type = "MedicationDispense"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.authorizingPrescription = None
        """ Medication order that authorizes the dispense.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.category = None
        """ Type of medication dispense.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.context = None
        """ Encounter / Episode associated with event.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.daysSupply = None
        """ Amount of medication expressed as a timing amount.
        Type `Quantity` (represented as `dict` in JSON). """

        self.destination = None
        """ Where the medication was sent.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.detectedIssue = None
        """ Clinical issue with action.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.dosageInstruction = None
        """ How the medication is to be used by the patient or administered by
        the caregiver.
        List of `Dosage` items (represented as `dict` in JSON). """

        self.eventHistory = None
        """ A list of relevant lifecycle events.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.identifier = None
        """ External identifier.
        List of `Identifier` items (represented as `dict` in JSON). """

        self.location = None
        """ Where the dispense occurred.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.medicationCodeableConcept = None
        """ What medication was supplied.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.medicationReference = None
        """ What medication was supplied.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.note = None
        """ Information about the dispense.
        List of `Annotation` items (represented as `dict` in JSON). """

        self.partOf = None
        """ Event that dispense is part of.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.performer = None
        """ Who performed event.
        List of `MedicationDispensePerformer` items (represented as `dict` in JSON). """

        self.quantity = None
        """ Amount dispensed.
        Type `Quantity` (represented as `dict` in JSON). """

        self.receiver = None
        """ Who collected the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.status = None
        """ preparation | in-progress | cancelled | on-hold | completed |
        entered-in-error | stopped | unknown.
        Type `str`. """

        self.statusReasonCodeableConcept = None
        """ Why a dispense was not performed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.statusReasonReference = None
        """ Why a dispense was not performed.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.subject = None
        """ Who the dispense is for.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.substitution = None
        """ Whether a substitution was performed on the dispense.
        Type `MedicationDispenseSubstitution` (represented as `dict` in JSON). """

        self.supportingInformation = None
        """ Information that supports the dispensing of the medication.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.type = None
        """ Trial fill, partial fill, emergency fill, etc..
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.whenHandedOver = None
        """ When product was given out.
        Type `FHIRDate` (represented as `str` in JSON). """

        self.whenPrepared = None
        """ When product was packaged and reviewed.
        Type `FHIRDate` (represented as `str` in JSON). """

        super(MedicationDispense, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicationDispense, self).elementProperties()
        js.extend([
            ("authorizingPrescription", "authorizingPrescription", fhirreference.FHIRReference, "Reference", True, None, False),
            ("category", "category", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("context", "context", fhirreference.FHIRReference, "Reference", False, None, False),
            ("daysSupply", "daysSupply", quantity.Quantity, "Quantity", False, None, False),
            ("destination", "destination", fhirreference.FHIRReference, "Reference", False, None, False),
            ("detectedIssue", "detectedIssue", fhirreference.FHIRReference, "Reference", True, None, False),
            ("dosageInstruction", "dosageInstruction", dosage.Dosage, "Dosage", True, None, False),
            ("eventHistory", "eventHistory", fhirreference.FHIRReference, "Reference", True, None, False),
            ("identifier", "identifier", identifier.Identifier, "Identifier", True, None, False),
            ("location", "location", fhirreference.FHIRReference, "Reference", False, None, False),
            ("medicationCodeableConcept", "medicationCodeableConcept", codeableconcept.CodeableConcept, "CodeableConcept", False, "medication", True),
            ("medicationReference", "medicationReference", fhirreference.FHIRReference, "Reference", False, "medication", True),
            ("note", "note", annotation.Annotation, "Annotation", True, None, False),
            ("partOf", "partOf", fhirreference.FHIRReference, "Reference", True, None, False),
            ("performer", "performer", MedicationDispensePerformer, "MedicationDispensePerformer", True, None, False),
            ("quantity", "quantity", quantity.Quantity, "Quantity", False, None, False),
            ("receiver", "receiver", fhirreference.FHIRReference, "Reference", True, None, False),
            ("status", "status", str, "code", False, None, True),
            ("statusReasonCodeableConcept", "statusReasonCodeableConcept", codeableconcept.CodeableConcept, "CodeableConcept", False, "statusReason", False),
            ("statusReasonReference", "statusReasonReference", fhirreference.FHIRReference, "Reference", False, "statusReason", False),
            ("subject", "subject", fhirreference.FHIRReference, "Reference", False, None, False),
            ("substitution", "substitution", MedicationDispenseSubstitution, "MedicationDispenseSubstitution", False, None, False),
            ("supportingInformation", "supportingInformation", fhirreference.FHIRReference, "Reference", True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("whenHandedOver", "whenHandedOver", fhirdate.FHIRDate, "dateTime", False, None, False),
            ("whenPrepared", "whenPrepared", fhirdate.FHIRDate, "dateTime", False, None, False),
        ])
        return js


from . import backboneelement

class MedicationDispensePerformer(backboneelement.BackboneElement):
    """ Who performed event.

    Indicates who or what performed the event.
    """

    resource_type = "MedicationDispensePerformer"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.actor = None
        """ Individual who was performing.
        Type `FHIRReference` (represented as `dict` in JSON). """

        self.function = None
        """ Who performed the dispense and what they did.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        super(MedicationDispensePerformer, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicationDispensePerformer, self).elementProperties()
        js.extend([
            ("actor", "actor", fhirreference.FHIRReference, "Reference", False, None, True),
            ("function", "function", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
        ])
        return js


class MedicationDispenseSubstitution(backboneelement.BackboneElement):
    """ Whether a substitution was performed on the dispense.

    Indicates whether or not substitution was made as part of the dispense.  In
    some cases, substitution will be expected but does not happen, in other
    cases substitution is not expected but does happen.  This block explains
    what substitution did or did not happen and why.  If nothing is specified,
    substitution was not done.
    """

    resource_type = "MedicationDispenseSubstitution"

    def __init__(self, jsondict=None, strict=True):
        """ Initialize all valid properties.

        :raises: FHIRValidationError on validation errors, unless strict is False
        :param dict jsondict: A JSON dictionary to use for initialization
        :param bool strict: If True (the default), invalid variables will raise a TypeError
        """

        self.reason = None
        """ Why was substitution made.
        List of `CodeableConcept` items (represented as `dict` in JSON). """

        self.responsibleParty = None
        """ Who is responsible for the substitution.
        List of `FHIRReference` items (represented as `dict` in JSON). """

        self.type = None
        """ Code signifying whether a different drug was dispensed from what
        was prescribed.
        Type `CodeableConcept` (represented as `dict` in JSON). """

        self.wasSubstituted = None
        """ Whether a substitution was or was not performed on the dispense.
        Type `bool`. """

        super(MedicationDispenseSubstitution, self).__init__(jsondict=jsondict, strict=strict)

    def elementProperties(self):
        js = super(MedicationDispenseSubstitution, self).elementProperties()
        js.extend([
            ("reason", "reason", codeableconcept.CodeableConcept, "CodeableConcept", True, None, False),
            ("responsibleParty", "responsibleParty", fhirreference.FHIRReference, "Reference", True, None, False),
            ("type", "type", codeableconcept.CodeableConcept, "CodeableConcept", False, None, False),
            ("wasSubstituted", "wasSubstituted", bool, "boolean", False, None, True),
        ])
        return js


import sys
try:
    from . import annotation
except ImportError:
    annotation = sys.modules[__package__ + '.annotation']
try:
    from . import codeableconcept
except ImportError:
    codeableconcept = sys.modules[__package__ + '.codeableconcept']
try:
    from . import dosage
except ImportError:
    dosage = sys.modules[__package__ + '.dosage']
try:
    from . import fhirdate
except ImportError:
    fhirdate = sys.modules[__package__ + '.fhirdate']
try:
    from . import fhirreference
except ImportError:
    fhirreference = sys.modules[__package__ + '.fhirreference']
try:
    from . import identifier
except ImportError:
    identifier = sys.modules[__package__ + '.identifier']
try:
    from . import quantity
except ImportError:
    quantity = sys.modules[__package__ + '.quantity']
