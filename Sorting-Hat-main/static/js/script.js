$(document).ready(function () {
  $('#myForm').on ('submit', function (e) {
      e.preventDefault(); // Prevent the default form submission

      // Serialize the form data
      const formData = $(this).serialize();

      // Send a POST request to the Flask route
      $.ajax({
          type: 'POST',
          url: '/submit_form',
          data: formData,
          dataType: 'json',
          success: function (response) {
              // Update the result div wisth the response data
              var responseData = response.user_name;

              window.localStorage.setItem('myData', responseData);

              //$('#L').html(responseData);
              
          },
          error: function (error) {
              console.error('Error:', error);
          }
      });
  });
});

