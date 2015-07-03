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

import json
import base64

from django import forms
from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt

from Watson.models import Big5Traits

from Watson.watsonutils.wdc import WDCService
from Watson.watsonutils.pinsights import Pidata

class Form_pi(forms.Form):
  personality = forms.CharField()
  data = forms.CharField()

	
def piindex(request):  
  wdc = WDCService('PI')
  service_creds = wdc.getCreds()
  
  form = Form_pi()    
  service_creds['form'] = form 
  return render(request, 'Watson/piindex.html', service_creds)

  
@csrf_exempt 
def pireq(request):
  theData= {}
  
  if request.POST:  
    form = Form_pi(request.POST)
    theResponse = {"Response":"No Response as form not deemed valid"}

    if form.is_valid():
      personality = form.cleaned_data["personality"]
      data = form.cleaned_data["data"]

      theData["personality"] = personality
      theData["data"] = data

      theResponse = processPIRequest(request, theData)

  return HttpResponse(json.dumps(theResponse), content_type="application/json") 


def processPIRequest(request, theData):
  wdc = WDCService('PI')
  service_creds = wdc.getCreds()
  
  data = theData["data"]
  personality = theData["personality"]
	  
  results = wdc.performOperation(data)  
  service_creds['results'] = results
  pi = Pidata(results)
  
  keys = pi.big5keys()
  
  traits = {}
  for trait in keys:  
    traits[trait] = pi.getTraitValue(trait, False)  

  service_creds["traits"] = traits    
  savePersonality(personality, pi)	  
  
  return service_creds
  
def savePersonality(personality, pidata): 
  # If there is no big 5 data then no need to save
  if "No value" in pidata.getOpennessValue():
    return
  else:	
    new_traits = Big5Traits(personality=personality,
	                        Openness=pidata.getOpennessValue(),
							Conscientiousness=pidata.getConscientiousnessValue(),
							Extraversion=pidata.getExtraversionValue(),
							Agreeableness=pidata.getAgreeablenessValue(),
							Emotional_range=pidata.getEmotionalrangeValue())
    new_traits.save()
  