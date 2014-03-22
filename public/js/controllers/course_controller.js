App.CourseaddController = Ember.ObjectController.extend({

        actions: {
                add: function(courseName, courseAltName) {
                        var name = courseName;
                        var altName = courseAltName;
                        var courseAdd =this.store.createRecord('course', {
                                name: name,
                                alt_name: altName,
                                professor: 1 // This need to be the user logged in 
                        });
                        courseAdd.save();
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
