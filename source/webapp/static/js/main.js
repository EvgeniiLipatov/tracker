function getToken() {
    $.ajax({
        url: 'http://127.0.0.1:8000/api/login/',
        method: 'post',
        data: JSON.stringify({username: 'admin', password: 'admin'}),
        dataType: 'json',
        contentType: 'application/json',
        success: function(response, status){console.log(response); localStorage.setItem('apiToken', response.token);},
        error: function(response, status){console.log(response);}
    });

}

function getProjects() {
    $.ajax({
         url: 'http://127.0.0.1:8000/api/projects/',
         method: 'get',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         data: JSON.stringify({username: 'admin', password: 'admin'}),
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log(response);},
         error: function(response, status){console.log(response);}
    });

}

function getTasks() {
    $.ajax({
         url: 'http://127.0.0.1:8000/api/tasks/',
         method: 'get',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         data: JSON.stringify({username: 'admin', password: 'admin'}),
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log(response);},
         error: function(response, status){console.log(response);}
    });
}

function getProjectTasks() {
    $.ajax({
         url: 'http://127.0.0.1:8000/api/projects/2',
         method: 'get',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         data: JSON.stringify({username: 'admin', password: 'admin'}),
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log(response['tasks']);},
         error: function(response, status){console.log(response);}
    });

}


$(document).ready(function() {
   getToken();
   getProjects();
   getTasks();
   getProjectTasks();
});