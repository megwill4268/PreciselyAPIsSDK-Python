"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 11.9.3
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from com.precisely.apis.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from com.precisely.apis.exceptions import ApiAttributeError


def lazy_import():
    from com.precisely.apis.model.get_postal_codes_api_output_user_fields import GetPostalCodesAPIOutputUserFields
    globals()['GetPostalCodesAPIOutputUserFields'] = GetPostalCodesAPIOutputUserFields


class ValidateMailingAddressPremiumOutput(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'user_fields': ([GetPostalCodesAPIOutputUserFields],),  # noqa: E501
            'status': (str,),  # noqa: E501
            'status_code': (str,),  # noqa: E501
            'status_description': (str,),  # noqa: E501
            'confidence': (str,),  # noqa: E501
            'record_type': (str,),  # noqa: E501
            'record_type_default': (str,),  # noqa: E501
            'multiple_matches': (str,),  # noqa: E501
            'could_not_validate': (str,),  # noqa: E501
            'country_level': (str,),  # noqa: E501
            'address_format': (str,),  # noqa: E501
            'address_line1': (str,),  # noqa: E501
            'address_line2': (str,),  # noqa: E501
            'address_line3': (str,),  # noqa: E501
            'address_line4': (str,),  # noqa: E501
            'city': (str,),  # noqa: E501
            'state_province': (str,),  # noqa: E501
            'postal_code': (str,),  # noqa: E501
            'postal_code_base': (str,),  # noqa: E501
            'postal_code_add_on': (str,),  # noqa: E501
            'country': (str,),  # noqa: E501
            'additional_input_data': (str,),  # noqa: E501
            'firm_name': (str,),  # noqa: E501
            'house_number': (str,),  # noqa: E501
            'leading_directional': (str,),  # noqa: E501
            'street_name': (str,),  # noqa: E501
            'street_suffix': (str,),  # noqa: E501
            'trailing_directional': (str,),  # noqa: E501
            'apartment_label': (str,),  # noqa: E501
            'apartment_number': (str,),  # noqa: E501
            'apartment_label2': (str,),  # noqa: E501
            'apartment_number2': (str,),  # noqa: E501
            'rrhc': (str,),  # noqa: E501
            'po_box': (str,),  # noqa: E501
            'private_mailbox': (str,),  # noqa: E501
            'private_mailbox_type': (str,),  # noqa: E501
            'house_number_input': (str,),  # noqa: E501
            'leading_directional_input': (str,),  # noqa: E501
            'street_name_input': (str,),  # noqa: E501
            'street_suffix_input': (str,),  # noqa: E501
            'trailing_directional_input': (str,),  # noqa: E501
            'apartment_label_input': (str,),  # noqa: E501
            'apartment_number_input': (str,),  # noqa: E501
            'rrhc_input': (str,),  # noqa: E501
            'po_box_input': (str,),  # noqa: E501
            'private_mailbox_input': (str,),  # noqa: E501
            'private_mailbox_type_input': (str,),  # noqa: E501
            'city_input': (str,),  # noqa: E501
            'state_province_input': (str,),  # noqa: E501
            'postal_code_input': (str,),  # noqa: E501
            'country_input': (str,),  # noqa: E501
            'firm_name_input': (str,),  # noqa: E501
            'house_number_result': (str,),  # noqa: E501
            'leading_directional_result': (str,),  # noqa: E501
            'street_result': (str,),  # noqa: E501
            'street_name_result': (str,),  # noqa: E501
            'street_name_alias_type': (str,),  # noqa: E501
            'street_suffix_result': (str,),  # noqa: E501
            'trailing_directional_result': (str,),  # noqa: E501
            'apartment_label_result': (str,),  # noqa: E501
            'apartment_number_result': (str,),  # noqa: E501
            'apartment_label2_result': (str,),  # noqa: E501
            'apartment_number2_result': (str,),  # noqa: E501
            'rrhc_result': (str,),  # noqa: E501
            'rrhc_type': (str,),  # noqa: E501
            'po_box_result': (str,),  # noqa: E501
            'city_result': (str,),  # noqa: E501
            'state_province_result': (str,),  # noqa: E501
            'postal_code_result': (str,),  # noqa: E501
            'postal_code_city_result': (str,),  # noqa: E501
            'address_record_result': (str,),  # noqa: E501
            'postal_code_source': (str,),  # noqa: E501
            'postal_code_type': (str,),  # noqa: E501
            'country_result': (str,),  # noqa: E501
            'firm_name_result': (str,),  # noqa: E501
            'street_name_preferred_alias_result': (str,),  # noqa: E501
            'street_name_abbreviated_alias_result': (str,),  # noqa: E501
            'address_line5': (str,),  # noqa: E501
            'address_quality': (str,),  # noqa: E501
            'deliverability': (str,),  # noqa: E501
            'address_type': (str,),  # noqa: E501
            'locality': (str,),  # noqa: E501
            'change_score': (str,),  # noqa: E501
            'suburb': (str,),  # noqa: E501
            'block_address': (str,),  # noqa: E501
            'latitude': (str,),  # noqa: E501
            'longitude': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'user_fields': 'user_fields',  # noqa: E501
        'status': 'Status',  # noqa: E501
        'status_code': 'Status.Code',  # noqa: E501
        'status_description': 'Status.Description',  # noqa: E501
        'confidence': 'Confidence',  # noqa: E501
        'record_type': 'RecordType',  # noqa: E501
        'record_type_default': 'RecordType.Default',  # noqa: E501
        'multiple_matches': 'MultipleMatches',  # noqa: E501
        'could_not_validate': 'CouldNotValidate',  # noqa: E501
        'country_level': 'CountryLevel',  # noqa: E501
        'address_format': 'AddressFormat',  # noqa: E501
        'address_line1': 'AddressLine1',  # noqa: E501
        'address_line2': 'AddressLine2',  # noqa: E501
        'address_line3': 'AddressLine3',  # noqa: E501
        'address_line4': 'AddressLine4',  # noqa: E501
        'city': 'City',  # noqa: E501
        'state_province': 'StateProvince',  # noqa: E501
        'postal_code': 'PostalCode',  # noqa: E501
        'postal_code_base': 'PostalCode.Base',  # noqa: E501
        'postal_code_add_on': 'PostalCode.AddOn',  # noqa: E501
        'country': 'Country',  # noqa: E501
        'additional_input_data': 'AdditionalInputData',  # noqa: E501
        'firm_name': 'FirmName',  # noqa: E501
        'house_number': 'HouseNumber',  # noqa: E501
        'leading_directional': 'LeadingDirectional',  # noqa: E501
        'street_name': 'StreetName',  # noqa: E501
        'street_suffix': 'StreetSuffix',  # noqa: E501
        'trailing_directional': 'TrailingDirectional',  # noqa: E501
        'apartment_label': 'ApartmentLabel',  # noqa: E501
        'apartment_number': 'ApartmentNumber',  # noqa: E501
        'apartment_label2': 'ApartmentLabel2',  # noqa: E501
        'apartment_number2': 'ApartmentNumber2',  # noqa: E501
        'rrhc': 'RRHC',  # noqa: E501
        'po_box': 'POBox',  # noqa: E501
        'private_mailbox': 'PrivateMailbox',  # noqa: E501
        'private_mailbox_type': 'PrivateMailbox.Type',  # noqa: E501
        'house_number_input': 'HouseNumber.Input',  # noqa: E501
        'leading_directional_input': 'LeadingDirectional.Input',  # noqa: E501
        'street_name_input': 'StreetName.Input',  # noqa: E501
        'street_suffix_input': 'StreetSuffix.Input',  # noqa: E501
        'trailing_directional_input': 'TrailingDirectional.Input',  # noqa: E501
        'apartment_label_input': 'ApartmentLabel.Input',  # noqa: E501
        'apartment_number_input': 'ApartmentNumber.Input',  # noqa: E501
        'rrhc_input': 'RRHC.Input',  # noqa: E501
        'po_box_input': 'POBox.Input',  # noqa: E501
        'private_mailbox_input': 'PrivateMailbox.Input',  # noqa: E501
        'private_mailbox_type_input': 'PrivateMailbox.Type.Input',  # noqa: E501
        'city_input': 'City.Input',  # noqa: E501
        'state_province_input': 'StateProvince.Input',  # noqa: E501
        'postal_code_input': 'PostalCode.Input',  # noqa: E501
        'country_input': 'Country.Input',  # noqa: E501
        'firm_name_input': 'FirmName.Input',  # noqa: E501
        'house_number_result': 'HouseNumber.Result',  # noqa: E501
        'leading_directional_result': 'LeadingDirectional.Result',  # noqa: E501
        'street_result': 'Street.Result',  # noqa: E501
        'street_name_result': 'StreetName.Result',  # noqa: E501
        'street_name_alias_type': 'StreetName.Alias.Type',  # noqa: E501
        'street_suffix_result': 'StreetSuffix.Result',  # noqa: E501
        'trailing_directional_result': 'TrailingDirectional.Result',  # noqa: E501
        'apartment_label_result': 'ApartmentLabel.Result',  # noqa: E501
        'apartment_number_result': 'ApartmentNumber.Result',  # noqa: E501
        'apartment_label2_result': 'ApartmentLabel2.Result',  # noqa: E501
        'apartment_number2_result': 'ApartmentNumber2.Result',  # noqa: E501
        'rrhc_result': 'RRHC.Result',  # noqa: E501
        'rrhc_type': 'RRHC.Type',  # noqa: E501
        'po_box_result': 'POBox.Result',  # noqa: E501
        'city_result': 'City.Result',  # noqa: E501
        'state_province_result': 'StateProvince.Result',  # noqa: E501
        'postal_code_result': 'PostalCode.Result',  # noqa: E501
        'postal_code_city_result': 'PostalCodeCity.Result',  # noqa: E501
        'address_record_result': 'AddressRecord.Result',  # noqa: E501
        'postal_code_source': 'PostalCode.Source',  # noqa: E501
        'postal_code_type': 'PostalCode.Type',  # noqa: E501
        'country_result': 'Country.Result',  # noqa: E501
        'firm_name_result': 'FirmName.Result',  # noqa: E501
        'street_name_preferred_alias_result': 'StreetNamePreferredAlias.Result',  # noqa: E501
        'street_name_abbreviated_alias_result': 'StreetNameAbbreviatedAlias.Result',  # noqa: E501
        'address_line5': 'AddressLine5',  # noqa: E501
        'address_quality': 'AddressQuality',  # noqa: E501
        'deliverability': 'Deliverability',  # noqa: E501
        'address_type': 'AddressType',  # noqa: E501
        'locality': 'Locality',  # noqa: E501
        'change_score': 'ChangeScore',  # noqa: E501
        'suburb': 'Suburb',  # noqa: E501
        'block_address': 'BlockAddress',  # noqa: E501
        'latitude': 'Latitude',  # noqa: E501
        'longitude': 'Longitude',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ValidateMailingAddressPremiumOutput - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            user_fields ([GetPostalCodesAPIOutputUserFields]): These fields are returned, unmodified, in the user_fields section of the response.. [optional]  # noqa: E501
            status (str): Reports the success or failure of the match attempt.. [optional]  # noqa: E501
            status_code (str): Reason for failure, if there is one.. [optional]  # noqa: E501
            status_description (str): Description of the problem, if there is one.. [optional]  # noqa: E501
            confidence (str): The level of confidence assigned to the address being returned.. [optional]  # noqa: E501
            record_type (str): Type of address record.. [optional]  # noqa: E501
            record_type_default (str): Code indicating the default match.. [optional]  # noqa: E501
            multiple_matches (str): Indicates which address component had multiple matches.. [optional]  # noqa: E501
            could_not_validate (str): Mentions the address component that could not be validated, in case no match is found.. [optional]  # noqa: E501
            country_level (str): The category of address matching available.. [optional]  # noqa: E501
            address_format (str): The type of address data being returned.. [optional]  # noqa: E501
            address_line1 (str): The first line of the validated address.. [optional]  # noqa: E501
            address_line2 (str): The second line of the validated address.. [optional]  # noqa: E501
            address_line3 (str): The third line of the validated address.. [optional]  # noqa: E501
            address_line4 (str): The fourth line of the validated address.. [optional]  # noqa: E501
            city (str): The validated city name.. [optional]  # noqa: E501
            state_province (str): The validated state or province abbreviation.. [optional]  # noqa: E501
            postal_code (str): The validated ZIP Code or postal code.. [optional]  # noqa: E501
            postal_code_base (str): The 5-digit ZIP Code.. [optional]  # noqa: E501
            postal_code_add_on (str): The 4-digit add-on part of the ZIP Code.. [optional]  # noqa: E501
            country (str): The country in the format determined by what you selected.. [optional]  # noqa: E501
            additional_input_data (str): Input data that could not be matched to a particular address component.. [optional]  # noqa: E501
            firm_name (str): The validated firm or company name.. [optional]  # noqa: E501
            house_number (str): House number.. [optional]  # noqa: E501
            leading_directional (str): Leading directional.. [optional]  # noqa: E501
            street_name (str): Street name.. [optional]  # noqa: E501
            street_suffix (str): Street suffix.. [optional]  # noqa: E501
            trailing_directional (str): Trailing directional.. [optional]  # noqa: E501
            apartment_label (str): Apartment designator (such as STE or APT).. [optional]  # noqa: E501
            apartment_number (str): Apartment number.. [optional]  # noqa: E501
            apartment_label2 (str): Secondary apartment designator.. [optional]  # noqa: E501
            apartment_number2 (str): Secondary apartment number.. [optional]  # noqa: E501
            rrhc (str): Rural Route/Highway Contract indicator.. [optional]  # noqa: E501
            po_box (str): Post office box number.. [optional]  # noqa: E501
            private_mailbox (str): Private mailbox indicator.. [optional]  # noqa: E501
            private_mailbox_type (str): The type of private mailbox.. [optional]  # noqa: E501
            house_number_input (str): House number.. [optional]  # noqa: E501
            leading_directional_input (str): Leading directional.. [optional]  # noqa: E501
            street_name_input (str): Street name.. [optional]  # noqa: E501
            street_suffix_input (str): Street suffix.. [optional]  # noqa: E501
            trailing_directional_input (str): Trailing directional.. [optional]  # noqa: E501
            apartment_label_input (str): Apartment designator (such as STE or APT).. [optional]  # noqa: E501
            apartment_number_input (str): Apartment number.. [optional]  # noqa: E501
            rrhc_input (str): Rural Route/Highway Contract indicator.. [optional]  # noqa: E501
            po_box_input (str): Post office box number.. [optional]  # noqa: E501
            private_mailbox_input (str): Private mailbox indicator.. [optional]  # noqa: E501
            private_mailbox_type_input (str): The type of private mailbox.. [optional]  # noqa: E501
            city_input (str): Validated city name.. [optional]  # noqa: E501
            state_province_input (str): Validated state or province name.. [optional]  # noqa: E501
            postal_code_input (str): Validated postal code.. [optional]  # noqa: E501
            country_input (str): Country. Format is determined by what you selected in OutputCountryFormat.. [optional]  # noqa: E501
            firm_name_input (str): The validated firm or company name.. [optional]  # noqa: E501
            house_number_result (str): The field-level result indicator for HouseNumber.. [optional]  # noqa: E501
            leading_directional_result (str): The field-level result indicator for LeadingDirectional.. [optional]  # noqa: E501
            street_result (str): The field-level result indicator for Street.. [optional]  # noqa: E501
            street_name_result (str): The field-level result indicator for StreetName.. [optional]  # noqa: E501
            street_name_alias_type (str): The field-level result indicator for StreetName Alias.. [optional]  # noqa: E501
            street_suffix_result (str): The field-level result indicator for StreetSuffix.. [optional]  # noqa: E501
            trailing_directional_result (str): The field-level result indicator for TrailingDirectional.. [optional]  # noqa: E501
            apartment_label_result (str): The field-level result indicator for ApartmentLabel.. [optional]  # noqa: E501
            apartment_number_result (str): The field-level result indicator for ApartmentNumber.. [optional]  # noqa: E501
            apartment_label2_result (str): The field-level result indicator for ApartmentLabel2.. [optional]  # noqa: E501
            apartment_number2_result (str): The field-level result indicator for ApartmentNumber2.. [optional]  # noqa: E501
            rrhc_result (str): The field-level result indicator for RRHC.. [optional]  # noqa: E501
            rrhc_type (str): The field-level result indicator for RRHC Type.. [optional]  # noqa: E501
            po_box_result (str): The field-level result indicator for POBox.. [optional]  # noqa: E501
            city_result (str): The field-level result indicator for City.. [optional]  # noqa: E501
            state_province_result (str): The field-level result indicator for StateProvince.. [optional]  # noqa: E501
            postal_code_result (str): The field-level result indicator for PostalCode.. [optional]  # noqa: E501
            postal_code_city_result (str): The field-level result indicator for PostalCodeCity.. [optional]  # noqa: E501
            address_record_result (str): The field-level result indicator for AddressRecord.. [optional]  # noqa: E501
            postal_code_source (str): The field-level result indicator for PostalCode Source.. [optional]  # noqa: E501
            postal_code_type (str): Indicates the type of postal code returned.. [optional]  # noqa: E501
            country_result (str): The validated firm or company name.. [optional]  # noqa: E501
            firm_name_result (str): Indicates if the firm name got validated.. [optional]  # noqa: E501
            street_name_preferred_alias_result (str): Indicates the result of preferred alias processing.. [optional]  # noqa: E501
            street_name_abbreviated_alias_result (str): Indicates the result of abbreviated alias processing.. [optional]  # noqa: E501
            address_line5 (str): The fifth line of the validated address.. [optional]  # noqa: E501
            address_quality (str): A two character code indicating overall quality of the resulting address.. [optional]  # noqa: E501
            deliverability (str): An estimate of confidence that an item mailed or shipped to this address would be successfully delivered.. [optional]  # noqa: E501
            address_type (str): A single letter code that indicates the type of address.. [optional]  # noqa: E501
            locality (str): A locality is a village in rural areas or it may be a suburb in urban areas.. [optional]  # noqa: E501
            change_score (str): A value of 0 and 100 that reflects how much the address has changed to make it valid.. [optional]  # noqa: E501
            suburb (str): The validated firm or company name.. [optional]  # noqa: E501
            block_address (str): It is the formatted address, as it would appear on a physical mail piece.. [optional]  # noqa: E501
            latitude (str): Seven-digit number in degrees, calculated to four decimal places.. [optional]  # noqa: E501
            longitude (str): Seven-digit number in degrees, calculated to four decimal places.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """ValidateMailingAddressPremiumOutput - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            user_fields ([GetPostalCodesAPIOutputUserFields]): These fields are returned, unmodified, in the user_fields section of the response.. [optional]  # noqa: E501
            status (str): Reports the success or failure of the match attempt.. [optional]  # noqa: E501
            status_code (str): Reason for failure, if there is one.. [optional]  # noqa: E501
            status_description (str): Description of the problem, if there is one.. [optional]  # noqa: E501
            confidence (str): The level of confidence assigned to the address being returned.. [optional]  # noqa: E501
            record_type (str): Type of address record.. [optional]  # noqa: E501
            record_type_default (str): Code indicating the default match.. [optional]  # noqa: E501
            multiple_matches (str): Indicates which address component had multiple matches.. [optional]  # noqa: E501
            could_not_validate (str): Mentions the address component that could not be validated, in case no match is found.. [optional]  # noqa: E501
            country_level (str): The category of address matching available.. [optional]  # noqa: E501
            address_format (str): The type of address data being returned.. [optional]  # noqa: E501
            address_line1 (str): The first line of the validated address.. [optional]  # noqa: E501
            address_line2 (str): The second line of the validated address.. [optional]  # noqa: E501
            address_line3 (str): The third line of the validated address.. [optional]  # noqa: E501
            address_line4 (str): The fourth line of the validated address.. [optional]  # noqa: E501
            city (str): The validated city name.. [optional]  # noqa: E501
            state_province (str): The validated state or province abbreviation.. [optional]  # noqa: E501
            postal_code (str): The validated ZIP Code or postal code.. [optional]  # noqa: E501
            postal_code_base (str): The 5-digit ZIP Code.. [optional]  # noqa: E501
            postal_code_add_on (str): The 4-digit add-on part of the ZIP Code.. [optional]  # noqa: E501
            country (str): The country in the format determined by what you selected.. [optional]  # noqa: E501
            additional_input_data (str): Input data that could not be matched to a particular address component.. [optional]  # noqa: E501
            firm_name (str): The validated firm or company name.. [optional]  # noqa: E501
            house_number (str): House number.. [optional]  # noqa: E501
            leading_directional (str): Leading directional.. [optional]  # noqa: E501
            street_name (str): Street name.. [optional]  # noqa: E501
            street_suffix (str): Street suffix.. [optional]  # noqa: E501
            trailing_directional (str): Trailing directional.. [optional]  # noqa: E501
            apartment_label (str): Apartment designator (such as STE or APT).. [optional]  # noqa: E501
            apartment_number (str): Apartment number.. [optional]  # noqa: E501
            apartment_label2 (str): Secondary apartment designator.. [optional]  # noqa: E501
            apartment_number2 (str): Secondary apartment number.. [optional]  # noqa: E501
            rrhc (str): Rural Route/Highway Contract indicator.. [optional]  # noqa: E501
            po_box (str): Post office box number.. [optional]  # noqa: E501
            private_mailbox (str): Private mailbox indicator.. [optional]  # noqa: E501
            private_mailbox_type (str): The type of private mailbox.. [optional]  # noqa: E501
            house_number_input (str): House number.. [optional]  # noqa: E501
            leading_directional_input (str): Leading directional.. [optional]  # noqa: E501
            street_name_input (str): Street name.. [optional]  # noqa: E501
            street_suffix_input (str): Street suffix.. [optional]  # noqa: E501
            trailing_directional_input (str): Trailing directional.. [optional]  # noqa: E501
            apartment_label_input (str): Apartment designator (such as STE or APT).. [optional]  # noqa: E501
            apartment_number_input (str): Apartment number.. [optional]  # noqa: E501
            rrhc_input (str): Rural Route/Highway Contract indicator.. [optional]  # noqa: E501
            po_box_input (str): Post office box number.. [optional]  # noqa: E501
            private_mailbox_input (str): Private mailbox indicator.. [optional]  # noqa: E501
            private_mailbox_type_input (str): The type of private mailbox.. [optional]  # noqa: E501
            city_input (str): Validated city name.. [optional]  # noqa: E501
            state_province_input (str): Validated state or province name.. [optional]  # noqa: E501
            postal_code_input (str): Validated postal code.. [optional]  # noqa: E501
            country_input (str): Country. Format is determined by what you selected in OutputCountryFormat.. [optional]  # noqa: E501
            firm_name_input (str): The validated firm or company name.. [optional]  # noqa: E501
            house_number_result (str): The field-level result indicator for HouseNumber.. [optional]  # noqa: E501
            leading_directional_result (str): The field-level result indicator for LeadingDirectional.. [optional]  # noqa: E501
            street_result (str): The field-level result indicator for Street.. [optional]  # noqa: E501
            street_name_result (str): The field-level result indicator for StreetName.. [optional]  # noqa: E501
            street_name_alias_type (str): The field-level result indicator for StreetName Alias.. [optional]  # noqa: E501
            street_suffix_result (str): The field-level result indicator for StreetSuffix.. [optional]  # noqa: E501
            trailing_directional_result (str): The field-level result indicator for TrailingDirectional.. [optional]  # noqa: E501
            apartment_label_result (str): The field-level result indicator for ApartmentLabel.. [optional]  # noqa: E501
            apartment_number_result (str): The field-level result indicator for ApartmentNumber.. [optional]  # noqa: E501
            apartment_label2_result (str): The field-level result indicator for ApartmentLabel2.. [optional]  # noqa: E501
            apartment_number2_result (str): The field-level result indicator for ApartmentNumber2.. [optional]  # noqa: E501
            rrhc_result (str): The field-level result indicator for RRHC.. [optional]  # noqa: E501
            rrhc_type (str): The field-level result indicator for RRHC Type.. [optional]  # noqa: E501
            po_box_result (str): The field-level result indicator for POBox.. [optional]  # noqa: E501
            city_result (str): The field-level result indicator for City.. [optional]  # noqa: E501
            state_province_result (str): The field-level result indicator for StateProvince.. [optional]  # noqa: E501
            postal_code_result (str): The field-level result indicator for PostalCode.. [optional]  # noqa: E501
            postal_code_city_result (str): The field-level result indicator for PostalCodeCity.. [optional]  # noqa: E501
            address_record_result (str): The field-level result indicator for AddressRecord.. [optional]  # noqa: E501
            postal_code_source (str): The field-level result indicator for PostalCode Source.. [optional]  # noqa: E501
            postal_code_type (str): Indicates the type of postal code returned.. [optional]  # noqa: E501
            country_result (str): The validated firm or company name.. [optional]  # noqa: E501
            firm_name_result (str): Indicates if the firm name got validated.. [optional]  # noqa: E501
            street_name_preferred_alias_result (str): Indicates the result of preferred alias processing.. [optional]  # noqa: E501
            street_name_abbreviated_alias_result (str): Indicates the result of abbreviated alias processing.. [optional]  # noqa: E501
            address_line5 (str): The fifth line of the validated address.. [optional]  # noqa: E501
            address_quality (str): A two character code indicating overall quality of the resulting address.. [optional]  # noqa: E501
            deliverability (str): An estimate of confidence that an item mailed or shipped to this address would be successfully delivered.. [optional]  # noqa: E501
            address_type (str): A single letter code that indicates the type of address.. [optional]  # noqa: E501
            locality (str): A locality is a village in rural areas or it may be a suburb in urban areas.. [optional]  # noqa: E501
            change_score (str): A value of 0 and 100 that reflects how much the address has changed to make it valid.. [optional]  # noqa: E501
            suburb (str): The validated firm or company name.. [optional]  # noqa: E501
            block_address (str): It is the formatted address, as it would appear on a physical mail piece.. [optional]  # noqa: E501
            latitude (str): Seven-digit number in degrees, calculated to four decimal places.. [optional]  # noqa: E501
            longitude (str): Seven-digit number in degrees, calculated to four decimal places.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
