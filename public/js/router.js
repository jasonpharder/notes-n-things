App.Router.map(function() {
	this.resource('home', { path : '/'}, function() {
		this.resource('mycourse', { path : ':course_id' } );
	});
	this.resource('messages', function() {
		this.resource('message', { path : ':message_id' }, function()
		{
			this.resource('comments');
		});
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
	this.resource('logout');
	this.resource('createaccount');
});

App.LogoutRoute = Ember.Route.extend({
	model: function() {
	return Em.Object.create({});
	}
 });

App.LoginRoute = Ember.Route.extend({
	model: function() {
	return Em.Object.create({});
	}
 });

App.CreateaccountRoute = Ember.Route.extend({
	model: function() {
	//the model for this route is a new empty Ember.Object
	return Em.Object.create({});
	}
 });

App.CourseaddRoute = Ember.Route.extend({
  	model: function(){
    	// the model for this route is a new empty Ember.Object
    	return Em.Object.create({});
  	}
 });

App.MycourseRoute = Ember.Route.extend({
  	model: function(params) {
  		console.log(this.get('currCourse'));
  		this.set('currCourse', params.course_id);
  		console.log(this.get('currCourse'));
    	var string = '{"filters":[{"name":"courseid","op":"eq","val":'+params.course_id+'}]}'
    	return this.store.filter('message', { q: string }, function(message) {
      		return message.get('courseid')==params.course_id;
    	});
  	}
 });

App.HomeRoute = Ember.Route.extend(
{
	model: function() {
		return this.store.find('user', 1);
	}
});

App.MessagesRoute = Ember.Route.extend(
{
	model: function() {
		return this.store.find('message');
	}
});

App.MessageRoute = Ember.Route.extend({
	model: function(params) {
		return this.store.find('message', params.message_id);
		//return this.modelFor('messages').comments.findBy('id', params.comment_id);
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

