$(document).ready(function(){
    $('#request-btn').on('click',function(){
       
       var sepalLength = $('#sepalLength').val();
       var sepalWidth = $('#sepalWidth').val();
       var petalLength = $('#petalLength').val();
       var petalWidth = $('#petalWidth').val();
 
       var body = {
          "sepal_length":sepalLength,
          "sepal_width":sepalWidth,
          "petal_length":petalLength,
          "petal_width":petalWidth
       };
 
       $.ajax({
          url:'http://127.0.0.1:5000/ai/predict-iris',
          headers:{
             'Content-Type':'application/json'
          },
          type:'POST',
          data:JSON.stringify(body),
          success:function(response){
             alert('분석완료');
             console.log(response)
             $('#result').html(response.message);
          },
          error:function(error){
             console.error(error);
          }
       });
 
    });
 })