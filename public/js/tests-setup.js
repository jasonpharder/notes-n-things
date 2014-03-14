// put app in qunit-fixture
window.App = Ember.Application.create({
  rootElement: '#qunit-fixture'
});

App.Store = DS.Store.extend({
    revision: 12,
    adapter: DS.RESTAdapter.reopen({
        namespace: 'api'
    })
});

// turn on testing mode
window.App.setupForTesting();
