App.Note = DS.Model.extend({
	file_name: DS.attr('string'),
	stored_as: DS.attr('string'),
	rating:    DS.attr(),
	noteID:    DS.attr(),
	owner:     DS.attr(),
	contents:  DS.attr('string')
});

//Stub data for notes
App.Note.FIXTURES = [
	{
		noteID:    1,
		id :       1,
		file_name: "Test Note",
		contents:  "test content"
	},
	{
		noteID:    2,
		id :       2,
		file_name: "Test Note 2",
		contents:  "test content 2"
	},
	{
		noteID:    3,
		id :       3,
		file_name: "Test Note 3",
		contents:  "test content 3"
	},
];