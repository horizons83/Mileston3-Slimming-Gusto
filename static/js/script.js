$(document).ready(function(){
  $('.sidenav').sidenav();
  $('.slider').slider();
  $('.tooltipped').tooltip();
  $('.collapsible').collapsible();
  $('select').formSelect();

  // Add ingredient input line on the edit/add recipe form:
  $(".add-ingred").click(function () {
      $(".ingre-input").append('<input class=ingredients id="ingredients" name="ingredients" type="text" placeholder="ingredient" aria-label="ingredient input" required> ');
      $(".remove-ingred").show();
  }); 
  // Add method input line on edit/add recipe form:
  $(".add-method").click(function () {
      $(".method-input").append(' <input class="method" name="method" type="text" placeholder="Add Method Step" aria-label="method input" required> ');
      $(".remove-method").show();
  });  
  // Remove last ingredient  added on edit/add recipe form:
  $(".remove-ingred").click(function () {
      $(".ingredients").last().remove();
  });  
  // Remove last method input:
  $(".remove-method").click(function () {
      $(".method").last().remove();
  });  
  // Show delete confirmation on button press:
  $(".delete-btn").click(function () {
      $(this).next().show();
  }); 
  // Hide delete confirmation:
  $(".cancel-delete-btn").click(function () {
      $(this).parent().hide();
  });
});