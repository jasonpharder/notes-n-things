App.Course = DS.Model.extend({
	title:    DS.attr('string'),
	uid:      DS.attr('string'),
	contents: DS.attr('string')
})

//stub Data for courses
App.Course.FIXTURES = [
	{
		uid:      "1",
		id :      1,
		title:    "Test Course",
		contents: "test content"
	},
	{
		uid:      "2",
		id :      2,
		title:    "Test Course 2",
		contents: "test content 2"
	},
	{
		uid:      "3",
		id :      3,
		title:    "Test Course 3",
		contents: "test content 3"
	},
]