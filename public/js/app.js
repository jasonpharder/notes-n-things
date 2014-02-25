App = Ember.Application.create();

App.Router.map(function() {
  this.resource('notes');
  this.resource('courses');
  this.resource('login');
});
