App.Note = DS.Model.extend({
	uid: DS.attr(),
	stored_as: DS.attr('string'),
	file_name: DS.attr('string'),
	owner: DS.attr(),
	rating:DS.attr()
});

//Stub data for notes
/*App.Note.FIXTURES = [
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
];*/
