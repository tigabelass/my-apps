$(document).ready(function(){
    $('#note-form').submit(function(event){
        event.preventDefault();
        $.ajax({
            url : "{% url 'add_note' %}",
            type : "POST",
            data : $(this).serialize(),
            succes : function(response) {
                $('#note-list').append(
                    `<li><strong>${response.title}</strong>: ${response.content}</li>`
                );
                $('#note-list').reset();
            },
            error: function(xhr) {
                alert('Error: ' + xhr.responseText);
            }
        })
    })
})