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
         url: 'http://127.0.0.1:8000/api/projects/2/',
         method: 'get',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         data: JSON.stringify({username: 'admin', password: 'admin'}),
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log(response['tasks']);},
         error: function(response, status){console.log(response);}
    });

}

function CreateTask() {
    data = {
        username:"fedya",
        password: "M1234q",
        "brief": "test1000",
        "description": "just_for_fun_11",
        "status": 2,
        "type": 1,
        "project": 1,
       // "created_at": "2019-12-09T11:50:50.694108Z",
       // "updated_at": "2019-12-09T11:50:50.694159Z",
        "created_by": 1

    };
    $.ajax({
         url: 'http://127.0.0.1:8000/api/tasks/',
         method: 'post',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         //data: JSON.stringify({username: 'fedya', password: 'M1234q'}),
         data: JSON.stringify(data),
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log(response);},
         error: function(response, status){console.log(response);}
    });

}

function DeleteTask() {
    $.ajax({
         url: 'http://127.0.0.1:8000/api/tasks/11',
         method: 'delete',
         headers: {'Authorization': 'Token ' + localStorage.getItem('apiToken')},
         dataType: 'json',
         contentType: 'application/json',
         success: function(response, status){console.log("Deleted");},
         error: function(response, status){console.log("Not deleted");}
    });

}

$(document).ready(function() {
   getToken();
   getProjects();
   getTasks();
   getProjectTasks();
   CreateTask();
   DeleteTask();
});