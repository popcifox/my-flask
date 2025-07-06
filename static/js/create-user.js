$(document).ready(function(){
    $('#search-address-btn').on('click',function(){
        new daum.Postcode({
            oncomplete: function(data) {
                $('#address').val(data.address);
             }
        }).open();
    });


    //회원가입
    $("#create-user-btn").on('click', function(){
        var id = $('#user-id').val();
        var pw = $('#password').val();
        var confirmPw = $('#confirm_password').val();
        var nick = $('#nickname').val();
        var addr = $('#address').val();


        //유효성 검사
        if(id == ''){
            alert('아이디를 입력해주세요.');
            return;
        }
        if(pw == ''){
            alert('비밀번호를 입력해주세요.');
            return;
        }
        if(confirmPw == ''){
            alert('비밀번호 확인을 입력해주세요');
            return;
        }
        if(pw != confirmPw){
            alert('비밀번호가 일치하지 않습니다.');
            return;
        }
        if(nick == ''){
            alert('닉네임을 입력해주세요.');
            return;
        }
        if(addr == ''){
            alert('주소를 입력해주세요.');
            return;
        }

        console.log(id,pw,confirmPw,nick,addr);
        var body = {
            id : id,
            pw : pw,
            nick: nick,
            addr: addr
        };

        $.ajax({
            url : 'http://127.0.0.1:5000/user/save',
            type: 'POST',
            data : JSON.stringify(body),
            contentType : 'application/json',
            success : function(response){
                if(response.success==true){
                    alert(response.message);
                    window.location.href = '/';
                }else {
                    alert(response.message);
                }
            },
            error: function(error){}
        });
    });
});