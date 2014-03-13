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
