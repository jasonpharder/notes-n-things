App.Router.map(function() {
	this.resource('home', { path : '/'}, function() {
		this.resource('mycourse', { path : ':course_id' } );
	});
	this.resource('notes', function() {
		this.resource('note', { path : ':note_id' } );
	});
	this.resource('courses', function() {
		this.resource('course', { path : ':course_id' } );
		this.resource('courseadd');
	});
	this.resource('users', function() {
		this.resource('user', { path : ':user_id' } );
	});
	this.resource('login');
});

App.CourseaddRoute = Ember.Route.extend({
  	model: function(){
    	// the model for this route is a new empty Ember.Object
    	return Em.Object.create({});
  	}
 });

App.MycourseRoute = Ember.Route.extend({
  	model: function(params) {
    	// the model for this route is a new empty Ember.Object
    	var string = '{"filters":[{"name":"courseid","op":"eq","val":'+params.course_id+'}]}'
    	return this.store.find('message', { q: string });
  	}
 });

App.HomeRoute = Ember.Route.extend(
{
	model: function() {
		return this.store.find('course');
	}
});

App.UsersRoute = Ember.Route.extend({
	model: function() {
		return this.store.find('user');
	}
});

App.UserRoute = Ember.Route.extend({
	model: function(params) {
		return this.store.find('user', params.user_id);
	}
});

App.CoursesRoute = Ember.Route.extend({
	model: function() {
		return this.store.find('course');
	}
});

App.CourseRoute = Ember.Route.extend({
	model: function(params) {
		return this.store.find('course', params.course_id);
	}
});

App.NotesRoute = Ember.Route.extend({
	model: function() {
		return this.store.find('note');
	}
});

App.NoteRoute = Ember.Route.extend({
	model: function(params) {
		return this.store.find('note', params.note_id);
	}
})
