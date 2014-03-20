module("Testing the homepage", {
	setup: function() {
		App.reset();
		App.injectTestHelpers();
	}
});

test("App Instantiation", function() {
	equal(
		App.constructor, Ember.Application,
		'App is an Ember App!'
	);
});

test("Does the homepage work correctly", function() {
	visit("/")
		.find("ul#home-sidebar")
		.then(function(sidebar) {
			equal(sidebar.length, 1, 'found homepage course sidebar');
		});

	visit("/")
		.find("h1#home-header")
		.then(function(header){
			equal(header.length, 1, 'found homepage header');
		});

});

test("Does the notes page work correctly", function() {

	visit("/notes")
		.find("button#create-note")
		.then(function(button) {
			equal(button.length, 1, 'found create note button');
		});

	visit("/notes")
		.find("div#notes-sidebar")
		.then(function(sidebar){
			equal(sidebar.length, 1, 'found notes sidebar');
		});

	visit("/notes")
		.find("h1#notes-header")
		.then(function(header){
			equal(header.length, 1, "found notes header");
		});

});

test("Does the courses page work correctly", function(){

	visit("/courses")
		.find("ul#courses-sidebar")
		.then(function(sidebar) {
			equal(sidebar.length, 1, 'found courses sidebar');
		});

	visit("/courses")
		.click("a[href$=\"courseadd\"]")
		.find("div#course-container")
		.then(function(form){
			equal(form.length, 1, 'add course form successfully loads')
		});

	visit("/courses")
		.find("h1#courses-header")
		.then(function(header){
			equal(header.length, 1, "found courses header");
		});
});

test("Does the login page work correctly", function(){

	visit("/login")
		.find("form#signin-form")
		.then(function(form) {
			equal(form.length, 1, 'found login form');
		});

	visit("/login")
		.find("input#email-field")
		.then(function(field) {
			equal(field.length, 1, 'found email field');
		});

	visit("/login")
		.find("input#password-field")
		.then(function(field) {
			equal(field.length, 1, 'found password field');
		});

	visit("/login")
		.find("input#remember-checkbox")
		.then(function(checkbox) {
			equal(checkbox.length, 1, 'found remember me checkbox');
		});

	visit("/login")
		.find("button#signin-button")
		.then(function(button) {
			equal(button.length, 1, "found signin button");
		});

	visit("/login")
		.find("button#register-link")
		.then(function(button) {
			equal(button.length, 1, "found register link");
		});

});

test("Does the users page work correctly", function(){

	visit("/users")
		.find("ul#users-sidebar")
		.then(function(sidebar) {
			equal(sidebar.length, 1, 'found users sidebar');
		});

	visit("/users")
		.find("h1#users-header")
		.then(function(header) {
			equal(header.length, 1, "found users header");
		});

});
