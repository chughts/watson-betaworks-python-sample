# -*- coding: utf-8 -*-
# Copyright 2015 IBM
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.contrib.auth.models import User
from django.db.utils import IntegrityError 

import logging

logger = logging.getLogger(__name__)

class MainProgram(object):
  def __init__(self):
    try:
      User.objects.create_superuser(username='xxxx',password='yyyy',email='me@myco.com')
    except IntegrityError as e:
      logger.warning("DB Error Thrown %s" % e)

go = MainProgram()

 