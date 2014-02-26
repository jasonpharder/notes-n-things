App.Router.map(function() {
  this.resource('notes');
  this.resource('courses');
  this.resource('login');
});

App.NotesRoute = Ember.Route.extend({
	model: function() {
		return this.store.find('noteTitle');
	}
});
