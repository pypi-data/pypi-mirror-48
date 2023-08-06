# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v2.0 (
 https://apimatic.io ).
"""

from tester.api_helper import APIHelper
from tester.exceptions.api_exception import APIException
from tester.exceptions.nested_model_exception import NestedModelException
from tester.exceptions.custom_error_response_exception import CustomErrorResponseException
from tester.exceptions.exception_with_string_exception import ExceptionWithStringException
from tester.exceptions.exception_with_boolean_exception import ExceptionWithBooleanException
from tester.exceptions.exception_with_dynamic_exception import ExceptionWithDynamicException
from tester.exceptions.exception_with_uuid_exception import ExceptionWithUUIDException
from tester.exceptions.exception_with_date_exception import ExceptionWithDateException
from tester.exceptions.exception_with_number_exception import ExceptionWithNumberException
from tester.exceptions.exception_with_long_exception import ExceptionWithLongException
from tester.exceptions.exception_with_precision_exception import ExceptionWithPrecisionException
from tester.exceptions.exception_with_rfc_3339_date_time_exception import ExceptionWithRfc3339DateTimeException
from tester.exceptions.unix_time_stamp_exception import UnixTimeStampException
from tester.exceptions.rfc_1123_exception import Rfc1123Exception
from tester.exceptions.send_boolean_in_model_as_exception import SendBooleanInModelAsException
from tester.exceptions.send_rfc_3339_in_model_as_exception import SendRfc3339InModelAsException
from tester.exceptions.send_rfc_1123_in_model_as_exception import SendRfc1123InModelAsException
from tester.exceptions.send_unix_time_stamp_in_model_as_exception import SendUnixTimeStampInModelAsException
from tester.exceptions.send_date_in_model_as_exception import SendDateInModelAsException
from tester.exceptions.send_dynamic_in_model_as_exception import SendDynamicInModelAsException
from tester.exceptions.send_string_in_model_as_exception import SendStringInModelAsException
from tester.exceptions.send_long_in_model_as_exception import SendLongInModelAsException
from tester.exceptions.send_number_in_model_as_exception import SendNumberInModelAsException
from tester.exceptions.send_precision_in_model_as_exception import SendPrecisionInModelAsException
from tester.exceptions.send_uuid_in_model_as_exception import SendUuidInModelAsException
from tester.exceptions.global_test_exception import GlobalTestException


class BaseController(object):

    """All controllers inherit from this base class.

    Attributes:
        config (Configuration): The HttpClient which a specific controller
            instance will use. By default all the controller objects share
            the same HttpClient. A user can use his own custom HttpClient
            as well.
        http_call_back (HttpCallBack): An object which holds call back
            methods to be called before and after the execution of an HttpRequest.
        global_headers (dict): The global headers of the API which are sent with
            every request.

    """

    global_headers = {

    }

    def __init__(self, config, call_back=None):
        self._config = config
        self._http_call_back = call_back

    @property
    def config(self):
        return self._config

    @property
    def http_call_back(self):
        return self._http_call_back

    def validate_parameters(self, **kwargs):
        """Validates required parameters of an endpoint.

        Args:
            kwargs (dict): A dictionary of the required parameters.

        """
        for name, value in kwargs.items():
            if value is None:
                raise ValueError("Required parameter {} cannot be None.".format(name))

    def execute_request(self, request, binary=False):
        """Executes an HttpRequest.

        Args:
            request (HttpRequest): The HttpRequest to execute.
            binary (bool): A flag which should be set to True if
                a binary response is expected.

        Returns:
            HttpResponse: The HttpResponse received.

        """
        # Invoke the on before request HttpCallBack if specified
        if self.http_call_back is not None:
            self.http_call_back.on_before_request(request)

        # Add global headers to request
        request.headers = APIHelper.merge_dicts(self.global_headers, request.headers)

        # Invoke the API call to fetch the response.
        func = self.config.http_client.execute_as_binary if binary else self.config.http_client.execute_as_string
        response = func(request)

        # Invoke the on after response HttpCallBack if specified
        if self.http_call_back is not None:
            self.http_call_back.on_after_response(response)

        return response

    def validate_response(self, response):
        """Validates an HTTP response by checking for global errors.

        Args:
            response (HttpResponse): The HttpResponse of the API call.

        """
        if response.status_code == 400:
            raise GlobalTestException('400 Global', response)
        elif response.status_code == 402:
            raise GlobalTestException('402 Global', response)
        elif response.status_code == 403:
            raise GlobalTestException('403 Global', response)
        elif response.status_code == 404:
            raise GlobalTestException('404 Global', response)
        elif response.status_code == 412:
            raise NestedModelException('Precondition Failed', response)
        elif response.status_code == 450:
            raise CustomErrorResponseException('caught global exception', response)
        elif response.status_code == 452:
            raise ExceptionWithStringException('global exception with string', response)
        elif response.status_code == 453:
            raise ExceptionWithBooleanException('boolean in global exception', response)
        elif response.status_code == 454:
            raise ExceptionWithDynamicException('dynamic in global exception', response)
        elif response.status_code == 455:
            raise ExceptionWithUUIDException('uuid in global exception', response)
        elif response.status_code == 456:
            raise ExceptionWithDateException('date in global exception', response)
        elif response.status_code == 457:
            raise ExceptionWithNumberException('number in global  exception', response)
        elif response.status_code == 458:
            raise ExceptionWithLongException('long in global exception', response)
        elif response.status_code == 459:
            raise ExceptionWithPrecisionException('precision in global  exception', response)
        elif response.status_code == 460:
            raise ExceptionWithRfc3339DateTimeException('rfc3339 in global exception', response)
        elif response.status_code == 461:
            raise UnixTimeStampException('unix time stamp in global exception', response)
        elif response.status_code == 462:
            raise Rfc1123Exception('rfc1123 in global exception', response)
        elif response.status_code == 463:
            raise SendBooleanInModelAsException('boolean in model as global exception', response)
        elif response.status_code == 464:
            raise SendRfc3339InModelAsException('rfc3339 in model as global exception', response)
        elif response.status_code == 465:
            raise SendRfc1123InModelAsException('rfc1123 in model as global exception', response)
        elif response.status_code == 466:
            raise SendUnixTimeStampInModelAsException('unix time stamp in model as global exception', response)
        elif response.status_code == 467:
            raise SendDateInModelAsException('send date in model as global exception', response)
        elif response.status_code == 468:
            raise SendDynamicInModelAsException('send dynamic in model as global exception', response)
        elif response.status_code == 469:
            raise SendStringInModelAsException('send string in model as global exception', response)
        elif response.status_code == 470:
            raise SendLongInModelAsException('send long in model as global exception', response)
        elif response.status_code == 471:
            raise SendNumberInModelAsException('send number in model as global exception', response)
        elif response.status_code == 472:
            raise SendPrecisionInModelAsException('send precision in model as global exception', response)
        elif response.status_code == 473:
            raise SendUuidInModelAsException('send uuid in model as global exception', response)
        elif response.status_code == 500:
            raise GlobalTestException('500 Global', response)
        elif (response.status_code < 200) or (response.status_code > 208):  # [200,208] = HTTP OK
            raise GlobalTestException('Invalid response.', response)
