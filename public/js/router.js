App.Router.map(function() {
  this.resource('notes', function() {
  	this.resource('note', {path : ':note_id'} );
  });
  this.resource('courses');
  this.resource('login');
});

App.NotesRoute = Ember.Route.extend({
	model: function() {
		return this.store.find('note');
	}
});
