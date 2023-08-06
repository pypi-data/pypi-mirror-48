# -*- coding: utf-8 -*-

"""
tester

This file was automatically generated for Stamplay by APIMATIC v2.0 (
 https://apimatic.io ).
"""

from tester.api_helper import APIHelper
import tester.exceptions.api_exception
import tester.models.add_long_in_global_exception


class SendLongInModelAsException(tester.exceptions.api_exception.APIException):
    def __init__(self, reason, response):
        """Constructor for the SendLongInModelAsException class

        Args:
            reason (string): The reason (or error message) for the Exception
                to be raised.
            response (HttpResponse): The HttpResponse of the API call.

        """
        super(SendLongInModelAsException, self).__init__(reason, response)
        dictionary = APIHelper.json_deserialize(self.response.raw_body)
        if isinstance(dictionary, dict):
            self.unbox(dictionary)

    def unbox(self, dictionary):
        """Populates the properties of this object by extracting them from a dictionary.

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        """
        self.body = tester.models.add_long_in_global_exception.AddLongInGlobalException.from_dictionary(dictionary.get('body')) if dictionary.get('body') else None
