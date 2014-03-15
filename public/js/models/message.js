App.Message = DS.Model.extend({
	message: DS.attr('string'),
	posttime:  DS.attr('date'),
	course:  DS.belongsTo('course'),
	user: DS.belongsTo('user')
})