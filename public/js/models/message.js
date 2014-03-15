App.Message = DS.Model.extend({
	message: DS.attr('string'),
	posttime:  DS.attr('string'),
	course:  DS.belongsTo('course'),
	user: DS.belongsTo('user'),
	courseid:  DS.attr(),
	userid: DS.attr()
})