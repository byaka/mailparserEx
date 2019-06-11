#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright 2018 Fedele Mantuano (https://www.linkedin.com/in/fmantuano/)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


__all__ = (
    "MailParserExError",
    "MailParserExOutlookError",
    "MailParserExEnvironmentError",
    "MailParserExOSError",
    "MailParserExReceivedParsingError"
)


class MailParserExError(Exception):
    """
    Base MailParserEx Exception
    """
    pass


class MailParserExOutlookError(MailParserExError):
    """
    Raised when there is an error with Outlook integration
    """
    pass


class MailParserExEnvironmentError(MailParserExError):
    """
    Raised when the environment is not correct
    """
    pass


class MailParserExOSError(MailParserExError):
    """
    Raised when there is an OS error
    """
    pass


class MailParserExReceivedParsingError(MailParserExError):
    """
    Raised when a received header cannot be parsed
    """
    pass
