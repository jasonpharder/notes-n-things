App.Router.map(function() {
	this.resource('home', { path : '/'});
	this.resource('notes', function() {
		this.resource('note', { path : ':note_id' } );
	});
	this.resource('courses', function() {
		this.resource('course', { path : ':course_id' } );
	});
	this.resource('users', function() {
		this.resource('user', { path : ':user_id' } );
	});
	this.resource('login');
});

App.HomeRoute = Ember.Route.extend(
{
	model: function() {
		return this.store.find('course');
	}
})

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
