"""
    Precisely APIs

    Enhance & enrich your data, applications, business processes, and workflows with rich location, information, and identify APIs.  # noqa: E501

    The version of the OpenAPI document: 11.9.2
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from com.precisely.apis.api_client import ApiClient, Endpoint as _Endpoint
from com.precisely.apis.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from com.precisely.apis.model.error_info import ErrorInfo
from com.precisely.apis.model.timezone_address_request import TimezoneAddressRequest
from com.precisely.apis.model.timezone_location_request import TimezoneLocationRequest
from com.precisely.apis.model.timezone_response import TimezoneResponse
from com.precisely.apis.model.timezone_response_list import TimezoneResponseList


class TimeZoneServiceApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_batch_timezone_by_location_endpoint = _Endpoint(
            settings={
                'response_type': (TimezoneResponseList,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/timezone/v1/timezone/bylocation',
                'operation_id': 'get_batch_timezone_by_location',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'timezone_location_request',
                ],
                'required': [
                    'timezone_location_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'timezone_location_request':
                        (TimezoneLocationRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'timezone_location_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.get_timezone_by_address_endpoint = _Endpoint(
            settings={
                'response_type': (TimezoneResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/timezone/v1/timezone/byaddress',
                'operation_id': 'get_timezone_by_address',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'timestamp',
                    'address',
                    'match_mode',
                    'country',
                ],
                'required': [
                    'timestamp',
                    'address',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'timestamp':
                        (str,),
                    'address':
                        (str,),
                    'match_mode':
                        (str,),
                    'country':
                        (str,),
                },
                'attribute_map': {
                    'timestamp': 'timestamp',
                    'address': 'address',
                    'match_mode': 'matchMode',
                    'country': 'country',
                },
                'location_map': {
                    'timestamp': 'query',
                    'address': 'query',
                    'match_mode': 'query',
                    'country': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_timezone_by_address_batch_endpoint = _Endpoint(
            settings={
                'response_type': (TimezoneResponseList,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/timezone/v1/timezone/byaddress',
                'operation_id': 'get_timezone_by_address_batch',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'timezone_address_request',
                ],
                'required': [
                    'timezone_address_request',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'timezone_address_request':
                        (TimezoneAddressRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'timezone_address_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [
                    'application/json',
                    'application/xml'
                ]
            },
            api_client=api_client
        )
        self.get_timezone_by_location_endpoint = _Endpoint(
            settings={
                'response_type': (TimezoneResponse,),
                'auth': [
                    'oAuth2Password'
                ],
                'endpoint_path': '/timezone/v1/timezone/bylocation',
                'operation_id': 'get_timezone_by_location',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'timestamp',
                    'longitude',
                    'latitude',
                ],
                'required': [
                    'timestamp',
                    'longitude',
                    'latitude',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'timestamp':
                        (str,),
                    'longitude':
                        (str,),
                    'latitude':
                        (str,),
                },
                'attribute_map': {
                    'timestamp': 'timestamp',
                    'longitude': 'longitude',
                    'latitude': 'latitude',
                },
                'location_map': {
                    'timestamp': 'query',
                    'longitude': 'query',
                    'latitude': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json',
                    'application/xml'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_batch_timezone_by_location(
        self,
        timezone_location_request,
        **kwargs
    ):
        """Timezone Batch by Location.  # noqa: E501

        Identifies and retrieves the local time of any location in the world for a given latitude, longitude and time. The input and retrieved time format is in milliseconds.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_batch_timezone_by_location(timezone_location_request, async_req=True)
        >>> result = thread.get()

        Args:
            timezone_location_request (TimezoneLocationRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TimezoneResponseList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['timezone_location_request'] = \
            timezone_location_request
        return self.get_batch_timezone_by_location_endpoint.call_with_http_info(**kwargs)

    def get_timezone_by_address(
        self,
        timestamp,
        address,
        **kwargs
    ):
        """Timezone By Address.  # noqa: E501

        Identifies and retrieves the local time of any location in the world for a given address and time. The input and retrieved time format is in milliseconds.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_timezone_by_address(timestamp, address, async_req=True)
        >>> result = thread.get()

        Args:
            timestamp (str): Timestamp in miliseconds.
            address (str): The address to be searched.

        Keyword Args:
            match_mode (str): Match modes determine the leniency used to make a match between the input address and the reference data (Default is relaxed). [optional]
            country (str): Country ISO code (Default is USA). [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TimezoneResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['timestamp'] = \
            timestamp
        kwargs['address'] = \
            address
        return self.get_timezone_by_address_endpoint.call_with_http_info(**kwargs)

    def get_timezone_by_address_batch(
        self,
        timezone_address_request,
        **kwargs
    ):
        """Timezone Batch by Address.  # noqa: E501

        Identifies and retrieves the local time of any location in the world for a given address and time. The input and retrieved time format is in milliseconds.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_timezone_by_address_batch(timezone_address_request, async_req=True)
        >>> result = thread.get()

        Args:
            timezone_address_request (TimezoneAddressRequest):

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TimezoneResponseList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['timezone_address_request'] = \
            timezone_address_request
        return self.get_timezone_by_address_batch_endpoint.call_with_http_info(**kwargs)

    def get_timezone_by_location(
        self,
        timestamp,
        longitude,
        latitude,
        **kwargs
    ):
        """Timezone By Location.  # noqa: E501

        Identifies and retrieves the local time of any location in the world for a given latitude, longitude and time. The input and retrieved time format is in milliseconds.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_timezone_by_location(timestamp, longitude, latitude, async_req=True)
        >>> result = thread.get()

        Args:
            timestamp (str): Timestamp in miliseconds.
            longitude (str): Longitude of the location.
            latitude (str): Latitude of the location.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            TimezoneResponse
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['timestamp'] = \
            timestamp
        kwargs['longitude'] = \
            longitude
        kwargs['latitude'] = \
            latitude
        return self.get_timezone_by_location_endpoint.call_with_http_info(**kwargs)

