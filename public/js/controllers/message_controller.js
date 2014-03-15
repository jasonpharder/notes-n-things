App.MycourseController = Ember.ArrayController.extend({

        actions: {
                addMessage: function(messageText) {
                        var message = messageText;
                        
                        var c = this.store.find('course', 4);
                        var u = this.store.find('user', 1);

                        var messageAdd =this.store.createRecord('message', {
                                message: message,
                                posttime: "12:00pm",
                                courseid: 4,
                                userid: 1
                        });

                        messageAdd.save();
                }
        }
});
