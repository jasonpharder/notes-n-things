App.CourseaddController = Ember.ObjectController.extend({
	
        actions: {
                add: function(courseName, courseAltName) {
                        var name = courseName;
                        var altName = courseAltName;

			var cookie = document.cookie;			
			
			if (cookie.length != 0){
				var courseAdd =this.store.createRecord('course', {
                                	name: name,
                                	alt_name: altName,
                               		professor: 1 // This need to be the user logged in 
                        	});
                        	courseAdd.save();
				document.getElementById('coursesMsg').innerHTML = "Successfully added course";
			}
			else {
				document.getElementById('coursesMsg').innerHTML = "Please register or signin to create a course";
			}
                }
        }
});

// App.HomeController = Ember.ObjectController.extend({
//   messages: function() {
//     var messageId = this.get('id');
//     return this.get('store').filter('message', function(message) {
//       return message.get('message.id') == messageId;
//     });
//   }.property('messages')
// });
