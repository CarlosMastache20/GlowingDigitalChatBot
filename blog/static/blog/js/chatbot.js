function getUserResponse(){
    var userText = $('#textInput').val()
    if(!$('#textInput').val()){
        Swal.fire({
        icon: 'warning',
        title: 'El mensaje esta vacio. Por favor escribe un mensaje.',
        showConfirmButton: false,
        timer: 1000
        });
    }else{
        var userHTML = "<div class='post post-user'><span class='span-user'> Tú: </span><span>"+userText + timeStamp()+"</span></div>";
        $('#textInput').val("");
        $scrollDown();
        $('#chatbot').append(userHTML);

        $.get('/blog/getResponse',{userMessage: userText}).done(function(data){
        var returnedMessage = "<div class='post post-bot'><span class='span-user'>Chatbot: </span><span>"+ data + timeStamp() +"</span></div>";
        const timeTyping = 500 + Math.floor(Math.random() * 2000);
        $('#chatbot').append(returnedMessage);
        $scrollDown();

    })
    }
}

$('#Send').click(function(){
    getUserResponse();
}) 

// Chat input
$("#textInput").on("keyup", (event) => {
if (event.which === 13)  getUserResponse();; 
});



function timeStamp() {
const timestamp = new Date();
const hours = timestamp.getHours();
let minutes = timestamp.getMinutes();
if (minutes < 10) minutes = "0" + minutes;
const html = `<span class="timestamp">${hours}:${minutes}</span>`;
return html;
};


function $scrollDown() {
const $container = $("#chatbot");
const $maxHeight = $container.height();
const $scrollHeight = $container[0].scrollHeight;
if ($scrollHeight > $maxHeight) $container.scrollTop($scrollHeight);
}