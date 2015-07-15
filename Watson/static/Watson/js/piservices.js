/*
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
*/

$(document).ready(function() {
	hideStuff();
	ajaxStuff();
});


function hideStuff(){
	$('#id_traits').hide();
}

function ajaxStuff(){
}

function perform_pi(url){	
	var personality = $('#id_personality').val();
	var data = $('#id_data').val();
	
	$.ajax({
		type: 'POST',
		url: url,
		data: {"personality": personality,
		       "data": data},
		dataType: 'json',
		
		success: piOK,
		error: piNotOK
	});
		
	$('#id_response').text("Results will go here");
}

function piOK(response) {
	piresponse = JSON.parse('{"data":"the data"}');
	
	$('#id_response').text("Call was good - processing the Results");
	
	var results = response['results'];	
	var errMessage = results['error'];
	
	if (errMessage) {
		$('#id_response').text(errMessage);	
	}	
	else {
		var traits = response['traits'];
		if (traits) {
			$('#id_traitstable > tbody').empty();
			for (trait in traits)
			{
				var newRow = '<tr><td>' + trait + '</td><td>' + traits[trait] + '</td></tr>';
				$('#id_traitstable > tbody:last-child').append(newRow);
			}
			$('#id_response').text("Personality profile has completed");
			$('#id_traits').show();
		}
    }		
}

function piNotOK() {
	$('#id_response').text("Call was not so good");
}