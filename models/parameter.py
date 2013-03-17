# coding: utf-8
#
# Copyright 2013 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Model for an Oppia exploration parameter."""

__author__ = 'Sean Lip'

from base_model import BaseModel

from google.appengine.ext import ndb


class Parameter(BaseModel):
    """A parameter definition for an exploration."""
    # The name of the parameter
    name = ndb.StringProperty(required=True)
    # The data type of the parameter - for now only string or list
    type = ndb.StringProperty(required=False) # TODO: make required and make sure it doesn't break anything. for now assume string by default.
