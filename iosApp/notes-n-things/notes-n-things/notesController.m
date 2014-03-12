//
//  notesController.m
//  notes-n-things
//
//  Created by Joshua Drad on 2014-03-03.
//  Copyright (c) 2014 Comp4350. All rights reserved.
//

#import "notesController.h"

@implementation notesController

- (void)viewDidLoad
{
    [super viewDidLoad];
	// Do any additional setup after loading the view, typically from a nib.
    
    
    notesList.text = @"Notes:";
    
    NSMutableURLRequest *request = [[NSMutableURLRequest alloc] init];
    [request setURL:[NSURL URLWithString:@"http://www.notes-n-things.tk/notes"]];
    [request setHTTPMethod:@"GET"];
    [request setValue:@"application/json;charset=UTF-8" forHTTPHeaderField:@"Content-Type"];
    
    NSURLResponse *response;
    NSData *allNotesData = [NSURLConnection sendSynchronousRequest:request returningResponse:&response error:nil];
  
    NSError *error;
    NSMutableDictionary *allNotes = [NSJSONSerialization JSONObjectWithData:allNotesData options:NSJSONReadingMutableContainers error:&error];
    
    if (error) {
        
        NSLog(@"%@", [error localizedDescription]);
    }
    
    else {        
        NSArray *notesArray = allNotes[@"notes"];
        
        float _height = 25;
        float _y = 110;
        for (NSDictionary *note in notesArray){
           
            UIButton *noteBtn = [UIButton buttonWithType:UIButtonTypeRoundedRect];
            [noteBtn setTitle:[NSString stringWithFormat:@" %@\n", note[@"file_name"]]forState:UIControlStateNormal];
            [noteBtn setFrame:CGRectMake(10, _y, 200, _height)];
            [noteBtn addTarget:self action:@selector(noteDetail) forControlEvents:UIControlEventTouchUpInside];
            
            [self.view addSubview:noteBtn];
            _y = _y + _height;
            
            NSLog(@"---");
            NSLog(@"name %@", note[@"file_name"]);
            NSLog(@"alt Name %@", note[@"contents"]);
            NSLog(@"---");
            
        }
    }
}

- (void)didReceiveMemoryWarning
{
    [super didReceiveMemoryWarning];
    // Dispose of any resources that can be recreated.
}

- (IBAction)noteDetail
{
    
    noteController *noteControllerView = [self.storyboard instantiateViewControllerWithIdentifier:@"noteControllerView"];
    [self.navigationController pushViewController:noteControllerView animated:YES];
}

@end