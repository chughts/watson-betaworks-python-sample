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

from django.conf.urls import patterns, include, url
#from Watson import views
from Watson.views.IndexView import BFIndexView
from Watson.views.DetailView import BFDetailView

urlpatterns = patterns('',
    url(r'^$', BFIndexView.as_view(), name='personalities'),
    url(r'^(?P<pk>\d+)/$', BFDetailView.as_view(), name='detail'),
)