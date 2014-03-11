// put app in qunit-fixture
window.App = Ember.Application.create({
  rootElement: '#qunit-fixture'
});

// turn on testing mode
window.App.setupForTesting();

test( "hello test", function() {
  ok( 1 == "1", "Passed!" );
});

test("App Instantiation", function() {
  equal(
    App.constructor, Ember.Application,
    'App is an Ember App!'
  );
});

//test( "", function () {
//	var courses = this.store.find('course');/
//	alert(courses);
//	ok( 1== "1", "Passed!");
//})