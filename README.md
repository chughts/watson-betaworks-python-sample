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

# watson-betaworks-python-sample

This is a sample python application created by IBM Betaworks to 
show how a sample set of the Watson APIs can be used.

To run locally 
python manage.py runserver --settings=cognitive.settings.local

To run on bluemix
python manage.py runserver --settings=cognitive.settings.bluemix

On bluemix the application needs the following services (edit the manifest.yml file to match the 
instance names for your environment

1. postgresql
2. personality insights
3. tradeoff analytics